# -*- coding: utf-8 -*-

def includeme(config):
    config.add_route('index', '')
    config.include(admin_include, '/admin')
    config.include(post_include, '/post')


def admin_include(config):
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('all_posts', '/all_posts')
    


def post_include(config):
    config.add_route('new_post', '/new_post')
    config.add_route('post_detail', '/detail/{id}')
    config.add_route('post_edit', '/edit/{id}')
    config.add_route('post_delete', '/delete/{id}')
