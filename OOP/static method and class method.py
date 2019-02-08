class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = Student('Rolf', 'MIT')

rolf.marks.append(59)
rolf.marks.append(99)

print(rolf.average())


class Foo:
    @classmethod
    def hi(cls):
        # print class name
        print(cls.__name__)


my_object = Foo()
my_object.hi()


class Bar:
    @staticmethod
    def hi():
        print("Hello, i'm learning python and it's quite fun!")


Bar.hi()


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'  # example if we print 15.5 will print 15.50

    # that's how we create static methods
    # @staticmethod
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


number = FixedFloat(15.5)
print(number)
new_number = FixedFloat.from_sum(1.1, 2.33)
print(new_number)


# euro class inherits FixedFloat
class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'


money = Euro.from_sum(16.78, 10.1)
print(money)
