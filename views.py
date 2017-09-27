import datetime


from flask import Blueprint, render_template, request


from models import Advert, ispositive_int
from extensions import db


blueprint = Blueprint('dashboard', __name__, static_folder='../static')


@blueprint.route('/')
@blueprint.route('/<int:page>')
def ads_list(page=1, ads_per_page=15):
    oblast_district = request.args.get('oblast_district')
    new_building =  request.args.get('new_building')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    ads = Advert.query.filter(Advert.active == True)
    if oblast_district:
        ads = ads.filter(Advert.oblast_district == oblast_district)
    if new_building:
        ads = ads.filter(
            db.or_(Advert.under_construction == True,
                   Advert.construction_year >= datetime.date.today().year - 2))
    if ispositive_int(max_price):
        ads = ads.filter(Advert.price <= int(max_price))
    if ispositive_int(min_price):
        ads = ads.filter(Advert.price >= int(min_price))
    return render_template(
        'ads_list.html',
        ads=ads.order_by(Advert.price.asc()).paginate(page, ads_per_page),
        oblast_district=oblast_district,
        new_building=new_building,
        min_price=min_price,
        max_price=max_price,
    )
