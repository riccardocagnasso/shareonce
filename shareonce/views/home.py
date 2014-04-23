from pyramid.view import view_config

import logging
log = logging.getLogger('shareonce.views.home')


@view_config(route_name='home', renderer='home.mak')
def home(request):
    return {}


@view_config(route_name='privacy', renderer='privacy.mak')
def privacy(request):
    return {}
