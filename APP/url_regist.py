from Area.urls import area
from Bank.urls import bank
from Company.urls import company
from Guarantee.urls import guarantee
from Labor.urls import labor
from Project.urls import project
from User.urls import user
from UserTemplate.urls import user_template


def blue_regist(app):
    app.register_blueprint(user, url_prefix='/user/')
    app.register_blueprint(area, url_prefix='/area/')
    app.register_blueprint(company, url_prefix='/company/')
    app.register_blueprint(project, url_prefix='/project/')
    app.register_blueprint(labor, url_prefix='/labor/')
    app.register_blueprint(guarantee, url_prefix='/guarantee/')
    app.register_blueprint(bank, url_prefix='/bank/')
    app.register_blueprint(user_template, url_prefix='/template/')
