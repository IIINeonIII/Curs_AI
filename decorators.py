
# decorator = e o metoda de a "impacheta" (wrapped) o functie pt a ii adauga functionalitate
#             fara sa modificam codul acelei functii direct

# sintaxa:
# def "nume_decorator":
# ...
# @nume_decorator
# def nume_functie:
# ...
# nume_functie()

def decoratorul_meu(functia_originala):
    def functie_noua():
        print("Inainte de functie")
        functia_originala()
        print("Dupa functie")
    return functie_noua

@decoratorul_meu
def salut():
    print("Salutare, lume!")

salut()

# Ce se intampla mai sus?
# 1. Definim functia "salut"
# 2. Decoratorul @decoratorul_meu spune: "Inlocuieste "salut()" cu ce returneaza decoratorul_meu(salut)
# 3. decoratorul_meu(salut) returneaza functia wrapper
# 4. acum, "salut" devine wrapper
# 5. Cand apelezi salut() (cum e la linia 24), de fapt se executa wrapper()


def dubleaza_rezultatul(functie):
    def functie_noua():
        rezultat = functie()
        return rezultat * 2
    return functie_noua


@dubleaza_rezultatul
def numar():
    return 5
print(numar())

@dubleaza_rezultatul
def functie_string():
    return "Hello "
print(functie_string())





