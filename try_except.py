
# try-except este folosita pentru a trata exceptiile,
# astfel incat programul sa nu se opreasca brusc

# Impartirea la 0 nu se poate ( nici in matematica, nici in Python)
# -> ZeroDivisionError (daca rulam ex de mai jos)
# x = 10
# y = 0
# print(x / y)

try:
    # cod care poate genera o eroare
    x = 10 / 0
except ZeroDivisionError:
    # cod care se executa daca apare eroarea
    print("Nu poti imparti la zero!")

def imparte(a,b):
    try:
        rezultat = a / b
        print(f"Rezultatul este: {rezultat}")
    except ZeroDivisionError:
        print("Eroare: Impartirea la 0 nu este permisa")

imparte(10,2)
imparte(10,0)
imparte(15,19)

try:
    print(5/0)
except:
    print("Am intrat iar intr-o exceptie.")
finally:
    print("Se executa intotdeauna.")

# exemplu cu "TypeError"
try:
    print(10/"3")
except:
    print("A aparut o exceptie si aici")

# cum accesezi detalii despre eroare
# e -> contine detaliile despre eroare
try:
    10 + "text"
except TypeError as e:
    print("A aparut o eroare: ", e)

# Unde se mai poate folosi:
# 1. ZeroDivisionError
# 2. TypeError
# 3. ValueError  -> conversii invalide
# 4. IndexError  -> accesarea unui index inexistent in lista/tuple
# 5. KeyError    -> cand incerci sa accesezi o cheie inexistenta intr-un dict
# 6. FileNotFoundError -> cand deschizi un fisier care nu exista
# 7. AttributeError -> de ex. folosim "append" pe o variabila care e integer
# 8. ImportError/ModuleNotfoundError  -> import modul_inexistent

# Try/except/finally se foloseste pentru conexiune la API/Baze de date

