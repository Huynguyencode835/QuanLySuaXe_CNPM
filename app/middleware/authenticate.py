from functools import wraps

from flask_login import current_user
from flask import redirect, url_for, abort


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            #chưa đăng nhập => về login
            if not current_user.is_authenticated:
                return abort(404)
            #sai quyền
            if current_user.role not in roles:
                return abort(403)

            return f(*args, **kwargs)
        return wrapper
    return decorator

