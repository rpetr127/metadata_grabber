# -*- coding: utf-8 -*-
from os import path

class Config(object):
    DEBUG = False
    TESTING = False
    ROOT_DIR = path.abspath(
        path.dirname(path.join(__file__))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/test.db' % (ROOT_DIR)
    SECRET_KEY='\x62\x27\x5c\x78\x38\x35\x28\x5c\x78\x63\x33\x5c\x78\x64\x33\x66\x42\x5c\x78\x64\x61\x5c\x78\x30\x33\x36\x5c\x78\x66\x63\x32\x5c\x78\x39\x66\x5c\x78\x38\x64\x5c\x78\x65\x30\x5c\x5c\x62\x47\x5c\x78\x62\x38\x5c\x78\x65\x30\x5c\x78\x63\x36\x51\x5c\x74\x5c\x72\x41\x27'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/foo'
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_NATIVE_UNICODE = True
