# __author__ = 'dev'
#
# # for loop
#
# for i in range(1, 12):
#     print("No {} squred is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#
# # if control flow
#
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0} ?".format(name))) # converting to an int
# print(age)
#
# if age > 25:
#     print("Something new")
# else:
#     print("Something old")
#
# print("Please guess a number between 1 and 10")
# guess = int(input())
#
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done you guessed it")
#     else:
#         print("Sorry, you havent guessed correctly")
# else:
#     print("You got it first time")
#
#
# if 15 < age < 66:
#     print("Have a good day")
#
# # and condition
# if 15 > 17 and 19 > 14:
#     print(0)
# else:
#     print(1)
#
# # or condition
# if(age < 15) or (age > 55):
#     print("Have a look at my age ".format(age))
# else:
#     print("I think i have this age ".format(age))
#
# x = "false"
# if x:
#     print("x is true")
#
#
# parrot = "Norwegian Blue"
#
# letter = input("Enter a character: ")
#
# # if letter is find inside the parrot word
# if letter in parrot:
#     print("Please read it: " + letter)
# else:
#     print("We couldn't find any letter that's suited for that word")
#
# # While condition

# available_exits = ["east", "north east", "south"]
#
# chosen_exists = ""
# # while the chose_exist is not find in the available array
# # try until you got the right direction
# while chosen_exists not in available_exits:
#     chosen_exists = input("Please choose a direction: ")
#
# print("aren't you glad you got out of there?")

# Guessing game
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0
trytoguess = 0

while guess != answer:
	guess = int(input())
	trytoguess += 1
	if trytoguess == 10:
		print("Your game is over!. Out of chanses")
		break
	if guess < answer:
		print("Please enter a new number. Your number was to low!")
	elif guess > answer:
		print("Please try to guess on a lower number")
	else:
		print("Congratulation! You have guessed the number!")
