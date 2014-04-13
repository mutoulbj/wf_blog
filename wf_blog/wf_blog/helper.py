# -*- coding: utf-8 -*-
from hashlib import md5

def encrypt(s):
    m = md5(s)
    m.update(s)
    return m.hexdigest()
