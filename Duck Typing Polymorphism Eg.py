class Employee:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, employee):
        self.employee = employee

e1 = Employee("Bereket")
e2 = Employee("Getaneh")
e3 = Employee("Simion")

employee = [e1, e2, e3]

team = Team(employee)

for names in team.employee:
    print(names.name)
