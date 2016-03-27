# -*- coding: utf-8 -*-
import os
from flask import Flask

from .config import config

app = Flask(__name__)

with app.app_context():
    config_name = os.getenv('FLASK_CONFIG') or 'development'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

from views import *
