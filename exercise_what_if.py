

favourite_movies = [
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.6,
        "description": "A great movie.",
        "directors": [],
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
        "genres": ["Adventure", "Thriller",""]
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "description": "Nice movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Lana Wachowski"],
        "actors": ["Elliot Page","Christian Bale", "Aaron Eckhart", "Leonardo da Vinci"],
        "genres": ["Action", "Sci-Fi"]
    },
    {
        "title": "The Matrix",
        "year": 999,
        "rating": 8.7,
        "description": "An old movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Christopher Nolan"],
        "actors": ["Christian Bale", "Aaron Eckhart"],
        "genres": ["Action", "Crime"]
    }
]

# Cerinta 1: folosim un "for" loop si functia "print" pt a afisa toate titlurile filmelor

for movie in favourite_movies:
    print(movie["title"])

# Cerinta 2: realizarea aceleasi sarcini, folosind un while loop

i = 0
while i < len(favourite_movies):
    print(favourite_movies[i]["title"])
    i += 1

# Cerinta 3: calculeaza rating-ul mediu al filmelor
# creare variabila total_rate = 0 inainte de loop
# adaugam rating-ul fiecarul film in loop
# dupa loop, imparte total_rate la nr de filme si sa afisam media
print("Average rating: ")

total_rate = 0
for movie in favourite_movies:
    total_rate += movie["rating"]

average_rate = total_rate / len(favourite_movies)
print(average_rate)  # 8.725

# a2a varianta de rezolvare:
average_rate_2 = sum([movie["rating"] for movie in favourite_movies]) / len(favourite_movies)
# average_rate_2 = (8.6 + 8.6 + 9.0 + 8.7)   /   4

numere = [1, 2, 3, 4, 5]
suma = sum(numere)
print(suma)

# Cerinta 4: Newest movie - gaseste cel mai nou film
# initializare newest_movie cu primul film
# parcurgem lista + actualizam daca gasim un film mai nou
# afiseaza titlul filmului cel mai nou

print("Newest movie:")
newest_movie = favourite_movies[0]
for movie in favourite_movies:
    if movie["year"] > newest_movie["year"]:
        newest_movie = movie

print(f"Newest movie: {newest_movie["title"]} - {newest_movie["year"]}")

# Cerinta 5: folosim loop-uri combinate pt a afisa actorii tuturor filmelor
# creaza variabila stars_by_movies ca string gol
# pentru fiecare film, adaugam titlul si actorii sai in string

print("Stars by movies:")
stars_by_movies = ""
for movie in favourite_movies:
    stars_by_movies += f"{movie["title"]}"
    for actor in movie["actors"]:
        stars_by_movies += f"  -  {actor}"
    stars_by_movies += "\n"

print(stars_by_movies)














