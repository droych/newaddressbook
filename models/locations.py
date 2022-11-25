from sqlalchemy import Table,Column,String,Integer,Float

from config.db import meta,Base


class Location(Base):
    __tablename__ = "Locations"
    id = Column('id',Integer,primary_key = True, index=True)
    name = Column('name',String(255), nullable=True)
    latitude = Column('latitude',Float, nullable=True)
    longitude = Column('longitude',Float, nullable=True)
    Address = Column('Address',String(255), nullable=True)

 
