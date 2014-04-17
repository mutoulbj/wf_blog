from pyramid.security import Allow
from pyramid.security import Everyone, Authenticated

class Root(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, Authenticated, 'admin'),
                ]

    def __init__(self, request):
        self.request = request