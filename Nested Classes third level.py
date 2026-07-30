class House:
    class Shelf:
        class Paper:
            def my_paper(self):
                return "I got the paper"
        def __init__(self):
            self.paper= House.Shelf.Paper()
        def myshelf(self):
            return "I got the shelf"


    def __init__(self):
        self.shelf = House.Shelf()


house = House()
print(house.shelf.myshelf())
print(house.shelf.paper.my_paper())



