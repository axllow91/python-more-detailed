__author__ = 'dev'
age = 24
print("My age is " + str(age) + " and an author named: " + __author__)

# replacement field
print("My age is {0} years ".format(age))

# having multiple replacement fields
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7} ".format(31, "January", "March",
                "May", "July","August","October ","December"))

# better option form multiple replacement fields
# Having multiple replacement fields with an easier approach

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

# \n for new line
# %d for integer values like a format printing in java or c++
# %s for strings
print("\nMy age is %d years" % age)
print("\nMy age is  %d %s, %d %s" % (age, "years", 6, "months"))

# print i, i ^ 2, i ^ 3
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

# print the with 50 decimal points
print("Pi is approximately %12.50f" % (22 / 7))