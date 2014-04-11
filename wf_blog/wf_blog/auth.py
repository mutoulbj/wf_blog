# -*-coding:utf-8-*-
from pyramid.security import (Everyone, Authenticated, Allow, Deny, ALL_PERMISSIONS)

def auth(user_id, request):
    user = request.mongodb['user_user'].find_one({'uid': user_id})
    if user:
        if user.username == 'wf':
            return ['auth.admin', ]
        else:
            return [Authenticated]
    else:
        return [Everyone]
