# -*- coding: utf-8 -*-
from pyramid.security import (Everyone, Authenticated, Allow, Deny, ALL_PERMISSIONS)

from wf_blog.helper import encrypt
from wf_blog.model import User

class UserAdmin(object):
    def __init__(self, username, request):
        self.settings = request.registry.settings
        self.__get_stored_encrypt(username, request)

    def __get_stored_encrypt(self, username, request):
        record = User.get_user(request.mongodb, username)
        if record:
            self.stored_encrypt = record['password']
        else:
            self.stored_encrypt = None

    def validate_user(self, password):
        """验证用户"""
        if self.stored_encrypt:
            if self.stored_encrypt == encrypt(password):
                return True
        return False
