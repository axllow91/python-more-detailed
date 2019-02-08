"""
 - Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

 - Add movies
 - See movies
 - Find a movie
 - Stop running the program

Tasks:
 - Decide where to store movies
 - What is the format of a movies
 - Show the user the main interface and get their input
 - Allow users to add movies
 - Show all their movies
 - Find a movie
 - Stop running the program when they type 'q'

"""
# movies empty list

movies = []

"""
    example of dictionary
    movies {
        'name': ... (str),
        'director': ... (str),
        'year':... (int)
    }
"""


# menu definition
def menu():
    user_input = input("Enter 'a' to add a movie, 'l' "
                       "to see your movies, 'f' to find a movie, 'q' to quit ")

    while user_input != 'q':

        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Something went wrong. Please try again!")

        user_input = input("Enter 'a' to add a movie, 'l' "
                           "to see your movies, 'f' to find a movie, 'q' to quit ")


# # add movie definition
def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie year: ")

    # # creating a dictionary var
    # movie = {
    #     'name': name,
    #     'director': director,
    #     'year': year
    # } OR

    # append the directory to the movies list
    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movie_list):
    print("--- Movies ----")
    for movie in movie_list:
        show_movies_details(movie)


def show_movies_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")


def find_movie():
    find_by = input("What property of the movie are you looking for? ")  # can be year name director
    looking_for = input("What ae you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    # found list
    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


# Calling menu function
menu()
