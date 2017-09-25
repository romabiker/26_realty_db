import click
import json
import requests


from server import db, Advert


def get_ads_json(url):
    response = requests.get(url)
    if not response.ok:
        response.raise_for_status()
    return response.text


def load_into_db(ads):
    for ad in ads:
        ad_obj = Advert(
            ad.get('settlement'),
            ad.get('under_construction'),
            ad.get('description'),
            ad.get('price'),
            ad.get('oblast_district'),
            ad.get('living_area'),
            ad.get('has_balcony'),
            ad.get('address'),
            ad.get('construction_year'),
            ad.get('rooms_number'),
            ad.get('premise_area'),
            ad.get('id'),
            True,)
        db.session.add(ad_obj)
        db.session.commit()


@click.command()
def create():
    db.create_all()


@click.command()
def drop():
    db.drop_all()


@click.command()
@click.option('-u', '--url',
              default='https://devman.org/media/filer_public/e5/62/e56287d2-9519-4e18-878a-6d4849b628e2/ads.json',
              help='url to ads in json')
def main(url, create, drop):
    ads = json.loads(get_ads_json(url))
    load_into_db(ads)
    ads_objs = Advert.query.all()


if __name__ == '__main__':
    main()
