from flask import Blueprint

from Bank.views import CreateBank, QueryBank, QueryOneBank, AddBankReceipt

bank = Blueprint('bank', __name__)

# 创建银行管理
bank.add_url_rule('/create', methods=['POST', ], view_func=CreateBank.as_view('create_bank'))
# 银行列表查询
bank.add_url_rule('/query', methods=['GET', ], view_func=QueryBank.as_view('query_bank'))
# 查询单个银行信息
bank.add_url_rule('/info', methods=['GET', ], view_func=QueryOneBank.as_view('info_bank'))
# 添加银行回单
bank.add_url_rule('/receipt', methods=['post', ], view_func=AddBankReceipt.as_view('add_bank_receipt'))
