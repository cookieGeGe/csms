from User.urls import user


def blue_regist(app):
    app.register_blueprint(user, url_prefix='/userinfo')
