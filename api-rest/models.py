from app import db


class AirQuality(db.Model):
    __tablename__ = 'air_quality_measurements'

    time_instant = db.Column(db.DateTime)
    # Not really PRIMARY_KEY but needed for SQLAlchemy
    id_entity = db.Column(db.String(50), primary_key=True)
    so2 = db.Column(db.Float)
    no2 = db.Column(db.Float)
    co = db.Column(db.Float)
    o3 = db.Column(db.Float)
    pm10 = db.Column(db.Float)
    pm2_5 = db.Column(db.Float)

    def __repr__(self):
        return '< {}, {}, {}, {}, {}, {}, {}, {} >'.format(
            self.time_instant,
            self.id_entity,
            self.so2,
            self.no2,
            self.co,
            self.o3,
            self.pm10,
            self.pm2_5
        )

    def to_dict(self):
        return vars(self)
