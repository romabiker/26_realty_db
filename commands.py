import json
import requests


import click


from models import Advert
from extensions import db
import application


def get_remote_ads_json(url):
    response = requests.get(url)
    if not response.ok:
        response.raise_for_status()
    return json.loads(response.text)


def get_local_ads_json(path):
    with open(path, 'r') as file_handler:
        return json.load(file_handler)


def make_id_set(ads):
    return {ad.get('id') for ad in ads}


def set_not_active_ads(ads):
    incoming_ads_ides = make_id_set(ads)
    ads_active_in_db = Advert.query.filter(Advert.active == True)
    for ad in ads_active_in_db:
        if not ad.advert_id in incoming_ads_ides:
            ad.update(active=False)


def create_or_update(ads):
    for ad in ads:
        ad_obj = Advert.get_by_id(ad.get('id'))
        if ad_obj:
            ad_obj.update(ad)
        else:
            Advert.create(
                settlement         = ad.get('settlement'),
                under_construction = ad.get('under_construction'),
                description        = ad.get('description'),
                price              = ad.get('price'),
                oblast_district    = ad.get('oblast_district'),
                living_area        = ad.get('living_area'),
                has_balcony        = ad.get('has_balcony'),
                address            = ad.get('address'),
                construction_year  = ad.get('construction_year'),
                rooms_number       = ad.get('rooms_number'),
                premise_area       = ad.get('premise_area'),
                advert_id          = ad.get('id'),
            )


def upload_to_db(ads):
    set_not_active_ads(ads)
    create_or_update(ads)


@click.command()
def create():
    with application.create_app().app_context():
        db.create_all()
        click.echo('created {db}'.format(db=db.get_binds()))


@click.command()
def drop():
    with application.create_app().app_context():
        db.drop_all()
        click.echo('table was dropped')


@click.command()
@click.option(
    '-u', '--url',
    help='url to ads in json')
@click.option(
    '-p', '--path',  type=click.Path(exists=True),
    help='path to ads in json')
def feed(url, path):
    with application.create_app().app_context():
        if url:
            ads = get_remote_ads_json(url)
            click.echo('from url got {count} ads'.format(count=len(ads)))
            upload_to_db(ads)
        if path:
            ads = get_local_ads_json(path)
            click.echo('from path got {count} ads'.format(count=len(ads)))
            upload_to_db(ads)
