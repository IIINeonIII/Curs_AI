
# acces si modificari pe dictionary
my_personal_data = {
    "name" : "Mircea",
    "age" : 31
}

print(my_personal_data)

print(my_personal_data.get("name")) # Cu metoda get.() - NU da eroare daca cheia nu exista
print(my_personal_data["name"])     # [] folosesti sa te asigura ca cheia chiar exista

my_personal_data["age"] = 32        # se pote modifica datele intr-un dict (mutabilitate)
my_new_age = my_personal_data["age"]
print(my_personal_data)


# acces si modificari pe lista
my_shopping_list = ["banana", "paine", "lapte de ovaz", "rosii", "oua", "faina"]

my_first_item = my_shopping_list[0]
my_second_item = my_shopping_list[1]
last_item = my_shopping_list[-1]   # daca numaram invers, -1 e ultimul element, -2 e penultimul
print(last_item)

# Sintaxa pentru slicing ar fi [start:stop:step]

first_three = my_shopping_list[0:3]  # index 0, index 1, index 2
print(first_three)

from_index_2 = my_shopping_list[2:]  # index 2 -> pana la final
print(from_index_2)

last_two = my_shopping_list[-2:]     # index -2 -> pana la final
print(last_two)

middle_items = my_shopping_list[1:3]  # index 1, index 2 (de la 1 la n-1)
print(middle_items)

elements_with_step_2 = my_shopping_list[::2]   # toate elementele cu pas 2
print(elements_with_step_2)

reversed_list = my_shopping_list[::-1]   # inversarea listei
print(reversed_list)

selected_items = my_shopping_list[59:134:2]   # de la index 59 la index 134 (cu pas de 2)
print(selected_items)

my_shopping_list[0] = "ulei de masline"    # elementele listei se pot modifica (este tip de date mutabil)
print(my_shopping_list)

my_first_item_change = my_shopping_list[0] # putem crea o variabila noua si ii atribuim un element din lista

# append() - adauga un element in lista (la finalul listei, dupa ultimul element)
my_shopping_list.append("portocala")
print(my_shopping_list)

# insert() - adauga un element la un anumit index
my_shopping_list.insert(4,"morcov") # adauga "morcov" la index 4 si celor din dreapta li se modifica indexul
print(my_shopping_list)

# extend() - adauga mai multe elemente dintr-o lista
my_shopping_list.extend(["kiwi", "ananas"])
print(my_shopping_list)

# pop() - scoate elementu de la un index (default ultimul)
my_shopping_list.pop()
my_shopping_list.pop(1)   # scoate elementul de la index 1
print(my_shopping_list)

# remove() - sterge elementul dupa valoare
my_shopping_list.remove("morcov")
print(my_shopping_list)

# clear() - sterge toate elemente din lista
my_shopping_list.clear()
print(my_shopping_list)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b     # concatenare de liste
print(c)

d = a * 3     # repetare a unei liste (inmultire *)
print(d)


# acces si modificari pe seturi
# set = colectie neordonata de elemente unice -> daca dam "print" ele pot aparea in alta ordine, dar e ok
my_set = {"mar","banana","cireasa"}
print(my_set)
my_set.add("visine")   # similar cu "append" de la liste
print(my_set)

my_set.remove("mar")       # sterge un element (da eroare daca nu exista)
my_set.discard("banana")   # sterge un element (nu da eroare daca nu exista)
print(my_set)

my_set.pop()     # scoate un element aleator
print(my_set)

my_set.clear()   # stergem toate elementele din set
print(my_set)

# operatii pe set-uri
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

reuniune = a | b  # returneaza set cu toate elementele din a si b
print(reuniune)

intersectie = a & b
print(intersectie)

diferenta = a - b   # ce are "a" si nu are "b"
print(diferenta)

diferenta_simetrica = a ^ b  # elementele care apar in unul din seturi, dar nu in ambele (de fapt e (a-b) | (b-a) )
print(diferenta_simetrica)

reuniune.update([7, 8, 9, 10, 11])   # adauga in set toate elementele dintr-o lista
print(reuniune)


# acces si modificari pe tuple

my_tuple = ("mar","banana","cireasa","kiwi","ananas","visine","prune")  # index 0 -> index 6 (7 elemente)
first_item = my_tuple[0]
print(first_item)
# Sintaxa pentru slicing: tuple[start:stop:step]
# my_tuple[:2] slicing: ia elementele de la index 0 pana la n-1 -> de la index 0 la index 1 -> index 0, index 1

my_tuple = my_tuple[:2] + ("portocala",)  # index 0, index 1, index 2, index 3 + "portocala"
print(my_tuple)

my_tuple = my_tuple[::-1] + ("gutui",)
print(my_tuple)