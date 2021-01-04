from sqlalchemy import Column, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AirQuality(Base):
    """
    Class to represent the air_quality_measurements in the Postgres database
    """
    __tablename__ = 'air_quality_measurements'

    # We should define a composed Primary Key as AlchemySQL will create a object for each primary key.
    time_instant = Column(DateTime, primary_key=True)
    id_entity = Column(String(50), primary_key=True)
    so2 = Column(Float)
    no2 = Column(Float)
    co = Column(Float)
    o3 = Column(Float)
    pm10 = Column(Float)
    pm2_5 = Column(Float)

    def __init__(self, id_entity=None, so2=None, no2=None, co=None, o3=None, pm10=None, pm2_5=None):
        self.id_entity = id_entity
        self.so2 = so2
        self.no2 = no2
        self.co = co
        self.o3 = o3
        self.pm10 = pm10
        self.pm2_5 = pm2_5

    def __repr__(self):
        return '<Measure(time_instant={}, id_entity={}, so2={}, no2={}, co={}, o3={}, pm10={}, pm2_5={}>'\
            .format(
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
        """
        Return the object with a serializable JSON
        """
        return {
            'time_instant': self.time_instant.strftime('%Y-%m-%d %H:%M:%S'),
            'id_entity': self.id_entity,
            'so2': self.so2,
            'no2': self.no2,
            'co': self.co,
            'o3': self.o3,
            'pm10': self.pm10,
            'pm2_5': self.pm2_5
        }
