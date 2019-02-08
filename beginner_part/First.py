'''
something here multiline
'''

name = "suka"

print(type(name))

print(name)

grocery_list = ['Juice', 'Tomato', 'Apple Green']

grocery_list[0] = "Green Juice"
print("First item", grocery_list[0])

print(grocery_list[0:3])

other_events = ['Wash car', 'Pick up kids', 'Cash check']

todo_list = [other_events, grocery_list]

print(todo_list)

grocery_list.append("Sansa")

print(grocery_list)

grocery_list.remove("Sansa")

grocery_list.sort()

print(grocery_list)

grocery_list.reverse()

print(grocery_list)

del grocery_list[2]

print(todo_list)

todo_list2 = other_events + grocery_list

print(len(todo_list2))

print(max(todo_list2))
print(min(todo_list2))

pi_tuple = (3,1,4,5,6,9)

new_tuple = list(pi_tuple)

new_list = tuple(new_tuple)