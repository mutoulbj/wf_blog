from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPForbidden
from pyramid.response import Response

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
        if self.request.method == 'POST':
            username = self.request.POST['username']
            password = self.request.POST['password']
            admin_user = UserAdmin(username, request)

            if admin_user.validate(password):
                return HTTPFound('/') # TODO: 跳转到管理界面
        message = u"用户名或密码错误"
        return {'message': message, }
