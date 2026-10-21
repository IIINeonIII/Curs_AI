

movies = [
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.6,
        "description": "A great movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Christopher Nolan"],
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "genres": ["Action","Sci-Fi","Thriller"],
        "runtime": 148
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "rating": 8.6,
        "description": "An interesting movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Jonathan Nolan","Lilly Wachowski"],
        "actors": ["Anne Hathaway", "Jessica Chastain", "Elliot Page"],
        "genres": ["Adventure", "Thriller"],
        "runtime": 195
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "description": "Nice movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Lana Wachowski"],
        "actors": ["Leonardo DiCaprio", "Elliot Page","Christian Bale", "Aaron Eckhart"],
        "genres": ["Action", "Sci-Fi"],
        "runtime": 136
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "rating": 8.7,
        "description": "An old movie.",
        "directors": ["Christopher Nolan"],
        "writers": ["Christopher Nolan"],
        "actors": ["Christian Bale", "Aaron Eckhart"],
        "genres": ["Action", "Crime", "Drama"],
        "runtime": 210
    }
]

# task 1 - creare a unei functii care primeste argument o lista de filme
# asta ar trebui sa returneze o noua lista ce tontine titlurile filmelor, care includ "drama"

def dramas(movies):
    drama_movies = []

    for movie in movies:
        if "Drama" in movie["genres"]:
            drama_movies.append(movie["title"])

    return drama_movies


# task 2 - creata o functie "findbyGenre" care returneaza o lista cu titlurile filmelor ce corespund unui gen

def findbyGenre(genre,movies):
    movies_by_genre = []

    for movie in movies:
        if genre in movie["genres"]:
            movies_by_genre.append(movie["title"])

    return movies_by_genre


# task 3 - gaseste filmul cu cea mai mare durata, o functie "longestMovie"

def longestMovie(movies):

    if not movies:
        return None

    # 'key' specifica atributul pe baza caruia se face comparatia (runtime)
    longest = max(movies, key=lambda m: m["runtime"])

    return longest

# task 4 - creaza o functie "longestMoviebyGenre" care identifica filmul cu cea mai mare durata dintr-un gen

def longestMoviebyGenre(genre, movies):
    filtered_movies = [movie for movie in movies if genre in movie["genres"]]

    if not filtered_movies:
        return None

    longest = max(filtered_movies, key=lambda m: m["runtime"])

    return longest

result1 = dramas(movies)
print("Filme de tip Drama: ", result1)

result2 = findbyGenre("Action",movies)
print("Filme de actiune:", result2)

result3 = longestMovie(movies)
print("Filmul cu cea mai mare durata este: ", result3["title"], "-", result3["runtime"], "minute.")

result4 = longestMoviebyGenre("Sci-Fi",movies)
print("Cel mai lung film Sci-Fi este:", result4["title"], "-", result4["runtime"], "minute.")









