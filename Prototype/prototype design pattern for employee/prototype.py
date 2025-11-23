from abc import abstractmethod


class Prototype:
    @abstractmethod
    def getClone(self):
        pass