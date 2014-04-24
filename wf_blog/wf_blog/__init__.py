# -*-coding:utf-8 -*-
import pymongo

from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
from pyramid.request import Request

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from wf_blog.security import groupfinder
from wf_blog.model import User, RootFactory

from wf_blog import routers

from pyramid.threadlocal import get_current_registry
from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import unauthenticated_userid
class RequestWithUserAttribute(Request):
    @reify
    def user(self):
        userid = unauthenticated_userid(self)
        if userid is not None:
            settings = get_current_registry().settings
            user = User.get_user(self.mongodb, userid)
            return user

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    # auth
    authn_policy = AuthTktAuthenticationPolicy(settings['security'], callback=groupfinder)
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings, root_factory=RootFactory)

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    # jinja2
    from pyramid_jinja2 import renderer_factory
    config.include('pyramid_jinja2')
    config.add_renderer('.html', renderer_factory)
    config.add_static_view('static', 'wf_blog:static', cache_max_age=3600)

    # bind user to request
    config.set_request_factory(RequestWithUserAttribute)

    # set routers and views
    routers.includeme(config)
    config.scan("wf_blog.views")

    # MongoDB
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        db.authenticate(settings['mongodb.db_user'], settings['mongodb.passwd'])
        event.request.mongodb = db
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
