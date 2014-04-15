from pyramid.security import Authenticated
from pyramid.security import Allow


class Root(object):
    def __init__(self, context, request, ):
        self.request = request
        self.contect = context
        if hasattr(self.request, 'mongodb'):
            self.mongodb = self.request.mongodb
    def __call__(self):
        return {'context': self.context, 'request': self.request}

    def __getitem__(self):
        if key == 'my_admin':
            return Admin()
        # elif key == 'post':
        #     return Post()
        # elif key == 'category':
        #     return Catrgory()
        # elif key == 'tags':
        #     return Tags()
        return KeyError
