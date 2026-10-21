
# if - instructiune conditionala
# instructiunea "if" evalueaza daca o conditie e adevarata sau falsa
# Daca e adevarata, executa blocul de cod din interiorul ei, altfel il sare

# ex. conditie adevarata
if 1 == 1:
    print("Conditia este adevarata!")

# ex. conditie false
if 1 == 2:
    print("Conditia este adevarata!")  # acest cod nu se va executa

# Instructiunea "else"
# ofera un bloc alternativ de cod, executat daca "if" nu este indeplinit
# ex. cu if + else:
if "hello" == "ciao":
    print("Conditia este adevarata!")
else:
    print("Conditia este falsa!")

x = 15
y = 10

if x > 10:
    print("x este mai mare decat 10")

if x > y:
    print("x este mai mare decay y")

# comparam elementele din dictionare
person1 = {"name": "Ana", "age": 25}
person2 = {"name": "Maria", "age": 27}

if person1["age"] == person2["age"]:
    print("Cele 2 au aceeasi varsta.")
else:
    print("Cele 2 au varste diferite")

if person1["age"] == person2["age"] and person1["name"] != person2["name"]:
    print("Fetele au aceeai varsta, dar nume diferite.")

# comparam elementele din aceeasi lista
my_shopping_list = ["apple",'apple']
if my_shopping_list[0] == my_shopping_list[1]:
    print("Primele 2 produse sunt identice.")


# conditii multiple

x = 17

if x % 3 == 0 and x % 5 == 0:
    print("x este multiplu de 3 si 5")
elif x % 3 == 0:
    print("x este multiplu de 3")
elif x % 5 == 0:
    print("x este multiplu de 5")
else:
    print("x NU este multiplu de 3 sau 5")

animals = [
    {"name": "Mango", "type":"dog", "age": 7},
    {"name": "Berry", "type":"dog", "age": 12},
    {"name": "Mango", "type":"cat", "age": 7}
]

if animals[0]["type"] == "dog" and animals[1]["type"] == "dog" and animals[2]["type"] == "dog":
    print("Toate animalele din lista sunt caini.")
elif animals[0]["type"] == "dog" or animals[1]["type"] == "dog" or animals[2]["type"] == "dog":
    print("Exista cel putin un caine in lista, dar cel mult 2")
else:
    print("Nu exista niciun caine in lista animals.")












