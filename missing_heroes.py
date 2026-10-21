
# favourite_movies este ca tip de date lista (are 4 elemente, index 0, index 1, index 2, index 3)
# cele 4 el din lista sun dictionare
# fiecare dictionar are mai multe chei si valori asociate

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

print(type(favourite_movies))


# avem o lista, de aceea folosim "for" pentru a parcurge elementele din lista
for movie in favourite_movies:
    if movie.get("directors") == []:   # verificam daca lista de directori este goala
        movie["directors"] = "Martin Scorsese"

print("\n")
print("Aici am adaugat directorul filmului:")
print(favourite_movies)

# iteram prin lista favourite_movies
for movie in favourite_movies:
    year = movie.get("year",0)

    if year < 1900:     #luam year si verificam daca e mai mic de 1900
        if year + 2000 > 1900:
            movie["year"] += 2000
        elif year + 1000 > 1900:
            movie["year"] += 1000
        else:
            movie["year"] += 3000

print("\n")
print("Aici am modificat anul:")
print(favourite_movies)

for movie in favourite_movies:
    if "actors" in movie:
        for i in range(len(movie["actors"])):
            if movie["actors"][i] == "Leonardo da Vinci":
                movie["actors"][i] = "Leonardo DiCaprio"

print("\n")
print("Aici am modificat numele actorului")
print(favourite_movies)

for movie in favourite_movies:
    if "genres" in movie:
        for i in range(len(movie["genres"])):
            if movie["genres"][i] == "":
                movie["genres"][i] = "Drama"

# exemplu de mai sus, cu while:

for movie in favourite_movies:
    if "genres" in movie:
        i = 0
        while i < len(movie["genres"]):
            if movie["genres"][i] == "":
                movie["genres"][i] = "Drama"
            i += 1

print("\n")
print("Aici am adaugat 'Drama' ca gen de film:")
print(favourite_movies)

allTheActors = []

for movie in favourite_movies:
    if "actors" in movie:
        allTheActors.extend(movie["actors"])


print("\n")
print("Aici am calculat numarul total de actori")

print(allTheActors)

lungimea = len(allTheActors)
print(lungimea)

mySet = set(allTheActors)
print(mySet)

uniqueList = list(mySet)
print(uniqueList)
# se poate face si direct cu sintaxa: uniqueList = list(set(allTheActors))






