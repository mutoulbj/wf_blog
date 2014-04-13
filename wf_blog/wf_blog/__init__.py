# -*-coding:utf-8 -*-
import pymongo

from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest

from wf_blog import routers

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    from pyramid_beaker import session_factory_from_settings
    from pyramid_beaker import set_cache_regions_from_settings
    # auth
    from pyramid.authentication import SessionAuthenticationPolicy
    from pyramid.authorization import ACLAuthorizationPolicy
    from wf_blog.auth import auth
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'wf_blog')
    set_cache_regions_from_settings(settings)
    session_factory = session_factory_from_settings(settings)

    config = Configurator(session_factory=session_factory,
                          authentication_policy=SessionAuthenticationPolicy(prefix='auth', callback=auth),
                          authorization_policy=ACLAuthorizationPolicy(),
                          settings=settings,
                          )

    # jinja2
    from pyramid_jinja2 import renderer_factory
    config.include('pyramid_jinja2')
    config.add_renderer('.html', renderer_factory)
    config.add_static_view('static', 'wf_blog:static', cache_max_age=3600)

    # set routers and views
    routers.includeme(config)
    config.scan("wf_blog.views")

    # MongoDB
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db
    db_uri = settings['mongodb.url']
    MongoDB = pymongo.Connection
    conn = MongoDB(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)

    if 'pyramid_debugtoolbar' in set(settings.values()):
        class MongoDB(pymongo.Connection):
            def __html__(self):
                return 'MongoDB: <b>{}></b>'.format(self)

    application = config.make_wsgi_app()
    return application
