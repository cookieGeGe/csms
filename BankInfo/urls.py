from flask import Blueprint
from . import views

bankinfo = Blueprint('bankinfo', __name__)

bankinfo.add_url_rule('/add', methods=['post'], view_func=views.AddUpdateBankInfo.as_view('add_update_bankinfo'))
bankinfo.add_url_rule('/query', methods=['get'], view_func=views.QueryBankInfo.as_view('query_bankinfo'))
bankinfo.add_url_rule('/delete', methods=['delete'], view_func=views.DeleteBankInfo.as_view('delete_bankinfo'))
