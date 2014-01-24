from pyramid.config import Configurator
from sqlalchemy import engine_from_config
import os

from .models import (
    DBSession,
    Base,
    )


class UploadDirectory(object):
    directories = {'files': 'files'}

    def __init__(self, write_dir=None, read_dir=None):
        self.write_dir = write_dir
        if read_dir is not None:
            self.read_dir = read_dir
        else:
            self.read_dir = write_dir

        self.init_base_dir()

    def init_base_dir(self):
        if self.write_dir is not None and os.path.exists(self.write_dir):
            for d in self.directories.values():
                if not os.path.exists(self.get(d)):
                    os.makedirs(self.get(d))

    def set_base(self, write_dir, read_dir=None):
        self.write_dir = write_dir
        if read_dir is not None:
            self.read_dir = read_dir
        else:
            self.read_dir = write_dir

        self.init_base_dir()

    def get(self, dir, action='write'):
        if action == 'write':
            return os.path.join(self.write_dir, self.directories[dir])
        else:
            return os.path.join(self.read_dir, self.directories[dir])

    def get_file_path(self, dir, filename, action='write'):
        return os.path.join(self.get(dir, action), filename)

upload_directory = UploadDirectory()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_mako')

    upload_directory.set_base(settings['upload_directory'])

    #assetgen
    config.include('pyramid_assetgen')

    config.add_static_view(name='s', path='linkme:static/dist',
                                cache_max_age=3600)
    config.add_assetgen_manifest(
        'linkme:static/dist',
        manifest_file="linkme:static/assets.json")

    config.add_static_view('static', 'linkme:static/static',
                           cache_max_age=3600)

    config.add_route('home', '/')

    config.add_route('file.upload', '/upload')
    config.add_route('file.get', '/gf/{uploadid}')
    config.add_route('file.serve', '/file/{token}')

    config.scan()
    return config.make_wsgi_app()
