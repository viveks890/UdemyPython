import sys as sys

# Storing movies in form of a list, containing title, director, year

movies = []

# Adding movies as per users input
def add_movies():
    movie_detail = ["Title", "Director", "Year"]
    movie = dict()

    for detail in movie_detail:
        movie[detail] = input(f"{detail} : ")

    movies.append(movie)

    return f"""Movie you have enetered is : {movie["Title"]}, 
          Director name is : {movie["Director"]},
          Make year is : {movie["Year"]}"""

list_movies = lambda : [movie["Title"] for movie in movies]

def movie_details():

    title = input("Search with name of the movie : ")

    for movie in movies:
        if movie["Title"] == title:
            return f"""Name : {movie["Title"]},
                  Director : {movie["Director"]},
                  Year : {movie["Year"]}"""
        else:
            print("No such movie in database")

user_option = {
    "a": add_movies,
    "b": list_movies,
    "c": movie_details
}

def menu():

    menu_prompt = """What do you want to do : a: Add Movies
                b: List all Movies
                c: Find details about a particular movie by title
                q: quit"""

    option = input(menu_prompt).lower()

    while option != "q":
        if option in user_option:
            selected_function = user_option[option]
            out = selected_function()
            print(out)
            option = input(menu_prompt).lower()
        else:
            print("Unknown Command please try again")
    else:
        sys.exit()
    

menu()







