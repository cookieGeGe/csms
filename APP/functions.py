from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


def get_db_uri(DATABASE):
    user = DATABASE.get('USER')
    passwd = DATABASE['PASSWORD']
    host = DATABASE['HOST']
    port = DATABASE['PORT']
    name = DATABASE['NAME']
    db = DATABASE['DB']
    driver = DATABASE['DRIVER']

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver,
                                           user, passwd,
                                           host, port,
                                           name)


db = SQLAlchemy()
sess = Session()


def init_ext(app):
    db.init_app(app)
    sess.init_app(app)
