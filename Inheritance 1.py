class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Donkey(Animal):
    pass


dog1 = Dog("Bobby")
cat1 = Cat("Wuro")
donkey1 = Donkey("Kura")

print(dog1.name)
print(dog1.is_alive)
dog1.sleep()
dog1.eat()

