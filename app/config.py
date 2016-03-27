# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')

    SECRET_KEY = 'you-will-never-guess'
    CSRF_ENABLED = True

    BASE_URL = 'http://lolcode.cn/v1'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}
