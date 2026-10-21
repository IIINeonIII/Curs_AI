
# exista 2 tipuri de bucle in Python : for/while

# cand folosim for/while:
# for - il folosim cand stim de cate ori vrem sa repetam codul (ex. cand avem o lista sau un range)
# itereaza peste o secventa: lista, tuple, string, dict
# for-ul se opreste cand secventa s-a terminat

for i in range(50):
    print(i)   # se executa de 50 ori - de la 0 la 49

# while - il folosim cand nu stim exact de cate ori, dar stim ca o conditie trecut sa fie adevarata
# ruleaza atat timp cat conditia este True
# folosind "while" exista riscul de a intra in bucle infinite
# while-ul se opreste cand conditia devine False

x = 0
while x < 5:
    print(x)
    x += 1

# i nu este cuvant cheie in Python, e variabila de iteratie (la fiecare pas, i ia valoarea urmatorului element din lista)
for i in [0, 1, 2, 3 ,4]:
    print(i)

# exemplu cu "for" + "if"
animals = [
    {"name": "Mango", "type":"dog", "age": 7},
    {"name": "Berry", "type":"dog", "age": 12},
    {"name": "Mango", "type":"cat", "age": 7}
]

for animal in animals:
    if animal["type"] == "dog":
        print("Este un caine.")
    elif animal["type"] == "cat":
        print("Este o pisica.")
    else:
        print("Nu este nici caine, nici pisica.")


# exemplu cu "while" + "if"

x = 0  # initializeaza contorul pentru bucla "while"
animals_2 = ["dog","cat","bird","dog","cat"]

while x < len(animals_2):
    animal = animals_2[x]   # preia animalul curent din lista
    if animal == "dog":
        print("Animalul este un caine.")
    elif animal == "bird":
        print("Animalul este o pasare.")
    else:
        print("Animalul nu e nici caine, nici pasare.")
    x += 1

