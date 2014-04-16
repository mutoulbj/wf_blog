# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.response import Response
from pyramid.security import remember, forget

from wf_blog.views.admin.user_admin import UserAdmin
from wf_blog.resources import Root

class HomeView(Root):
    @view_config(renderer='index.html', route_name='index')
    def index(self):
        return {}


class PostView(Root):
    @view_config(renderer='/posts/detail.html', route_name='post_detail')
    def post_detail(self):
        return {}


class AdminView(Root):
    @view_config(context='pyramid.httpexceptions.HTTPForbidden', renderer='/admin/login.html', route_name='login')
    @view_config(renderer='/admin/login.html', route_name='login')
    def login(self):
        return {}

    @view_config(renderer='json', route_name='login_post')
    def login_post(self):
        if self.request.method == 'POST':
            username = self.request.POST['username']
            password = self.request.POST['password']
            admin_user = UserAdmin(username, self.request)

            if admin_user.validate_user(password):
                headers = remember(self.request, username)
                return {'success': 'true'}
            else:
                headers = forget(self.request)
        message = u"用户名或密码错误"
        return {'success': message, }

    @view_config(renderer='/admin/dashboard.html', route_name='dashboard', permission='admin')
    def dashboard(self):
        return {}

    @view_config(renderer='/admin/new_post.html', route_name='new_post')
    def new_post(self):
        return {}



