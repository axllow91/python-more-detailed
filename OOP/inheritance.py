class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []  # initialize empty array

    def average(self):
        return sum(self.marks) / len(self.marks)


# inherits Student class
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        # super is the parent class
        super().__init__(name, school)  # calling super class constructor
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5


rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf)

rolf.marks.append(59)
rolf.marks.append(99)
print('Average salary: ', rolf.average())
print('Printing the definition of the method: ', rolf.weekly_salary)

# with the decorator we can call the method without the brackets
print('Weekly salary: ', rolf.weekly_salary)
# this call in weekly_salary() will not work if we tag the method at @property
# @property an call when we only calculate(return something) and we don't need other operations
# print('Weekly salary: ', rolf.weekly_salary())
