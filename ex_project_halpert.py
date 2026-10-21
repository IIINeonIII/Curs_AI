
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(7))
print(even_or_odd(284))


def even_or_odd_extended(numbers):

    # verificam daca lista nu e goala
    if not numbers:
        return {"Error:" "Lista este goala. Introdu numere valide."}  # folosind dict aici -> mai structurat, mai extensibil
    # initializam listele pentru numere pare/impare
    even_numbers = []
    odd_numbers = []

    # parcurgem fiecare numar din lista, verificam daca e par/impar
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            odd_numbers.append(n)

    # sortare : sortam listele create - folosim functia sort()
    # lista cu numerele pare o sortam crescator
    # lista cu numerele impare o sortam descrescator (reverse = True)
    even_numbers.sort()
    odd_numbers.sort(reverse=True)

    return even_numbers, odd_numbers

numbers = [10, 3, 7, 4, 12, 9, 2, 5]
even_list, odd_list = even_or_odd_extended(numbers)
print("Numere pare (crescator): ", even_list)
print("Numere impare (descrescator: ", odd_list)


# crearea a unei functii "basic_operatons" cu 3 argumente
# input: operation, value1, value2
# output: returneze rezultatul operatiei specificate intre value1 si value2

def basic_operations(operation, value1, value2):
    if operation == "add":
        return value1 + value2
    elif operation == "subtract":
        return value1 - value2
    elif operation == "multiply":
        return value1 * value2
    elif operation == "divide":
        if value2 == 0:   # impartirea la 0 nu este permisa
            return "Error: division by zero"
        return value1 / value2
    else:
        return "Error: unknown operation"

print(basic_operations("add",5,3))
print(basic_operations("subtract",10,4))
print(basic_operations("multiply",6,7))
print(basic_operations("mod",10,2))


# creaza o functie "total_points" care primeste o lista de rezultate ale meciurior
# fiecare rezultat e string in formatul "x:y"
# x - scorul echipei tale
# y - scorul adversarului

# Functia trebuie sa calculeze punctele total obtinute astfel:
# 1. Victorie (x > y) -> 3 puncte
# 2. Egal (x == y) -> 1 punct
# 3. Infrangere (x < y) -> 0 puncte

# Functia returneaza nr total de puncte acumulate

def total_points(results):

    points = 0
    # trebuie parcursa lista de string-uri
    for r in results:
        x, y = r.split(":")    # separate scorurile, cu split(
        x, y = int(x), int(y)  # le transformam in numere intregi
        if x > y:
            points += 3
        elif x == y:
            points += 1

    return points

results = ["3:1", "2:2", "0:1", "4:0", "1:1"] # daca apelam functia pe acest ex: 3 + 1 + 0 + 3 + 1= 8


# crearea unei functii largest_numer care primeste 3 numere intregi a b si c
# fct trebuie sa determine cea mai mare valoare posibila obtinuta prin combinarea celor 3 numere
# trebuie sa fie verificate conditiile:
# a + b + c
# a * b * c
# (a+b) * c
# a * (b+c)

def largest_number(a,b,c):
    return max(a + b + c,  a * b * c,  (a + b) * c,  a * (b + c))


print(largest_number(1, 2, 3))  # output 9 -> (1+2)*3
print(largest_number(2, 1, 1))  # output 4 -> 2 *(1+1)
print(largest_number(3, 2, 2))  # output 12-> 3*(2+2)


# cream o functie numita "inex" care primeste 2 argumente
# 1. array - o lista de nr intregi
# 2. n - un index (nr intreg)

# return: elementul de la pozitia n din lista ridicat la puterea n, adica array[n] ** n
# daca indexul n nu e valid (adica e negativ sau mai mare ca ultimul index din lista) -> functia sa returneze -1

def index(array, n):
    if  0 <= n < len(array):
        return array[n] ** n
    else:
        return -1

print(index([1, 2, 3, 4], 2))  # Output(Iesiri): 3 ** 2 = 9
print(index([1, 3, 10, 100, 3],3)) # Output(Iesiri): 100 ** 3 = 100000
print(index([1, 2, 3, 4], 5))  # Output(Iesiri): -1 (index invalid)
print(index([1, 2, 3, 4], -1)) # Output(Iesiri): -1 (index invalid)

# variante diferite pt functia "index", care au aceeasi functionalitate
def index2(array, n):
    try:
        return array[n] ** n
    except IndexError:
        return -1

def index3(array, n):
    return array[n] ** n if  0 <= n < len(array) else -1


# creeaza o functie care primeste nr unei luni (1-12) si returneaza trimestrul corespunzator
# Ian-Mar -> 1, Apr-Jun -> 2, Iul-Sept ->3, Oct-Dec ->4

def quarter_of_the_year(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
    else:
        return None # pentru valori invalide

print(quarter_of_the_year(11))  # returneaza 4
print(quarter_of_the_year(23))
print(quarter_of_the_year(7))


# creaza o functie
# Input: primeste un an intreg
# Output: returnarea secolului corespunzator

def century(year):
    if year % 100 == 0:  # 1900 % 100 = 0 -> 1900 se termina exact cu 00, verific daca anul e ultimul dintr-un secol
        return year // 100   # // este impartirea intreaga: -> 1900 // 100 = 19,  1400 // 100 = 14
    else:
        return year // 100 + 1  # 1705 -> 1705 // 100 = 17 ->  17 + 1 -> 18

print(century(1705)) # output: 18
print(century(1950)) # output: 20












