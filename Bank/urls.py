from flask import Blueprint

from Bank.views import CreateBank, QueryBank

bank = Blueprint('bank', __name__)

bank.add_url_rule('/create', methods=['POST', ], view_func=CreateBank.as_view('create_bank'))
bank.add_url_rule('/query', methods=['GET', ], view_func=QueryBank.as_view('query_bank'))
