class Choir:
    def __init__(self):
        self.singer = ["Hilu","Yimar","Zemen"]

    def __contains__(self,item):
        return item in self.singer

chor = Choir()
print("Hilu" in chor)