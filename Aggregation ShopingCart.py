class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self, items):
        self.products = items

    def total_price(self):
        return sum(p.price for p in self.products)


p1 = Product("Exercise book", 100)
p2 = Product("Bic Pen", 200)
p3 = Product("New Bag", 300)

products = [p1, p2, p3]

shop = ShoppingCart(products)
print(f"the total price is: ${shop.total_price()}")