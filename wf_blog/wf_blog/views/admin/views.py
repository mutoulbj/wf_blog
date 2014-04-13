from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.response import Response

from wf_blog.views import Root

class HomeView(Root):
    @view_config(renderer='index.html', route_name='index')
    def index(self):
        return {}


    @view_config(renderer='/admin/login.html', route_name='login')
    def login(self):
        return {}


class PostView(Root):
    @view_config(renderer='/posts/detail.html', route_name='post_detail')
    def post_detail(self):
        return {}
