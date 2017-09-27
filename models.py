from flask_sqlalchemy import SQLAlchemy


from extensions import db


class Advert(db.Model):

    __tablename__ = 'realty_advertisments'
    advert_id          = db.Column(db.Integer, primary_key=True, index=True)
    settlement         = db.Column(db.String(50))
    under_construction = db.Column(db.Boolean)
    description        = db.Column(db.Text(1500))
    price              = db.Column(db.Integer)
    oblast_district    = db.Column(db.String(50), index=True)
    living_area        = db.Column(db.Float, nullable=True)
    has_balcony        = db.Column(db.Boolean)
    address            = db.Column(db.String(50))
    construction_year  = db.Column(db.Integer, nullable=True)
    rooms_number       = db.Column(db.Integer)
    premise_area       = db.Column(db.Float)
    active             = db.Column(db.Boolean, default=True)

    def __init__(self, active=True, **kwargs):
        db.Model.__init__(self, active=active, **kwargs)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
            for attr, value in kwargs.items():
                setattr(self, attr, value)
            return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    @classmethod
    def get_by_id(cls, record_id):
        if ispositive_int(record_id):
            return cls.query.get(int(record_id))
        return None

    def __repr__(self):
        return '<Ad {advert_id}>'.format(advert_id=self.advert_id)


def ispositive_int(data):
    return any(
            (isinstance(data, (str, bytes)) and data.isdigit(),
             isinstance(data, (int, float)))
    )
