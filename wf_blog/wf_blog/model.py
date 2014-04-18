# -*- coding: utf-8 -*-
import logging
import pymongo
from bson import ObjectId
from datetime import datetime
from pyramid.security import Allow, Everyone, Authenticated
from wf_blog.mongodb import safe_mongocall
from wf_blog.helper import encrypt

class User(object):
    """
    用户
    """
    @staticmethod
    @safe_mongocall
    def add_user(mongodb, username, password):
        user = {
        'username': username,
        'password': encrypt(password)
        }
        mongodb['user'].insert(user)

    def change_password(mongodb, id, password):
        mongodb['user'].update(
        {'_id': id},
        {'$set': {'password': encrypt(password)}}
        )

    @staticmethod
    @safe_mongocall
    def get_user(mongodb, username):
        return mongodb['user_user'].find_one({'username': username})

class Post(object):
    """
    博文
    """
    @staticmethod
    @safe_mongocall
    def add_post(mongodb, title, content, category, add_time=None, add_user=None):
        post = {
        'title': title,
        'content': content,
        'category': category,
        # 'image_url': image_url,
        'add_time': datetime.now(),
        'add_user': 'wf'
        }
        mongodb['post'].insert(post)


    @staticmethod
    @safe_mongocall
    def update_post(mongodb, id, title, content, category):
        mongodb['post'].update(
        {'_id': ObjectId(id)},
        {'$set': {'title': title, 'content': content, 'category': category, }}
        )


    @staticmethod
    @safe_mongocall
    def del_post(mongodb, id):
        mongodb['post'].remove({'_id': ObjectId(id)})


    @staticmethod
    @safe_mongocall
    def get_post(mongodb, id):
        return mongodb['post'].find_one({'_id': ObjectId(id)})

    @staticmethod
    @safe_mongocall
    def get_all_posts(mongodb):
        return mongodb['post'].find()  # TODO: 加排序

        
class RootFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'admin')
    ]

    def __init__(self, request):
        pass
