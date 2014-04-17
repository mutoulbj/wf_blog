# -*- coding: utf-8 -*-
from pyramid.security import Allow, Everyone, Authenticated
from wf_blog.model import User

def groupfinder(uid, request):
	cur = User.get_user(request.mongodb, uid)
	if cur:
		return cur.get('group', [])
	return []