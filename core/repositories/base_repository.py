from abc import ABC, abstractmethod

class BaseRepository(ABC):
    def __init__(self, collection):
        self.collection = collection

    @abstractmethod
    def insert(self, document):
        pass

    @abstractmethod
    def find_by_id(self, _id):
        pass
