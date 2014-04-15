# -*- coding: utf-8 -*-
from pyramid.security import Allow, Everyone, Authenticated

class PostFactory(object):
    __acl__ =[
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'add'),
        (Allow, Authenticated, 'edit')
    ]

    def __init__(self):
        pass
