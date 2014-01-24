from pyramid.view import view_config
from pyramid.response import FileResponse
from pyramid.httpexceptions import HTTPNotFound

from ..models import File, Upload, Token

from sqlalchemy.orm.exc import NoResultFound

import logging
log = logging.getLogger('shareonce.views.file')


@view_config(route_name='file.upload', renderer='json')
def file_upload(request):

    for item, filestorage in request.POST.items():
        f = File.create(filestorage)

        u = Upload.create(f.hash)

    return {
        'url': request.route_url('file.get', uploadid=u.urlid)
    }


@view_config(route_name='file.get', renderer='getfile.mak')
def file_get(request):
    try:
        upload = Upload.get_by_urlid(request.matchdict.get('uploadid'))
    except NoResultFound:
        return HTTPNotFound()

    t = Token.create(upload.id)
    upload.tickets -= 1

    request.response.headers['refresh'] = '5; URL={0}'.\
        format(request.route_url('file.serve', token=t.urlid))

    return {'token': t}


@view_config(route_name='file.serve')
def file_serve(request):
    try:
        t = Token.get_by_urlid(request.matchdict.get('token'))
    except NoResultFound:
        return HTTPNotFound()

    f = t.upload.file

    fr = FileResponse(
        f.get_file_path(),
        request=request,
        content_type=str(f.mime)
        )

    fr.content_disposition = 'filename="{0}"'.format(str(f.filename))

    return fr
