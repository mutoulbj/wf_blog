# -*- coding: utf-8 -*-
from wf_blog.security import PostFactory

def includeme(config):
    config.add_route('index', '')
    config.include(admin_include, '/admin')
    config.include(post_include, '/post')


def admin_include(config):
    config.add_route('index', '')
    config.add_route('login', '/login')
    config.add_route('login_post', '/login/post')
    config.add_route('logout', '/logout')


def post_include(config):
    config.add_route('post_detail', '/detail')
    config.add_route('post_action', '/add/{action}', factory='wf_blog.security.PostFactory')
