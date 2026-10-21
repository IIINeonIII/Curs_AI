
# list comprehension = o modalitate concica si eleganta de a crea liste
#                      pe baza unor liste existente sau a unor secvente

# sintaxa: [ new item for item in iterable if condition ]

# avem o lista si vrem sa inmultim toate elementele ei cu 2
# exemplu clasic (fara list comprehension):

numbers = [1, 2, 3, 4]
numbers_doubled = []
for n in numbers:
    numbers_doubled.append(n*2)

print(numbers)
print(numbers_doubled)

numbers_list_comprehension = [n*2 for n in numbers]

#daca vrem sa luam doar numerele pare dintr-o lista si sa le inmultim cu 3
even_numbers = [n*3 for n in numbers  if n % 2 == 0 ]
print(even_numbers)


# list comprehension, atunci cand folosim si "else"
# sintaxa: [new_value_if_true if condition else new_value_if_false for item in iterable]

# numerele pare sa se inmulteasca cu 2, iar cele impare cu 3
numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [ x*2 if x % 2 == 0 else x*3 for x in numbers_2 ]
print(result)

# list comprehension cu doua for-uri
numbers_3 = [1, 2]
numbers_4 = [3, 4]
result_2 = [i**2 + j**3 for i in numbers_3 for j in numbers_4 ]
print(result_2)
# primul for i in numbers_3 ia fiecare element din numbers_3
# al doilea for j in numbers_4, pentru fiecare i, ia fiecare element din numbers_4
# i = 1
#       j = 3 -> 1**2 + 3**3 = 1 + 27 = 28
#       j = 4 -> 1**2 + 4**3 = 1 + 64 = 65
# i = 2
#       j = 3 -> 2**2 + 3**3 = 4 + 27 = 31
#       j = 4 -> 2**2 + 4**3 = 4 + 64 = 68


fruits = ["apple","mango","cherry"]
upper_fruits = [u.upper() for u in fruits]
print(upper_fruits)

lenghts = [len(i) for i in fruits]
print(lenghts)

first_letter = [i[0] for i in fruits]
print(first_letter)

# pe langa list comprehension, exista si:
# set comprehension
# dict comprehension

# set comprehension
# {expression for item in iterable if condition}
numbers_5 = [1,2,2,2,2,3,3]
unique_numbers = { n for n in numbers_5 }
print(unique_numbers)

emails = ["Bob@gmail.com", "Mark@gmail.com", "John@gmail.com", "Mark@gmail.com"]

unique_email_upper = { email.lower() for email in emails }
print(unique_email_upper)

unique_names = {email.split("@")[0] for email  in emails}
print(unique_names)


# dict comprehension
# dict comprehension, cheile le luam elementele din lista, valorile vor fi elementele ** 2
numbers_6 = [1, 2, 3, 4]
squared_dict = {k: k**2 for k in numbers_6}
print(squared_dict)

even_squares = {k: k**2 for k in numbers_6 if k % 2 == 0}
print(even_squares)

fruits = ["apple    ","    kiwi","  banana   "]
result_3 = {k.strip(): len(k.strip()) for k in fruits}
print(result_3)







