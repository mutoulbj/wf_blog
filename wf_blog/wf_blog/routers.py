# -*- coding: utf-8 -*-

def includeme(config):
    config.include(home_include, '')
    config.include(admin_include, '/admin')

def home_include(config):
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

def admin_include(config):
    pass
