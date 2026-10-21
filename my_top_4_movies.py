from datetime import datetime
import time
# am creat mai jos o lista care contine 4 dictionare
# fiecare are cheile: title, year, rating, description

favourite_movies = [
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.6,
        "description": "A great movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Christopher Nolan"],
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "genres": ["Action","Sci-Fi","Thriller"]
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "rating": 8.6,
        "description": "An interesting movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Jonathan Nolan","Lilly Wachowski"],
        "actors": ["Anne Hathaway", "Jessica Chastain", "Elliot Page"],
        "genres": ["Adventure", "Thriller"]
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "description": "Nice movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Lana Wachowski"],
        "actors": ["Leonardo DiCaprio", "Elliot Page","Christian Bale", "Aaron Eckhart"],
        "genres": ["Action", "Sci-Fi"]
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "rating": 8.7,
        "description": "An old movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Christopher Nolan"],
        "actors": ["Christian Bale", "Aaron Eckhart"],
        "genres": ["Action", "Crime"]
    }
]

print(favourite_movies)
print(favourite_movies[0])

print(favourite_movies[0]["title"])
print(favourite_movies[1]["year"])
print(favourite_movies[2]["rating"])
print(favourite_movies[3]["description"])

print("The title of the first movie is: ", favourite_movies[0]["title"])
print("The release year of the second movie is:", favourite_movies[1]["year"])
print("The IMDB rating of the third movie is:", favourite_movies[2]["rating"])
print("The short description of the fourth movie is:", favourite_movies[3]["description"])


print("The lead director of the first movie is:", favourite_movies[0]["directors"][0])
print("The lead writer of the second movie is:", favourite_movies[1]["writers"][1],)
print("The lead star of the third movie is:", favourite_movies[2]["actors"][2])
print("The main genre of the fourth movie is:", favourite_movies[3]["genres"][-1])

# aici am calculat media rating-ului:
# adunam 4 variabile de tip float si le impartim la 4
average_rating = (favourite_movies[0]["rating"] +
                  favourite_movies[1]["rating"] +
                  favourite_movies[2]["rating"] +
                  favourite_movies[3]["rating"]) / 4
print("The average rating of all movies is: ", average_rating)

# aici aflam varsta medie a filmelor
current_year = datetime.now().year
print(current_year)
average_age = ((current_year - favourite_movies[0]["year"]) +
               (current_year - favourite_movies[1]["year"]) +
               (current_year - favourite_movies[2]["year"]) +
               (current_year - favourite_movies[3]["year"])) / 4
print("The average age of movies is: ", average_age)

now = datetime.now()
print(now)

print("Start")
time.sleep(12)  # aici avem o pauza de 12 secunde
print("End after 12 sec.")