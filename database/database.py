from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager
db = SQLAlchemy()


def init_database():
    db.create_all()


def commit(db): #commit decorator
    def decorated(func):
        def f(*args,**kwargs):
            ret = func(*args, **kwargs)
            db.session.commit()
            return ret
        return f
    return decorated




