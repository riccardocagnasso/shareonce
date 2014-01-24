from pyramid.view import view_config

import logging
log = logging.getLogger('linkme.views.home')


@view_config(route_name='home', renderer='home.mak')
def home(request):
    return {}
