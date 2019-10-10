from Area.urls import area
from Attend.urls import attend
from Bank.urls import bank
from BankInfo.urls import bankinfo
from Company.urls import company
from Guarantee.urls import guarantee
from Index.urls import index
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
    app.register_blueprint(attend, url_prefix='/attend/')
    app.register_blueprint(index, url_prefix='/index/')
    app.register_blueprint(bankinfo, url_prefix='/bankinfo/')
