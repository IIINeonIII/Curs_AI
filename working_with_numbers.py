import math
import random
# valoarea absoluta
print(abs(-52.5))

# rotunjire
# Sintaxa: round(number, ndigits)
# ndigit este optional, arata nr de zecimale
print(round(3.2))
print(round(3.8))
print(round(3.14159,3))

print(min(152,10,25,832,12))
print(max(152,10,25,832,12))

fructe = ["mar","banana","portocala","ananas"]
print(min(fructe))  # ananas
print(max(fructe))  # portocala

text = "python"
print(min(text)) # h

print(max(fructe, key=len)) # cel mai lung string
print(min(fructe, key=len)) # cel mai scurt string

a = [1, 5, 10]
b = [3, 7, 2]
c = [8, 0 ,4]

print(min(min(a),min(b),min(c))) # min(1,2,0) -> 0

note = {"Ion": 9,"Ana":10,"Maria":8}

print(min(note, key=note.get))
print(max(note, key=note.get))

# patru
def text_into_integer(text):
    numere = {
        "zero": 0,
        "unu": 1,
        "doi": 2,
        "trei": 3,
        "patru": 4,
        "cinci": 5,
        "sase": 6,
        "sapte": 7,
        "opt": 8,
        "noua": 9,
    }
    return numere.get(text.lower())

print(text_into_integer("DOI"))

print(sum([1, 2, 3, 4, 5, 6, 7])) # 28

numere_str = ["10.23","20.2","30.21","40.232"]
total = sum( round(float(x)) for x in numere_str )
print(total) # 10 + 20 + 30 + 40

numere_str_2 = ["1","2","3","4","5","-2","-4"]
total_pozitive = sum( int(x) for x in numere_str_2 if int(x) > 0 )
print(total_pozitive)

x = 8
y = -8
z = 0
print(type(x))
print(type(y))
print(type(z))

# numar complex
print(complex(1,2))

z = 1 + 2j
print(z.real)
print(z.imag)

# Logaritm = la ce putere trebuie ridica baza ca sa obtin rezutultatul dintre paranteze?

print(math.log10(1000))  # la ce putere il ridicam pe 10 ca sa ne dea 1000
print(math.log2(8))
print(math.log(1))  # logaritm natural (nu am scris nicio baza)
                    # inseamna logaritm in baza e (in matematica ln(e))
                    # "e" la ce putere ne da 1? La puterea 0

# modulul random
# integer aleator intre 1 si 10
i = random.randint(1,10)
print(i)

# floart aleator intre 0.0 si 1.0
f = random.random()
print(f)

# alegem random un element dintr-o lista
choice = random.choice([1, 2, 3, 4, 5])
print(choice)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(my_list)
print(my_list)

# o esantionare dintr-un interval
# Sintaxa "sample": sample(population, k) -> alege k elemente distincte din population
sample = random.sample(range(1,100),5)
print(sample)

# numar aleator float intr-un interval dat
f_interval = random.uniform(1.5, 2.5)
print(f_interval)
