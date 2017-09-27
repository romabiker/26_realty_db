# Real Estate Site

Realty dashboard: filter by new building, settlement, min and max prices, is active, pagination. Script loads advertisments from url in json into sqlite3.

Quickstart
----------


Run the following commands to install project locally:

```
    # to install dependancies:
    pipenv shell
    pipenv install


    #set the ``FLASK_APP`` and ``FLASK_DEBUG`` environment variables :
    export FLASK_DEBUG=1              # if debug
    export FLASK_APP=autoapp.py       # to use 'flask' shell commands


    # enter db path, default is realty.db
    export SQLALCHEMY_DATABASE_URI=path/to/realty.db


    # creates db and inits ads 'realty_advertisments' table
    flask create

    created {Table('realty_advertisments', MetaData(bind=None), Column('advert_id',
    Integer(), table=<realty_advertisments>, primary_key=True, nullable=False),
    Column('settlement', String(length=50), table=<realty_advertisments>),
    Column('under_construction', Boolean(), table=<realty_advertisments>),
    Column('description', Text(length=1500), table=<realty_advertisments>),
    Column('price', Integer(), table=<realty_advertisments>), Column('oblast_district',
    String(length=50), table=<realty_advertisments>), Column('living_area', Float(),
    table=<realty_advertisments>), Column('has_balcony', Boolean(),
    table=<realty_advertisments>), Column('address', String(length=50),
    table=<realty_advertisments>), Column('construction_year', Integer(),
    table=<realty_advertisments>), Column('rooms_number', Integer(),
    table=<realty_advertisments>), Column('premise_area', Float(),
    table=<realty_advertisments>), Column('active', Boolean(),
    table=<realty_advertisments>, default=ColumnDefault(True)),
    schema=None): Engine(sqlite:////home/path/to/devman/26_realty_db/realty.db)}


    # drops ads table
    flask drop


    # loads or updates ads from url  in text json format  into 'realty_advertisments' table of the database
    flask feed --url https://some/url/ads.json
    flask feed --path path/to/ads.json

    $ flask  feed -p ads.json
    from path got 4 ads


    # run server and open http://127.0.0.1:5000/ page in browser
    flask run

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
