from abc import ABC, abstractmethod


class UnitOfWork(ABC):
    """
    Abstract base class for Unit of Work pattern.
    This class defines the interface for managing transactions and repositories.
    It should be implemented by concrete classes that handle specific database operations.
    """

    @property
    @abstractmethod
    def session(self):
        """Returns the current session."""

    @property
    @abstractmethod
    def repository(self):
        """Returns the current repository."""

    @abstractmethod
    def begin(self):
        """Initialize a transaction."""

    @abstractmethod
    def commit(self):
        """Confirm the transaction."""

    @abstractmethod
    def rollback(self):
        """Revert the transaction."""
