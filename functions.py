
# o functie = un bloc de cod reutilizabil care face o anumita sarica
# poti sa o apelezi de cate ori ai nevoie, fara sa scrii din nou codul
# poate sa primeasca date de intrare (parametrii) si sa returneze rezultate (return)

# definim o functie numita "greet"
def greet():        # condul indentat reprezinta corpul funcitiei
    print("Ciao")   # aceasta este actiunea functiei: afiseaza "Ciao"


# functia NU POATE fi apelata inainte de a fi definita
# am declarat mai sus functia "greet" si apoi o putem apela de cate ori vrem:
# greet()
#
# greet()
#
# greet()
#
# greet()

# parametrii functiei sunt date de intrare ("nume" in cazul asta)
def salut(nume):
    print(f"Salut, {nume}")

salut("Ana")
salut("Mihai")
salut("Cristi")

# functii cu return:

def aduna(a, b):
    return a + b

rezultat = aduna(5, 3)
print(rezultat)

x = None
print(type(x))

def calculeaza(a, b):
    suma = a + b
    diferenta = a - b
    return suma, diferenta

rezultat_suma, rezultat_diff = calculeaza(10, 4)

print("Suma: ", rezultat_suma)
print("Diferenta: ", rezultat_diff)

# functie care verifica daca un numar este prim

def este_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(este_prim(7))   # True
print(este_prim(10))  # False
print(este_prim(44))  # False
print(este_prim(13))  # True


# functie care caculeaza factorialul unui numar
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1

    rezultat = 1
    for i in range(1,n + 1):
        rezultat *= i  # rezultat = rezultat * i

    return rezultat

print(factorial(3)) # 1 * 2 * 3 = 6
print(factorial(5)) # 1 * 2 * 3 * 4 * 5 = 120
print(factorial(-7))


# Functii in functii (Nexted Functions)
# definim o functie in interiorul alteia

def mesaj_principal(nume):        # functia principala primeste un parametru
    def formateaza_mesaj(text):   # functia interna primeste alt parametru
        return f"Salut, {nume}!  {text}"   # acceseaza si "nume" din functia parinte, dar si "text"

    return formateaza_mesaj("Bine ai venit la curs!")  # apelam functia interna

print(mesaj_principal("Mircea"))   # return: "Salut, Mircea! Bine ai venit la curs!

# calculator de TVA
# - o functie care calculeaza pretul final cu tot tu TVA
#           - in interior avem o functie care calculeaza doar TVA-ul

def calculeaza_pret_final(pret, tva_procent):

    def calculeaza_tva(suma):
        return suma * tva_procent / 100

    tva = calculeaza_tva(pret)
    pret_final = pret + tva
    return pret_final

print(calculeaza_pret_final(100,21))  # 121

# *args
def aduna_2(a, b):
    return a + b

rezultat_2 = aduna_2(5, 3)

def aduna_3(a, b, c):
    return a + b + c

rezultat_3 = aduna_3(4, 7, 3)
print(rezultat_3)

def aduna_4(a, b, c, d):
    return a + b + c + d

rezultat_4 = aduna_4(4, 7, 3, 6)
print(rezultat_4)

# *args il folosim atunci cand vrem sa dam oricate argumente unei functii
def aduna_5(*args):
    total = 0
    for num in args:
        total += num
    return total

rezultat = aduna_5(3,4,6,7,89,2,123,45,5,3,2)  # *args colecteaza toate argumentele intr-un tuple
print(rezultat)

# ar fi similar cu:

def aduna_6(*args):
    return sum(args)

print(aduna_6(2,3,6,8,123,43,3,19))


# **kwargs vine de la keyword arguments = argumente cheie/valoare
# ** colecteaza toate argumentele numite intr-un dicitonar
# il folosim cand nu stim exact ce parametrii va primi functia

def creeaza_profil(**kwargs):
    rezultat = "Date utilizator:\n"
    for cheie, valoare in kwargs.items():
        rezultat += f"{cheie} : {valoare}\n"
    return rezultat

profil = creeaza_profil(nume = "Mircea", varsta = 31, oras = "Bucuresti")
print(profil)

def creeaza_melodie(**kwargs):
    rezultat = "Detalii melodie:\n"
    for cheie, valoare in kwargs.items():
        rezultat += f"{cheie} : {valoare}\n"
    return rezultat

melodie = creeaza_melodie(titlu = "Oda Bucuriei", compozitor = "Beethoven", gen = "Clasic", note = ["Do","Re","Mi","Fa","Sol"])
print(melodie)

melodie_2 = creeaza_melodie(titlu = "Simfonia Lunii", compozitor = "Mozart", gen = "Romantic", note = ["La","Si","Do#","Fa","Sol"])
print(melodie_2)


# media notelor unui student

def media_note(note):
    return sum(note) / len(note)

note_student = [8, 9, 10, 7]
print(media_note(note_student))


# functie pentru verificare cont bancar, daca un client poate primi credit
# conditia ar fi salariu - datorii >= 1000
def credit_aprobat(salariu, datorii):
    if  salariu - datorii >= 1000:
        return True
    else:
        return False

print(credit_aprobat(3000,1500))  # diferenta e 1500 -> True
print(credit_aprobat(2000,1200))  # diferenta e 800  -> False
print(credit_aprobat(8000,7200))  # diferenta e 800  -> False


# functie care creeaza o rezervare la hotel

def rezervare_hotel(nume, nopti, pret_pe_noapte):
    total = nopti * pret_pe_noapte
    return f"Rezervare pe numele {nume} pentru {nopti} nopti. Total: {total} RON."

print(rezervare_hotel("John Smith",3,250))
print(rezervare_hotel("Mike Saylor",5,230))
print(rezervare_hotel("Peter Smith",2,420))
print(rezervare_hotel("Chris Anderson",9,300))

coduri_scanate = ["3721987321987398721","3982198382193922","98321809398210293"]
cod = input("Scaneaza pradus: ")  # poti introduce date in consola python cu functia "input"
print("Am scanat:",cod)






