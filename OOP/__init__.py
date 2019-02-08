# creating a dictionary
my_student = {
    'name ': 'Something',
    'grades': [70, 80, 90, 99]
}


def calculate_avg(student):
    return sum(student['grades']) / len(student['grades'])


print(calculate_avg(my_student))



