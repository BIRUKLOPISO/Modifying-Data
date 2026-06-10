from datetime import datetime
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self._quantity = quantity
        self._last_restocked = datetime.now() if quantity > 0 else None
        self._sold =None

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_quantity):

        if new_quantity == 0 and self.quantity == 0:
            print("⚠️ OUT OF STOCK!")
            self._sold = datetime.now()

        if new_quantity > self._quantity:
            self._last_restocked = datetime.now()

        if new_quantity < self._quantity:

            print(f"📦 Low stock: {new_quantity} remaining")
            self._sold = datetime.now()



        self._quantity = new_quantity

product = Product("Laptop", 10)
product.quantity = 8   # Should print "📦 Low stock: 8 remaining" and update _last_sold



