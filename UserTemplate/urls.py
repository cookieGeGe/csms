from flask import Blueprint

from UserTemplate.views import CreateTemplate, QueryOneTemplate, QueryTemplate, DeleteTemplate

user_template = Blueprint('user_template', __name__)

user_template.add_url_rule('/create', methods=['post'], view_func=CreateTemplate.as_view('create_temp'))
user_template.add_url_rule('/query/one', methods=['get'], view_func=QueryOneTemplate.as_view('query_one_temp'))
user_template.add_url_rule('/delete', methods=['delete'], view_func=DeleteTemplate.as_view('delete_temp'))
user_template.add_url_rule('/query', methods=['get'], view_func=QueryTemplate.as_view('query_temp'))
