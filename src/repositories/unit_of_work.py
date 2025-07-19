from sqlalchemy.orm import Session

from src.repositories.base_unit_of_work import UnitOfWork


class UnitOfWorkImpl(UnitOfWork):

    def __init__(self, session: Session, repo: UnitOfWork):
        self.session: Session = session
        self.repository: UnitOfWork = repo

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
