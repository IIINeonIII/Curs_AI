from data import favorite_books, favourite_movies, best_selling_albums # din data.py luam cele 3 liste
#import data # asta il folosim daca vrem sa importam tot din data.py

current_year = 2025

def average_age(objects, current_year):
    total_age = 0                   # initializam suma varstelor cu 0
    for obj in objects:
        total_age += current_year - obj["year"]  # total_age = 15 + 11 + 17 + 26 (pt favourite_movies)

    return total_age / len(objects)  # impartim totalul la numarul de obiecte pt a obtine media

print("Average age of favourite books:",average_age(favorite_books,current_year))
print("Average age of favourite movies:", average_age(favourite_movies, current_year))
print("Average age if best-selling albums:", average_age(best_selling_albums,current_year))


def average(objects, key):
    total = 0
    for obj in objects:
        total += obj[key]  # adunam valoarea pentru cheia data
                           # pt key = "sale" -> ne va luam ce avem ca valori la cheia "sale"
    return total / len(objects)

print("Average rating of favorite movies:", average(favourite_movies,"rating"))
print("Average sale of best_selling albums", average(best_selling_albums,"sale"))

def latest_or_oldest(objects, latest):

    selected = objects[0]  # asta este list[0], deci este in cazul nostru un dictionar intreg

    for obj in objects:
        if latest:    # daca vrem cel mai nou obiect (latest = True)
            if obj["year"]  > selected["year"]:
                selected = obj # daca obiectul curent e mai nou, il setam ca selected
        else:         # daca vrem cel mai vechi obiect (latest = False)
            if obj["year"]  < selected["year"]:
                selected = obj # daca obiectul curent e mai vechi, il setam ca selected

    return selected["title"]  # selected este dictionar, noi vrem sa returnam doar titlul lui

print("Latest book:", latest_or_oldest(favorite_books,True)) # la True ne va arata cel mai nou
print("Oldest book:", latest_or_oldest(favorite_books,False)) # la False ne va arata cel mai vechi




