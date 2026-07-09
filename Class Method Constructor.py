class School:
    def __init__(self, name, year,address):
        self.name = name
        self.year = year
        self.address = address

    @classmethod
    def from_string(cls,school_info):

        name,year,address = school_info.split(",")
        return cls(name,int(year),address)


school = School.from_string("Vision,2016,Gofermeda")
print(school.name)
print(school.year)
print(school.address)
