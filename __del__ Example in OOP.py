class Photos:
    def __init__(self,place, price, qty):
        self.place = place
        self.price = price
        self.qty = qty
        print(f"We have {self.qty} photos in {self.place} the price is {self.price}.")

    def __del__(self):
      print(f"The {self.place} photos with total price of {self.price}ETB are deleted. We had {self.qty} photos.")


photo = Photos("Studio",20,"10")

del photo