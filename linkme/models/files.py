from sqlalchemy import *

import Image as PIL_image
import magic
import hashlib
import os.path
import shutil
import transaction

from . import Base, DBSession
from sqlalchemy.exc import IntegrityError

import logging
log = logging.getLogger('tesolvents.models.file')


class File(Base):
    __tablename__ = 'file'
    __mapper_args__ = dict(with_polymorphic="*",
                           polymorphic_on='kind',
                           polymorphic_identity=u'file')

    kind = Column(Unicode, nullable=False)

    hash = Column(Unicode, primary_key=True)
    mime = Column(Unicode, nullable=False)
    filename = Column(Unicode, nullable=False)

    def __init__(self, filep, filename):
        self.mime = unicode(magic.from_file(filep, magic.MAGIC_MIME))
        self.filename = filename

        #calculate the hash in efficent way
        s = hashlib.sha256()
        for b in open(filep):
            s.update(b)

        self.hash = unicode(s.hexdigest())

    @classmethod
    def create(cls, filep, filename):
        f = cls(filep, filename)

        DBSession.add(f)
        try:
            DBSession.flush()
        except IntegrityError as e:
            transaction.abort()
            return File.get(f.hash)
        return f

    @classmethod
    def get(cls, hash):
        return DBSession.query(File).filter(File.hash == hash).one()

    def get_file_path(self):
        pass

    def __repr__(self):
        return "File: hash={0}".\
            format(self.hash)


class Image(File):
    __tablename__ = 'image'
    __mapper_args__ = dict(polymorphic_on='kind',
                           polymorphic_identity=u'image')

    hash = Column(Unicode, ForeignKey(
        File.hash, onupdate="CASCADE",
        ondelete="CASCADE"), primary_key=True)

    height = Column(Integer)
    width = Column(Integer)

    thumbnail_width = Column(Integer)
    thumbnail_height = Column(Integer)

    mini_thumbnail_width = Column(Integer)
    mini_thumbnail_height = Column(Integer)

    thumbnails_resize_width, thumbnails_resize_height = 300, None
    mini_thumbnails_resize_width, mini_thumbnails_resize_height = None, 100

    def __init__(self, filep, filename):
        super(Image, self).__init__(filep, filename)

        self.save_to_file(filep)
        self.calculate_dimensions()

        self.thumbnail_width, self.thumbnail_height =\
            self.save_thumbnail(
                'thumbnails',
                self.thumbnails_resize_width, self.thumbnails_resize_height)

        self.mini_thumbnail_width, self.mini_thumbnail_height =\
            self.save_thumbnail(
                'mini_thumbnails', self.mini_thumbnails_resize_width,
                self.mini_thumbnails_resize_height)

    def get_file_path(self, action='read'):
        return os.path.join(t.media_directory.get('images', action), self.hash)

    def get_image_path(self):
        return self.get_file_path()

    def get_thumbnail_path(self, action='read'):
        return os.path.join(t.media_directory.get('thumbnails', action),
                            self.hash)

    def get_mini_thumbnail_path(self, action='read'):
        return os.path.join(t.media_directory.get('mini_thumbnails', action),
                            self.hash)

    def save_to_file(self, image_file):
        image_path = t.media_directory.get('images')

        ouf = open(os.path.join(image_path, self.hash), 'w')

        for d in open(image_file):
            ouf.write(d)

    def calculate_dimensions(self):
        image = PIL_image.open(self.get_file_path(action='write'), 'r')

        self.width, self.height = image.size

    def save_thumbnail(self, itype, width, height):
        thumb_path = os.path.join(t.media_directory.get(itype),
                                  self.hash)
        image_path = self.get_file_path(action='write')

        image = PIL_image.open(image_path)

        if height is None and width is not None:
            height = int(float(image.size[1])/float(image.size[0])*width)
        elif height is not None and width is None:
            width = int(float(image.size[0])/float(image.size[1])*height)

        thumb = image.resize((width, height), PIL_image.ANTIALIAS)

        if thumb.mode != 'RGB':
            thumb = thumb.convert('RGB')

        thumb.save(thumb_path, "PNG", optimize=True)

        image_size = os.path.getsize(image_path)
        thumb_size = os.path.getsize(thumb_path)

        #if the thumbnail is bigger than the original image, we discard it
        if(thumb_size >= image_size):
            shutil.copy(image_path, thumb_path)
            return self.width, self.height
        else:
            return width, height
