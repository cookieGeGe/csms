from flask import Blueprint

from Index.views import GetBadRecordInfo, MessageTotal

index = Blueprint('index', __name__)

index.add_url_rule('/info', methods=['get',], view_func=GetBadRecordInfo.as_view('index_info_all'))
index.add_url_rule('/number', methods=['get',], view_func=MessageTotal.as_view('index_info_number'))
