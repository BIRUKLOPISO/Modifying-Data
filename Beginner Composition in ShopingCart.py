class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = [Product("Exercise book", 200),
 Product("Bic Pen", 100),
Product("New Bag", 400)]

    def total_price(self):
        return sum(p.price for p in self.products)






shop = ShoppingCart()
print(f"the total price is: ${shop.total_price()}")