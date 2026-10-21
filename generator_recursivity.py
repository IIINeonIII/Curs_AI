# Exemplu cu functie recursiva
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  # apel recursiv

print(factorial(3))
# factorial(3) -> 3 * factorial(3-1) -> 3 * factorial(2)
# factorial(2) -> 2 * factorial (2-1) -> 2 * factorial(1)
# factorial(1) -> 1 * factorial(0)
# factorial(0) -> 1 (caz de baza, se opreste aici)
# rezultatul final: 3*2*1*1 = 6


# Generator
# un generator = o functie care returneaza valori pe rand,
# fara sa stocheze toate valorile in memorie
# in loc de "return" se foloseste "yield"

def numere_pare(n):
    for i in range(n):
        if i % 2 == 0:
            yield i  # returneaza valoarea i si pastreaza starea functiei

gen = numere_pare(10)
print(gen)

# o varianta de a folosi generatorul
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# a2a varianta pentru a folosi generatorul

for numar in numere_pare(100):
    print(numar)

lista = list(numere_pare(10))
print(lista)






