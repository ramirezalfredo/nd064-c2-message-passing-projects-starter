import logging
from .config import SQLALCHEMY_DATABASE_URI
from .models import Location
from datetime import datetime, timedelta
import json
from typing import Dict
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, BigInteger
from sqlalchemy.orm import sessionmaker
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("connections-api")

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        # validation_results: Dict = LocationSchema().validate(location)
        # if validation_results:
        #     logger.warning(f"Unexpected data format in payload: {validation_results}")
        #     raise Exception(f"Invalid payload: {validation_results}")
        
        json_location = json.loads(location)
        new_location = Location()
        new_location.person_id = json_location['person_id']
        new_location.coordinate = ST_Point(json_location['latitude'], json_location['longitude'])
        new_location.creation_time = json_location['created_at']
        session.add(new_location)
        session.commit()

        return new_location
