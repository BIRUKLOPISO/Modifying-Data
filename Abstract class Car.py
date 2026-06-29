from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model: str, year: int):
        self.model = model
        self.year = year

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Toyota(Car):
    def drive(self):
        print("Here is the car.")

    def stop(self):
        print(f"{self.model} is Stopping.")

    def latest(self):
        return f"The {self.year} is the recent one."


class Ranger(Car):
    def drive(self):
        print("Here is the car.")

    def stop(self):
        print(f"{self.model} is Stopping.")

    def latest(self):
        return f"{self.year} is the recent model."


car1 = Toyota("Model1", 2027)
car2 = Ranger("Model2", 2028)
print("===Toyota===")
car1.drive()
car1.stop()
print(car1.latest())
print("===Ranger===")
car2.stop()
car2.drive()
print(car2.latest())

