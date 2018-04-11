import random
import string
from flask import session as login_session
from flask import request, abort
from functools import wraps


def generate_csrf_token():
    if '_csrf_token' not in login_session:
        login_session['_csrf_token'] = ''.join(random.choice(
            string.ascii_lowercase + string.digits) for x in range(32))
    return login_session['_csrf_token']

def generate_login_token():
    if 'login_token' not in login_session:
        login_session['login_token'] = ''.join(random.choice(
            string.ascii_lowercase + string.digits) for x in range(32))
    return login_session['login_token']

def csrf_protect(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            token = login_session.pop('_csrf_token', None)
            if not token or token != request.form.get('_csrf_token'):
                return abort(403)
        return f(*args, **kwargs)
    return decorated_function