class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, make, model, horsepower, size):
        self.engine = Engine(horsepower)
        self.wheels = [Wheel(size) for _ in range(4)]
        self.make = make
        self.model = model

    def car_type(self):
        return f"My car is {self.make} {self.model} model with {self.engine.horsepower}hp and wheel size is {self.wheels[1].size}."


car = Car("Ford", "2027", 200, "19in")

print(car.car_type())