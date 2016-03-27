# -*- coding: utf-8 -*-
import requests
import json
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import redirect
from flask import url_for

from app import app


@app.route('/user/login', methods=['GET', 'POST'])
def login():

    url = app.config['BASE_URL'] + '/users/login'

    if request.method == "POST":
        email_or_username = request.form['username']
        password = request.form['password']
        data = {
            'email_or_username': email_or_username,
            'password': password
        }
        r = json.loads(requests.post(url, data)._content)
        if r['code'] == 200:
            session['token'] = r['data']['token']
            return redirect(url_for('index'))
        else:
            if type(r['errors']) is dict:
                flash(r['errors'][r['errors'].keys()[0]][0])
            else:
                flash(r['errors'])

    return render_template('auth/login.html')
