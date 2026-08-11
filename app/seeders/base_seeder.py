from sqlalchemy.orm import Session


class BaseSeeder:
    def __init__(self, session: Session):
        self.session = session

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def add(self, entity):
        self.session.add(entity)