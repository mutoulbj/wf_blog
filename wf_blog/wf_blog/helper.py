# -*- coding: utf-8 -*-
from hashlib import md5
from pyramid.httpexceptions import HTTPFound

def encrypt(s):
    m = md5(s)
    m.update(s)
    return m.hexdigest()

def login_required(view_callable):
	def inner(context, request):
		if request.user is None:
			url = '/admin/login?next=%s' % request.url
			return HTTPFound(location=url)
		else:
			return view_callable(context, request)

	return inner
