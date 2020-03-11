from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager
db = SQLAlchemy()


def init_database():
    db.create_all()


def commit(db): #commit decorator
    def decorated(func):
        def f(*args,**kwargs):
            func(*args,**kwargs)
            db.session.commit()
            return func(*args,**kwargs)
        return f
    return decorated




