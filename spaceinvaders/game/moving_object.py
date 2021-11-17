from abc import ABC, abstractmethod

class MovingObject(ABC):

    @abstractmethod
    def draw_self(self):
        pass

    @abstractmethod
    def advance(self):
        pass

    