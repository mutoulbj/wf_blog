from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
import pymongo

from wf_blog.resources import Root

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=Root)
    config.add_view('wf_blog.views.my_view',
                    context='wf_blog:resources.Root',
                    renderer='wf_blog:templates/mytemplate.html')

    # jinja2
    from pyramid_jinja2 import renderer_factory
    config.include('pyramid_jinja2')
    config.add_renderer('.html', renderer_factory)
    config.add_static_view('static', 'wf_blog:static', cache_max_age=3600)
    
    # MongoDB
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db
    db_uri = settings['mongodb.url']
    MongoDB = pymongo.Connection
    if 'pyramid_debugtoolbar' in set(settings.values()):
        class MongoDB(pymongo.Connection):
            def __html__(self):
                return 'MongoDB: <b>{}></b>'.format(self)
    conn = MongoDB(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
    config.scan('wf_blog')
    return config.make_wsgi_app()
