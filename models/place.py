#!/usr/bin/python3
"""Place module for hbnb project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.review import Review
from os import getenv
from models.amenity import Amenity

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship(
        'Review',
        backref=backref('place', cascade='all, delete-orphan'),
        cascade='all, delete-orphan')
    amenities = relationship(
        'Amenity', secondary='place_amenity', viewonly=False,
        back_populates='place_amenities')

    # For FileStorage
    @property
    def reviews(self):
        """Getter attribute to retrieve reviews linked to this
        place for FileStorage"""
        from models import storage
        return [review for review in storage.all(Review).values()
                if review.place_id == self.id]

    @property
    def amenities(self):
        """ Returns list of amenity ids """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj=None):
        """ Appends amenity ids to the attribute """
        if type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
