from functools import wraps
from flask import redirect, url_for, request
from flask import session as login_session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect(url_for('authController.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function