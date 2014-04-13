# -*- coding: utf-8 -*-

def includeme(config):
    config.add_route('index', '')
    config.include(admin_include, '/admin')
    config.include(post_include, '/post')


def admin_include(config):
    config.add_route('index', '')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')


def post_include(config):
    config.add_route('post_detail', '/detail')
    config.add_route('post_add', '/add')
    config.add_route('post_edit', '/edit')
    config.add_route('post_delete', '/delete')
