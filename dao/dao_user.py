import sys
sys.path.append('/Users/mac/PycharmProjects/SQLAlchemyProject')
from common.base import session_factory
from models.person import Person
from models.user import User
from models.mobile import Mobile
from datetime import date


def populate_database():
    session = session_factory()

    bruno = User("Bruno Krebs")
    john = User("John Doe")

    brunos_mobile = Mobile("android", "99991111", bruno)
    johns_mobile = Mobile("iphone", "55554444", john)

    session.add(brunos_mobile)
    session.add(johns_mobile)

    session.commit()
    session.close()
