import sys
sys.path.append('/Users/mac/PycharmProjects/SQLAlchemyProject')
from common.base import session_factory
from models.person import Person
from datetime import date


def create_people_sample():
    session = session_factory()
    bruno = Person("Bruno Krebs", date(1984, 10, 20), 182, 84.5)
    john = Person("John Doe", date(1990, 5, 17), 173, 90)
    session.add(bruno)
    session.add(john)
    session.commit()
    session.close()


def get_all_people():
    session = session_factory()
    people_query = session.query(Person)
    session.close()
    return people_query.all()


def insert_person(person):
    session = session_factory()
    session.add(person)
    session.commit()
    session.close()


def insert_bulk_people(all_people):
    session = session_factory()
    session.bulk_insert_mappings(Person, all_people)
    session.commit()
    session.close()