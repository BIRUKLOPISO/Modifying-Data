class Car:
    def __init__(self):
        self.make =  {}


    def __setitem__(self,key,value):
        self.make[key] = value
        print(f"The car marked as {key} is changed too {value}.")

    def __getitem__(self,key):
        return self.make[key]


car1 = Car()
car1[1] = "Tesla"
car1[2] = "Toyota"
car1[3] = "Ford"
print(car1[1])
