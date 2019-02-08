# Errors
# Index Error
# friends = ['Rolf', 'Anne']
# friends[2] # we don't have a value at the index 2 (IndexError: list index out of range)

# Key Error
# def show_movie_details(movie):
#     print(f"Name: {movies['name']}")

# Name Error
# print(Hello) # NameError: name 'Hello' is not defined

# Attribute Error
# friends = ['Rolf', 'Jose', 'Charlie']
# friends_nearby = ['Rolf', 'Anna']
# friends.intersection(friends_nearby) # AttributeError: 'list' object has no attribute 'intersection'

# NotImplementedError
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     def login(self):
#         raise NotImplementedError('This feature has not implemented yet')

# RuntimeError - this is a base class that other error class inherits
# this error happens when you are running your program

# Syntax Error
# class User  # SyntaxError: invalid syntax (no columns after the name of the class)
#     def __init__(self, user, passw):
#         self.user = user
#         self.passw = passw

# Indentation Error
# def add_two(x, y):
# return x + y

# def add_two(x, y):
#     pass
#
# return x + y

# TabError
# def add_two(x, y):
#  return x + y

# TypeError
# 5 + 5 + 'hi' #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ValueError
# int('20.6') #ValueError: invalid literal for int() with base 10: '20.6'

# Import Error
# import blog
# def menu():
#     pass
#
# from __init__ import menu

# DeprecationWarning
# It is a warning that is seen like an error
# The thing you want to do is not the best way to do
# So the code you use might be old and not that fast/secure
# And for that exists new code that is written better and maybe faster
