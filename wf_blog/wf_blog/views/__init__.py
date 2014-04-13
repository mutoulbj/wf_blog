from pyramid.view import view_config

class Root(object):
    def __init__(self, request, context):
        self.request = request
        self.contect = context

    def __call__(self):
        return {'context': self.context}
