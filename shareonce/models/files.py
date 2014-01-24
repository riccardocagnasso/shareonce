from sqlalchemy import *

import magic
import hashlib
import shutil
import transaction
import tempfile

from . import Base, DBSession, URL_ENCODER
from .token import Token
import shareonce
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship

from datetime import datetime, timedelta

import logging
log = logging.getLogger('shareonce.models.files')


class Upload(Base):
    """
    The upload of one file
    """
    __tablename__ = 'upload'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(Unicode, ForeignKey('file.hash', onupdate='CASCADE',
                  ondelete='CASCADE'))
    file = relationship('File', backref='uploads')
    tickets = Column(Integer, default=1)

    created = Column(DateTime, default=datetime.utcnow())

    def __init__(self, hash):
        self.hash = hash

    @classmethod
    def create(cls, hash):
        u = Upload(hash)
        DBSession.add(u)
        DBSession.flush()

        return u

    @property
    def urlid(self):
        return URL_ENCODER.encode_url(self.id)

    @urlid.setter
    def urlid(self, value):
        self.id = URL_ENCODER.decode_url(value)

    @classmethod
    def get_by_urlid(self, urlid):
        return DBSession.query(Upload).filter(
            Upload.id == URL_ENCODER.decode_url(urlid)).filter(
            Upload.tickets > 0).one()


class File(Base):
    __tablename__ = 'file'
    __mapper_args__ = dict(with_polymorphic="*",
                           polymorphic_on='kind',
                           polymorphic_identity=u'file')

    kind = Column(Unicode, nullable=False)

    hash = Column(Unicode, primary_key=True)
    mime = Column(Unicode, nullable=False)
    filename = Column(Unicode, nullable=False)

    def __init__(self, filestorage):
        #calculate the hash in efficent way
        temp = tempfile.NamedTemporaryFile(delete=False, mode='w')

        s = hashlib.sha256()
        for b in filestorage.file:
            s.update(b)
            temp.write(b)

        temp.close()

        self.hash = unicode(s.hexdigest())
        self.mime = unicode(magic.from_file(temp.name, magic.MAGIC_MIME))
        self.filename = filestorage.filename

        shutil.move(temp.name, shareonce.upload_directory.get_file_path('files',
                    self.hash))

    @classmethod
    def create(cls, filestorage):
        f = cls(filestorage)

        DBSession.add(f)
        try:
            DBSession.flush()
        except IntegrityError as e:
            log.debug(e)
            transaction.abort()
            return File.get(f.hash)
        return f

    @classmethod
    def get(cls, hash):
        return DBSession.query(File).filter(File.hash == hash).one()

    def get_file_path(self, action='read'):
        return shareonce.upload_directory.get_file_path(
            'files', self.hash, action)

    def __repr__(self):
        return "File: hash={0}".\
            format(self.hash)

    @classmethod
    def find_unused(cls, delay=24):
        return DBSession.query(File).join(Upload).outerjoin(Token)\
            .filter(or_(Upload.created < (datetime.utcnow() - timedelta(hours=72)), 
                and_(Upload.tickets < 1, Token.created <
                    (datetime.utcnow() - timedelta(hours=delay)))))
