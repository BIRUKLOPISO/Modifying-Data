from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """This must be implemented by subclasses"""
        pass

    def sleep(self):
        """Concrete method: shared by all subclasses"""
        print("Sleeping...")


class Dog(Animal):
    def make_sound(self):
        print("Bark!")

# animal = Animal()  # Raises TypeError: Can't instantiate abstract class


dog = Dog()
dog.make_sound()    # Output: Bark!
dog.sleep()         # Output: Sleeping...
