
# operatorii aritmetici + - * / // % **

# operatori de atribuire/asignare
# "=" este principalul operator
# pe langa "=" exista operatori compusi care combina atribuirea cu operatii aritmetice

my_age = 20
print(my_age)

my_age += 1    # echivalent cu my_age = my_age + 1
print(my_age)

my_age -= 2    # echivalent cu my_age = my_age - 2
print(my_age)

my_age *= 3    # echivalent cu my_age = my_age * 3
print(my_age)

my_age /= 2    # echivalent cu my_age = my_age / 2
print(my_age)

# operatorii de comparatie (folositi pt a compara 1 sau mai multe valori)

print(4 == 4)   # "este egal cu"
print(4 != 5)   # "este diferit de"
print(5 > 3)
print(2 < 1)
print(4 >= 5)
print(5 <= 5)

a = 10
b = 10
print(id(a))
print(id(b))


# operatorii logici (combina conditii booleene)
print(4 == 4 and 3 == 3)  # True (cand avem "and" -> trebuie ca toate conditiile sa fie respectate)
print(4 == 4 or 3 == 4)   # True (cand avem "or" -> doar una dintre conditii trebuie sa fie respectata)
print(not (4 == 4))       # False (negarea adevarului) -> not(True) = False

my_data = {"age":18}
your_data = {"age":18}

print(my_data == your_data)  # == compara continutul obiectelor, ambele dict au aceeasi cheie/valoare -> True
print(my_data["age"] == your_data["age"])   # valoare egala

list1 = [1,2,3]
list2 = [1,1,3]
x = 1
print(list1[0] == list2[1])  # True : index 0 din list 1 este egal cu index 1 din list 2
print(list1[0] == x)   # True

x = 15
y = 30
z = 5
flag = True

# de evitat conditii foarte complexe ca mai jos (se recomanda impartirea pe bucati)
result = ((x < y and y > z) or (not flag and x == z) and (y != 0 or z < 10))
print(result)