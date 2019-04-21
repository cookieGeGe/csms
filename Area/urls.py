from flask import Blueprint

from Area.views import get_province,get_city,get_district

area = Blueprint('area', __name__)

area.add_url_rule('/province/<int:ID>', methods=['GET', ], view_func=get_province)
area.add_url_rule('/city/<int:ID>', methods=['GET', ], view_func=get_city)
area.add_url_rule('/district/<int:ID>', methods=['GET', ], view_func=get_district)

