import sys
sys.path.append('/Users/mac/PycharmProjects/SQLAlchemyProject')

from sqlalchemy import Column, String, Date, Integer, Numeric
from common.base import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(Date)
    height = Column(Integer)
    weight = Column(Numeric)

    def __init__(self, name, date_of_birth, height, weight):
        self.name = name
        self.date_of_birth = date_of_birth
        self.height = height
        self.weight = weight

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



