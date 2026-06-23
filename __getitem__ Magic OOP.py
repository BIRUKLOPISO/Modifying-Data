class Car:
    def __init__(self):
        self.make = ["Ford", "Hundayi","Toyota"]

    def __getitem__(self,index):
        return self.make[index]



car1 = Car()
print(car1[0])
