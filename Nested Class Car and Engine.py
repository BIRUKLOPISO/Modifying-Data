class Car:
    def __init__(self, brand):
        self.brand = brand
    class Engine:
        def __init__(self, hp):
            self.engine = hp
        def driving(self):
            return f"My car has {self.engine}hp engine."

car = Car("BMW")
engine = Car.Engine(100)
print(engine.driving())
print(f"So, my car is {car.brand} with {engine.engine}hp.")