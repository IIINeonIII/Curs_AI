
# String
# string = date de tip text ca o secventa de caractere - pot fi litere, cifre, simboluri
# este esential pt a fi incardrat intre ghilimele (' ' sau " ") pt a fi recunoscut ca sir de caractere

text1 = 'Acesta este un string cu ghilimele simple'  # single quote
text2 = "Acesta este un string cu ghilimele duble"   # double quotes

print(text1)
print(text2)
print(type(text1))
print(type(text2))

# Nu trebuie amesteca tipurile de ghilimele
# text3 = "Python e un limbaj interesant'
# print(text3)

# Se recomanda folosirea " " , in loc de ' '
text3 = "It's a great day."
print(len(text3))    # len e functie built-in ce se ne ajuta sa vedem lungimea unui string

# Concatenarea stringurilor (lipirea lor cu +)
text4 = "acesta " + "urmatorul"
print(text4)

# Repetare a unui string
text5 = "Hello " * 7
print(text5)
print(type(text5))

text6 = "4" + str(3)
print(text6)
print(type(text6))

text7 = int("4") + 3
print(text7)
print(type(text7))


# Boolean
# booleanii reprezinta valori de adevar si pot avea doar 2 valori posibile:
# True (Adevarat)
# False (Fals)

cleaned_my_room = True
print(type(cleaned_my_room))

cleaned_entire_house = False
print(type(cleaned_entire_house))

# True si False sunt cuvinte cheie in Python, trebuie scrise cu Majuscula la inceput
# NU SUNT STRINGURI!!

# Tipul de date "NoneType" - initializeaza o variabila fara valoare concreta
# "None" reprezinta lipsa unei valori sau valoare nula
rezultat = None
print(rezultat)
print(type(rezultat))

