import math   # math este un modul built-in in Python
              # doar trebuie importat in fisierele .py unde il folosim

# Python este limbaj compilat si interpretat
# Pas 1 : compilarea - fisierul .py este transformat intr-un fisier .pyc
# Pas 2 : interpretarea - codul este rulat de Python VM (Python Virtual Machine)

# Python este "high level language" - sintaxa simpla, apropiata de limba engleza
# Python este "dynamic typed" - nu trebuie sa declari tipul variabilei

# Nu se foloseste ";" ca sa inchidem o expresie (ca in C)
# Comentarii in Python se pun folosind "#"
# daca vreau sa comentez/decomentez mai multe linii -> Selectez liniile + (Ctrl + "/")

print("Azi avem curs de Python")  # "print" este o functie built-in in Python
print("Hello World")

# Reguli pentru veriabile:
# nu trebuie sa inceapa numele lor cu cifra (ex. 4person_info e un nume gresit)
# daca numele are mai multe cuvinte, trebuie separate prin "_"
# numele trebuie sa fie sugestiv
# ar trebui declarate cu litera mica la inceput
# in unele programe, constantele se trec cu majuscule (PI = 3.14 sau MAX_USERS = 100)
# PEP8 - contine conventii ale scrierii de cod in Python

# tipul de date "int"
x = 10    # variabila x are valoarea 10, variabila x este de tip "integer"
print(x)
print(bin(x))    # "bin" e functie built-in, ne arata valoare in binar
print(hex(x))    # "hex" e functie built-in, ne arata valoarea in hexa

# Variabilele se suprascriu
# Daca o variabila deja existenta "x" primeste o noua valoare,
# Python ii inlocuieste continutul
x = 57
print(x)

y = -34
z = 0
print(type(y))   # "type" e functie built-in, ne arata tipul de date al unei variabile
print(type(z))

# tipul de date "float"
a = 5.7
b = 9.234
c = 120.5
print(a)
print(type(a))

d = 10
e = 3
print(type(d/e))

# operatori matematici/aritmetici
# + adunare
# - scadere
# * inmultire
# ** ridicarea la putere
# /  impartirea reala (float) - se face impartirea si ne da 4.38, se ia 4.38
# // impartirea intreaga (doar partea intreaga) - se face impartirea si daca ne da 4.38, se ia 4
# % restul impartirii (modulo) - se face impartirea, nu conteaza cat da, se ia doar restul
# () paranteze rotunde - singurile acceptate in expresii matematice

# operator de asignare
# "=" este operator de asignare (NU este operator matematic si nici de comparatie)

# operattori de comparatie
# != == >= <= > < sunt operatori de comparatie (NU sunt operatori aritmetici/matematici)

rezultat_1 = 4 * 5 + 3  # 20 + 3 = 23 (in python se respecta ordinea operatilor)
print(rezultat_1)

rezultat_2 = (9 - 12) + 2 * (3 + 6) # -3 + 2*9 = -3 + 18 = 15
print(rezultat_2)

# ordinea operatilor in Python
# 1. Paranteze ( )
# 2. Exponent **
# 3. Inmultirea/Impartire/Module/Floor Division
# 4. Adunare/Scadere

rezultat_3 = 15 / 5    # chiar daca impart 2 integari si restul e 0, rezultatul va fi "float"
print("Aici avem rezultatul impartirii (float):")
print(rezultat_3)
print(type(rezultat_3))

rezultat_4 = 15 // 4   # rezultatul este mereu de tip "int"
print(rezultat_4)
print(type(rezultat_4))

rezultat_5 = 15 % 4    # modulo = restul impartirii -> 15/4 = 3 rest 3 -> rest = 3
print(rezultat_5)

rezultat_6 = 2 ** 5    # 2**5 = 2 * 2 * 2 * 2 * 2 (ridicarea la putere)
print(rezultat_6)

rezultat_7 = 9 ** 0.5  # cand ridicam la puterea "0.5" este de fapt radacina patrata a acelui nr (radical)
print(rezultat_7)

print(math.sqrt(9))
print(math.sqrt(25))
print(math.pi)
print(math.cos(0))
print(math.sin(math.pi/2))  # sin de 90 -> 1
print(math.factorial(5))   # 5 factorial = 1 * 2 * 3 * 4 * 5
print(math.log(100,10))   # 10^2 = 100 -> log in baza 10 din 100 = 2
print(math.log(10))     # logaritm natural(10) = ln(10) = 2.3025..

# folosim "\" pentru a scrie pe mai multe randuri, dar nu e recomandat
n = 1 + 2 + 3 + \
    4 + 5
print(n)

rezultat_8 = (2 + 3) * ((4 - 1) + (6 // 2))
print(rezultat_8)


