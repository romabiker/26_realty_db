# Real Estate Site

Realty dashboard: filter by new building, settlement, min and max prices, is active, pagination. Script loads advertisments from url in json into sqlite3.

Quickstart
----------


Run the following commands to install project locally:

```
    pipenv shell
    pipenv install
    export FLASK_DEBUG=1              # if debug
    export SQLALCHEMY_DATABASE_URI=   # enter db path, default is realty.db
    python ads_loader.py create       # creates db and inits ads table
    python ads_loader.py drop         # drops ads table
    python ads_loader.py              # loads ads in json format from url into table
    python server.py                  # open page in browser http://127.0.0.1:5000/

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
