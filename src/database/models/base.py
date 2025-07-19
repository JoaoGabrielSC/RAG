from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    raise NotImplementedError(
        "This is an abstract base class and should not be instantiated directly."
    )
