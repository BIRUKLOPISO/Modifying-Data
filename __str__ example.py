class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return f"Student: {self.name} (Grade: {self.grade}, Age: {self.age})"


# Create a student
student1 = Student("Emma", "A", 15)


print(student1)
