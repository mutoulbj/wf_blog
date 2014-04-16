# -*- coding: utf-8 -*-
from wf_blog.security import PostFactory

def includeme(config):
    config.add_route('index', '')
    config.include(admin_include, '/admin')
    config.include(post_include, '/post')


def admin_include(config):
    config.add_route('login', '/login', factory='wf_blog.security.PostFactory')
    config.add_route('login_post', '/login/post', factory='wf_blog.security.PostFactory')
    config.add_route('logout', '/logout')
    config.add_route('dashboard', '/dashboard')
    config.add_route('new_post', '/new_post')


def post_include(config):
    config.add_route('post_detail', '/detail')
    config.add_route('post_action', '/add/{action}', factory='wf_blog.security.PostFactory')
