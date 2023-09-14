import sys
sys.path.append('/Users/mac/PycharmProjects/SQLAlchemyProject')
from models.person import Person
from dao.dao_person import create_people_sample
from dao.dao_person import insert_person
from dao.dao_person import insert_bulk_people
from dao.dao_person import get_all_people
from datetime import date
from dao.dao_user import populate_database

if __name__ == "__main__":
    # people = get_all_people()
    # if len(people) == 0:
    #     create_people_sample()
    # people = get_all_people()
    #
    # lst_people = []
    #
    # for person in people:
    #     lst_people.append({
    #         'name': person.name,
    #         'date_of_birth': person.date_of_birth,
    #         'height': person.height,
    #         'weight': person.weight
    #     })
    #     print(person.name + " was born in " + str(person.date_of_birth))
    #
    # print(lst_people)
    #
    # insert_person(Person("Khoa", date(1992, 12, 12), 170, 84.5))
    # insert_bulk_people(lst_people)

    populate_database()