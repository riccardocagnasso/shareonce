from pyramid.view import view_config
from pyramid.request import Request
from pyramid.response import FileResponse
from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import Response

from ..models import File, Upload, Token, DBSession

from sqlalchemy.orm.exc import NoResultFound

import logging
log = logging.getLogger('shareonce.views.file')


from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from socketio.mixins import BroadcastMixin

import transaction

max_size = 20 * pow(2, 20)

class FileNamespace(BaseNamespace):
    def on_upload(self, data):
        log.debug('on upload')
        self.file = File(data)
        self.size = 0

        transaction.commit()

    def on_chunk(self, chunk):
        log.debug('on chunk')
        self.size += len(chunk)
        if self.size > max_size:
            self.file = None
            self.size = 0
            self.emit('toobig')
            log.debug('TOO BIG! EXTERMINATE! EXTERMINATE!')
            self.disconnect()
        else:
            if self.file.addChunk(chunk):
                f = self.file.save()

                u = Upload.create(f.hash)

                self.emit(
                    'filedone',
                    {'url': self.request.route_url(
                        'file.get', uploadid=u.urlid)})
                self.file = None
                self.size = 0
            else:
                self.emit('chunkdone')

            transaction.commit()


@view_config(route_name='socket_io')
def socketio_service(request):
    socketio_manage(request.environ, {'/file': FileNamespace},
                    request)

    return request.response


@view_config(route_name='file.get', renderer='getfile.mak')
def file_get(request):
    try:
        upload = Upload.get_by_urlid(request.matchdict.get('uploadid'))
    except NoResultFound:
        log.debug('NOT FOUND')
        return HTTPNotFound()

    t = Token.create(upload.id)
    upload.tickets -= 1

    request.response.headers['refresh'] = '5; URL={0}'.\
        format(request.route_url('file.serve', token=t.urlid))

    return {'token': t}


@view_config(route_name='file.serve')
def file_serve(request):
    serve_engine = request.registry.settings.get('serve_engine', 'local')

    try:
        t = Token.get_by_urlid(request.matchdict.get('token'))
    except NoResultFound:
        return HTTPNotFound()

    f = t.upload.file

    if serve_engine == 'nginx':
        print(f.get_file_path())
        headers = request.response.headers
        headers['Content-Disposition'] = str(f.filename)
        headers['Content-Type'] = 'application/force-download'
        headers['Accept-Ranges'] = 'bytes'
        headers['X-Accel-Redirect'] = '/getfile/'+f.hash+';'
        return request.response
    else:
        fr = FileResponse(
            f.get_file_path(),
            request=request,
            content_type=str(f.mime)
            )

        fr.content_disposition = 'filename="{0}"'.format(str(f.filename))

        return fr
