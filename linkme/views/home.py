from pyramid.view import view_config

import logging
log = logging.getLogger('linkme.views.files')


@view_config(route_name='home', renderer='home.mak')
def home(request):
    return {}