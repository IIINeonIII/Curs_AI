
# o functie lambda = o functie anonima (fara nume) folosita pt operatii scurte si simple
# Sintaxa: lambda argumente: expresie

# Nu are nevoie de return - expresia e returnata automat
# Poate avea oricati parametrii, dar doar o singura expresie

# Functie normala
def aduna(x, y):
    return x + y

# Echivalent cu lambda
aduna_lambda = lambda x, y: x + y

print(aduna(3, 4))
print(aduna_lambda(3, 4))

functie_lambda = lambda x : x * 2
print(functie_lambda(14))

# lambda + map
# map() e o functie built-in in Python care aplica o functie fiecareui element dintr-o lista
# Sintaxa pt map():  map(functia, lista)
numbers = [1, 2, 3, 4, 5, 6, 7]
squared = list(map(lambda x: x**2, numbers))
print(squared)

squared_2 = list(map(lambda x: x**2,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(squared_2)

pare = list(map(lambda x: x % 2 == 0, numbers))    # ne va returna Boolean
print(pare)


# lambda + filter
# filter() e o functie built-in ce se ajuta sa filtram elementele dintr-o lista
# Sintaxa pt filter():  filter(functia, lista)
numbers = [1, 2, 3, 4, 5, 6, 7]
calcul = list(filter(lambda x: x * 5 <= 35 and x * 3 >= 15, numbers))
print(calcul)  # ne va returna o lista [5, 6, 7]

pare = list(filter(lambda x: x % 2 == 0, numbers))
print(pare)

# filtram produsele cu pret sub 100:
products = [
    {"name": "Laptop", "price":1200},
    {"name": "Mouse", "price":40},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300},
]

cheap_product = list(filter(lambda x: x["price"] < 100, products ))
print(cheap_product)


# lambda + sorted
# sorted() = functie built-in care returneaza o lista sortata a elementelor
# argumentul key = lambda x:x inseamna ca fiecare el x din lista va fi considerat tot x pt sortare
# Sintaxa: sorted(lista, key = None, reverse=False)

numbers = [5, 2, 9, 1, 7]
sortare_desc = sorted(numbers, key= lambda x: x**2, reverse=True)
# key = lambda x: x ** 2 = [25, 4, 81, 1, 49] -> pe astea le va sorta ->
# -> rezultatul va fi tot prima lista sortata
print(sortare_desc)

# filtrare, cele pare mai intai, ulterior cele impare
numbers = [16, 31, 4, 12, 27]
sortare = sorted(numbers, key = lambda x: 0 if x % 2 == 0 else 1)
print(sortare)

studenti = [("Liviu", 9),("Laura", 10),("Cristi", 5)]
student_sortati = sorted(studenti , key = lambda student: student[0])
# student -> reprezinta fiecare tuple
# student[1] -> ia nota (al doilea elemente din fiecare tuple)
# student[0] -> ia numele (primul elemente din fiecare tuple)
# deci sorted() va sorata lista dupa note/dupa nume, in functie de ce ii dam (student[0]/student[1])
print(student_sortati)


