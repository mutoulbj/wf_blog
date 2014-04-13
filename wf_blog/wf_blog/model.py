# -*- coding: utf-8 -*-
import logging
import pymongo
from bson import ObjectId
from datetime import datetime
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


class Post(object):
    """
    博文
    """
    @staticmethod
    @safe_mongocall
    def add_post(mongodb, title, content, category, image_url, add_time, add_user):
        post = {
        'title': title,
        'content': content,
        'category': category,
        'image_url': image_url,
        'add_time': datetime.now(),
        'add_user': 'wf'
        }
        mongodb['post'].insert(post)


    @staticmethod
    @safe_mongocall
    def update_post(mongodb, id, title, content, category, image_url):
        mongodb['post'].update(
        {'_id': ObjectId(id)},
        {'$set': {'title': title, 'content': content, 'category': category, 'image_url': inage_url}}
        )


    @staticmethod
    @safe_mongocall
    def del_post(mongodb, id):
        mongodb['post'].remove({'_id': ObjectId(id)})


    @staticmethod
    @safe_mongocall
    def get_post(mongodb, id):
        return mongodb['post'].find_one({'_id': ObjectId(id)})
