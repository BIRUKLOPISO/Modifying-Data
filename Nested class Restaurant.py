class Restaurant:
    class MenuItem:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def display(self):
            return f" {self.name} ${self.price}"
    def __init__(self):
        self.menu_items = []

    def add_menu_item(self, name, price):
        menu_item = Restaurant.MenuItem(name, price)
        self.menu_items.append(menu_item)
    def show_menu(self):
        for _ in self.menu_items:
            print(_.display())

restaurant  = Restaurant()
restaurant.add_menu_item("Kitfo", 200)
restaurant.add_menu_item("Canjeero", 10)
restaurant.show_menu()
