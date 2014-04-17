# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.response import Response
from pyramid.security import remember, forget

from wf_blog.views.admin.user_admin import UserAdmin
from wf_blog.resources import Root
from wf_blog.helper import login_required
from wf_blog.model import Post

class HomeView(Root):
    @view_config(renderer='index.html', route_name='index')
    def index(self):
        return {}




class AdminView(Root):
    @view_config(context='pyramid.httpexceptions.HTTPForbidden', renderer='/admin/login.html', route_name='login')
    @view_config(renderer='/admin/login.html', route_name='login', permission='view')
    def login(self):
        if self.request.method == 'POST':
            username = self.request.POST['username']
            password = self.request.POST['password']
            admin_user = UserAdmin(username, self.request)

            if admin_user.validate_user(password):
                headers = remember(self.request, username)
                return HTTPFound('/', headers=headers)
            else:
                headers = forget(self.request)
                message = u"用户名或密码错误"
                return {'message': message}
        return {}


    @view_config(renderer='/admin/all_posts.html', route_name='all_posts', permission='admin')
    def all_posts(self):
        results = list(Post.get_all_posts(self.request.mongodb))
        return {'results': results}
        




