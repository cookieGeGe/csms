from Area.urls import area
from Company.urls import company
from User.urls import user


def blue_regist(app):
    app.register_blueprint(user, url_prefix='/userinfo')
    app.register_blueprint(area, url_prefix='/area')
    app.register_blueprint(company, url_prefix='company')
