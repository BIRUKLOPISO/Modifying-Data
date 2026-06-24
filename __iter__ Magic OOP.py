class Choir:
    def __init__(self):
        self.singer = ["Hilu","Yimar","Zemen"]

    def __iter__(self):
        return iter(self.singer)

ch = Choir()

for i in ch:
    print(i)