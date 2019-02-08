class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    # when we create a function inside a class
    # we call it method
    def average(self):
        return sum(self.grades) / len(self.grades)


# create new object
# definition of an object:
# an object is something that we can store data
# and we can tell to this object what data we want to store
student_one = Student('Marian Dobre', [90, 66, 88, 99])
print("student_one.average: ", student_one.average())

student_two = Student('Dumitru Dobre', [99, 99, 88, 80])
print("student_one.average: ", student_two.average())

if student_two.average() > student_one.average():
    print(student_two.name, "is a great student")

print(student_one.__class__)
