import datetime
import os


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
    os.environ.get('SQLALCHEMY_DATABASE_URI', 'realty.db'))
db = SQLAlchemy(app)


class Advert(db.Model):

    __tablename__ = 'realty_advertisments'
    advert_id          = db.Column(db.Integer, primary_key=True)
    settlement         = db.Column(db.String(50))
    under_construction = db.Column(db.Boolean)
    description        = db.Column(db.Text(1500))
    price              = db.Column(db.Integer)
    oblast_district    = db.Column(db.String(50))
    living_area        = db.Column(db.Float, nullable=True)
    has_balcony        = db.Column(db.Boolean)
    address            = db.Column(db.String(50))
    construction_year  = db.Column(db.Integer, nullable=True)
    rooms_number       = db.Column(db.Integer)
    premise_area       = db.Column(db.Float)
    active             = db.Column(db.Boolean, default=True)

    def __init__(self, settlement, under_construction, description, price,
                 oblast_district, living_area, has_balcony, address,
                 construction_year, rooms_number, premise_area, advert_id,
                 active,):
        self.settlement         = settlement
        self.under_construction = under_construction
        self.description        = description
        self.price              = price
        self.oblast_district    = oblast_district
        self.living_area        = living_area
        self.has_balcony        = has_balcony
        self.address            = address
        self.construction_year  = construction_year
        self.rooms_number       = rooms_number
        self.premise_area       = premise_area
        self.advert_id          = advert_id
        self.active             = active

    def __repr__(self):
        return '<Ad {advert_id}>'.format(advert_id=self.advert_id)


@app.route('/')
@app.route('/<int:page>')
def ads_list(page=1):
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
    if max_price:
        ads = ads.filter(Advert.price <= max_price)
    if max_price:
        ads = ads.filter(Advert.price >= min_price)
    return render_template(
        'ads_list.html',
        ads=ads.order_by(Advert.price.asc()).paginate(page, 15),
        oblast_district=oblast_district,
        new_building=new_building,
        min_price=min_price,
        max_price=max_price,
    )


if __name__ == "__main__":
    app.run()
