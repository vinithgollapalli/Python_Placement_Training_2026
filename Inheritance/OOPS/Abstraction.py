from abc import ABC, abstractmethod
class Bike(ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def acc(self):
        pass
class Bullet(Bike):
    def engine(self):
        print("It has 1000cc of Engine")
    def acc(self):
        print("It can pickup in 1.2 sec")
gt=Bullet()
gt.engine()