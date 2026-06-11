class Photo:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price
photo1 = Photo("Wedding", 100)
photo2 = Photo("Birthday", 100)

print(photo1 == photo2)
print(photo1 < photo2)
print(photo1 > photo2)
print(photo1 <= photo2)
print(photo1 >= photo2)
print(photo1 != photo2)
