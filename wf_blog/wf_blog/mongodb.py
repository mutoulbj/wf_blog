# -*- coding:utf-8
import logging
import time
import pymongo
from pymongo.errors import AutoReconnect

def init_mongodb(config, settings):
    if 'mongodb.use' in settings and settings['mongodb_use'] == 'true':
        conn = pymongo.Connection(settings['mongodb.uri'])
        config.registry.settings['!mongodb.conn'] == conn
        config.add_subscriber(add_mongodb, 'pyramid.event.NewRequest')

def add_mongodb(event):
    settings = event.request.registry.settings
    db = settings['!mongodb.conn'][settings['mongodb.name']]
    db.authenticate(settings['mongodb.user'], settings['mongodb.passwd'])
    event.request.mongodb = db

def safe_mongocall(call):
    def _safe_mongocall(*args, **kwargs):
        for i in xrange(5):
            try:
                return call(*args, **kwargs)
            except AutoReconnect:
                time.sleep(pow(2, i))
            log.debug('Error: Failed operation!AutoReconnect Exception')
    return _safe_mongocall
