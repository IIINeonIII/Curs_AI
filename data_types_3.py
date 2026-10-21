
# Dictionaries (Dictionare)
# asociaza chei unice cu valori corespunzatoare
# folosim ca sintaxa { } si fiecare cheie o separam cu ":" fata de valoarea asociata
# structurile cheie:valoare se separa cu ","

person = {
    "name": "Mircea",
    "age": 31
}

# "name" si "age" sunt chei
# "Mircea" si "31" sunt valori corespunzatoare acestora

print(person["name"])
print(person["age"])
print(person)

product = {
    "name" : "Laptop",
    "price": 3500,
    "in_stock": True
}
print(product)
print(type(product))

# cheile (keys) trebuie sa fie imutabile: int,float,str,boolean (NU POT FI list,dict,set)
# valorile (values) pot fi orice tip de date: int,float,str,boolean,list,tuple,dict


# Lists (Liste)
# Sintaxa: sunt create folosind paranteze patrate [] iar elementele sunt separate cu ","

# exemplu de liste:
shopping_list = ["banana", "bread", "oat milk"]   # 3 produse, separate prin virgule
print(shopping_list)
print(type(shopping_list))

numbers = [35, 8, 12, 6]   # lista de integeri

mixed_list = [35, "milk", 12, "sugar", 36.48]
# 5 elemente, ele au index 0,index 1, index 2, index 3, index 4
# daca ai 5 elemente -> ai index de la 0 la n-1, adica 0-4
# daca ai 17 elemente -> ai index de la 0 la n-1, adica 0-16
print(type(mixed_list))
print(mixed_list[0])
print(mixed_list[1])
print(mixed_list[2])
print(mixed_list[3])
print(mixed_list[4])
# print(mixed_list[5]) index 5 este "out of range" in acest caz, nu exista index 5

numbers_2 = list(range(100))     # de la 0 la n-1  -> de la 0 la 100-1  -> de la 0 la 99
print(numbers_2)

numbers_3 = list(range(7,100))   # de la 7 la 100-1 -> de la 7 la 99
print(numbers_3)

numbers_4 = [35.5, 8.6, 7, 12.3, 6.32]
print(numbers_4[2])

x = numbers_4[0]
y = int(x)
print(y)


# Sets (Seturi)
# gestionarea datelor unice si neordonate
# setul se creaza folosind {}, dar fara simbolul ":" folosit la dictionare

fruits = {"apple", "banana", "cherry"}   # set cu 3 fructe distincte

numbers_5 = {1, 2, 2, 2, 3, 4, 4, 5} # set cu valori duplicate eliminate automat
print(numbers_5)     # set-ul va deveni {1, 2, 3, 4, 5}

numbers_5.add(1)
print(numbers_5)

# Luam o lista cu duplicate:
fruits_2 = ["apple", "banana", "cherry", "banana", "apple", "apple"]
print(fruits_2)

# Apoi din lista facem set:
fruits_set = set(fruits_2)    # set() = transforma ce ii dai intr-un set
print(fruits_set)

# Apoi din set facem lista inapoi:
unique_fruits = list(fruits_set)    # list() = transforma ce ii dai intr-o lista
print(unique_fruits)

unique_fruits_2 = list(set(fruits_2))
print(unique_fruits_2)

# il putem folosi daca avem o lista de x mail-uri si vrem sa stergem duplicatele pt a nu da aceleasi persoane de 2 ori
email = ["ana@gmail.com", "bob@yahoo.com", "ana@gmail.com", "dan@hotmail.com"]
unique_email = list(set(email))
print(unique_email)

# Tuple
# sunt similare cu listele, doar ca sunt imutabile
# imutabile = odata create, continutul lor nu mai poate fi modificat
# Sintaxa: se folosesc ( ) si elementele se separa prin ","

fruits_3 = ("apple", "banana", "cherry")
print(fruits_3)
print(type(fruits_3))

# fruits_3[0] = "strawberry" Acest cod va da eroare "TypeError"

bucharest = (44.426, 26.1025)
london = (51.5074, -0.1278)

not_a_tuple = ("single element")           # de fapt, este un string
one_element_tuple = ("single element",)    # acesta este tuple cu 1 singur element

# tipuri de date mixte

# seturile nu pot contine tipuri mutabile precum listele sau dictionary
# seturile accepta doar tipuri imutabile
mixed_set = {42, 3.14, "apple", ("banana", "cherry")}

# tuple poate contine: int, float, str, list, tuple, set, dictionary
person_info = ("John", 30, ("Python Developer", "Data Analyst"), [3.5, 4.7])

# dictionare intr-o lista

people = [
    { "name": "Numele tau", "age": 24},
    { "name": "Alt nume", "age": 38}
]










