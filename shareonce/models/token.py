from sqlalchemy import *
from sqlalchemy.orm import relationship

from . import Base, DBSession, URL_ENCODER

from datetime import datetime, timedelta

import logging
log = logging.getLogger('shareonce.models.token')


class Token(Base):
    __tablename__ = 'token'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uploadid = Column(Integer(), ForeignKey('upload.id', onupdate='cascade',
                      ondelete='cascade'))
    created = Column(DateTime, default=datetime.utcnow())

    upload = relationship('Upload', backref='tokens')

    def __init__(self, uploadid):
        self.uploadid = uploadid

    @classmethod
    def create(cls, uploadid):
        t = Token(uploadid)

        DBSession.add(t)
        DBSession.flush()

        return t

    @property
    def urlid(self):
        return URL_ENCODER.encode_url(self.id)

    @urlid.setter
    def urlid(self, value):
        self.id = URL_ENCODER.decode_url(value)

    @classmethod
    def get_by_urlid(self, urlid):
        return DBSession.query(Token).filter(
            Token.id == URL_ENCODER.decode_url(urlid))\
            .filter(Token.created >
                    (datetime.utcnow() - timedelta(hours=1))).one()
