# -*- coding: utf-8 -*-
import json
import requests
from flask import render_template
from flask import request

from app import app


@app.route('/commodity')
def commodity():
    url = app.config['BASE_URL'] + '/get_commodity'
    reqs = requests.get(url).json()
    return render_template('commodity/commodity.html', reqs=reqs)
