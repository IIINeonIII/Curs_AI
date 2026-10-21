def string_repeat(a, b):
    return a * b

print(string_repeat(2, "HawaiPizza"))

def no_space(a):
    return a.strip()

print(no_space("     HawaiPizza "))

def number_to_string(num):
    return str(num)

numm = (number_to_string(34))
print(type(numm))

def boolean_to_string(s):
    if s == True:
        return "True"
    if s == False:
        return "False"

boolean = (boolean_to_string(True))
print(boolean)
print(type(boolean))

def abrev_name(name):
    red = name.split(" ")
    initials = "".join(d[0] + "." for d in red)
    return initials[:-1]

g = abrev_name("Hawai Pizza")
print(g)


def name(name):
    geh = name.split()
    foh = [word + str(len(word)) for word in geh]
    return foh

print(name("Hawaii Pizza"))


def remove_orders(sii):
    listt = sii.split(",")
    listt.pop(0)
    listt.pop(-1)
    io = "".join(n + "," for n in listt)
    return io[:-1]

print(remove_orders("1,2,3,4,5"))


def food_menu(list_of_foods=[]):
    indexed = []
    for i, item in enumerate(list_of_foods):
        indexed += [f"{(i +1)}.{item}" ]
    goh = ", ".join((indexed))
    return goh

print(food_menu(["Hawaii Pizza", "Diablo Pizza"]))


















# Write a function reverse_words(sentence) that takes a sentence like "I love Python" and returns "Python love I".

def reverse_words(sentence):
    words = sentence.split()
    new = " ".join(words[::-1])
    word = new.split()
    i = "".join(word[0]+"." for word in word)
    return i[:-1]

sentence = "I love Python"
print(reverse_words(sentence))


# Write a function parse_csv(line) that takes a string of comma-separated values like "apple,banana,cherry" and returns a list ["apple", "banana", "cherry"], with its elements in reverse order.

def parse(stro):
    list = []
    for word in stro.split(','):
        list.append(word)
    return list [::-1]
stro = "I,love,Python,meow"
print(parse(stro))


# Write a function obfuscate_email(email) that replaces the part before @ with *** but keeps the domain.


def email(email):
    new_email = email.split("@")
    domain = new_email[1]
    hidden_e = ("***" + domain)
    return hidden_e

print(email("janedoe@yahoo.com"))

# Write a function swap_name(full_name) that takes a name like "John Doe" and returns "Doe, John".

def swap(full_name):
    name, surname = full_name.split(" ")
    return surname+", "+name

print(swap("Jane Doe"))


# Challange string manipulation
# 1

def one(nu):
    juh = "".join(n[0] for n in nu.split())        # split() turns "Jane Doe" into: ["Jane", "Doe"] , without it each character is a "word " for n[0]
    return (f"{juh}")

print(one("Jane Doe"))

#2
def co(i):
    return len(i.split())   # split automatically works on empty spaces


print(co("Jane Doe Federica De la Plaja Con Jugador De Los Marquinos"))

#3

def re(ios):
    tos = ios.split()
    return tos[::-1]

print(re("How about now we get it"))


#4

def tul(stroo):
    tos = stroo.split(",")
    return tos

print(tul("How,about,now,we,get,it"))

#5

def slash(stros):
    tos = stros.replace(" ", "-")
    return tos

print(slash("How about now we get it"))

#6

def ma(sts):
    mail, domain = sts.split("@")
    return "***" + "@" + domain

print(ma("jilldoe@yahoo.com"))

#7

def format(n):
    listo = n.split()
    li = listo[-1]
    listo.pop()
    full = " ".join(listo)                      # standard for transforming the strings in a list to a big string
    return li + ", " + full

print(format("John Ronald Reuel Tolkien"))

#8

def strou(stroo):
    tt = stroo.split()
    no_space = []
    for word in tt:
        clean = word.strip()                     # clean is a str that ensures no_space takes individual words as elements, instead of single letter strings
        if clean:                      # if clean is a conditional statement, that skips empty spaces
            no_space.append(clean)
    word_toh = " ".join(no_space)
    return word_toh

print(strou("    John    Ronald    Reuel    Tolkien   "))

def strou2(stroo):
    tt = stroo.split()
    return " ".join(tt)

print(strou("    John    Ronald    Reuel    Tolkien   "))

#9

def gener(stah):
    list_content = stah.split()
    duh = "".join(n[0] for n in list_content if n[0].isupper())
    return duh

print(gener("the European Central Bank"))



#10

def pali(sss):
    cont = sss.split()
    cont3 = "".join(cont).lower()
    cont4 = cont3[::-1]
    if cont3 == cont4:
        return True

print(pali("Never odd or even"))
print(pali("Nevert even"))

def pali2(sss):
    cont = sss.replace(" ", "").lower()
    cont2 = cont[::-1]
    if cont2 == cont:
        return True

print(pali2("Never odd or even"))
print(pali2("Nevert even"))


# Conditional statements are especially useful when you want to filter out unwanted values like empty strings, zeros, None, or False
#1

words = ["apple", "", "banana", "", "", "cherry"]

#words2 = words.pop(1)
#print(words)

words3 = [word for word in words if word]
print(words3)

#2

numbers = [0, 5, 0, -3, 7, 0]
count = 0
for word in numbers:
    if word:
        count +=1
print(count)

#3

values = [10, None, 5, None, 0, 3]

valid = [word for word in values if word]
print(valid)

valid_int = [word for word in values if isinstance(word, int)]
print(valid_int)

#4

lines = ["Hello", "   ", "World", "", "Python  "]

def ii(list_l):
    rer = list( word.strip() for word in list_l if word.strip() )
    return rer

print(ii(lines))

#ii = lambda lst: [w.strip() for w in lst if w.strip()]

#5

s = "   The   quick   brown    fox   "
#uii = []
#for word in s.split():
#   uii.append(word)
uii = s.split()

print(uii)

#6

items = ["Apple", "", 0, None, "Banana", [], {}, "Cherry", False, "  "]

# items_real = [word for word in items if (word and (word if not isinstance(word, str) else word.strip()))]

ypru = []

for item in items:
    if isinstance(item, str):
        if item.strip():
            ypru.append(item.strip())
    elif item:
        ypru.append(item)
print(ypru)


filtered = [item for item in items if item]
resulto = [item.strip() if isinstance(item, str) else item
          for item in filtered
          if not (isinstance(item, str) and not item.strip())]
print(resulto)

#7

nested_items = [
    ["Apple", "", None, "Banana"],
    [],
    ["Cherry", "  ", "Date", 0],
    [False, "Egg", "", "  "]
]

final_list = []
for item in nested_items:
    for thing in item:
        if isinstance(thing, str):
            if thing.strip():
                final_list.append(thing.strip())
 #       else:
 #           if thing:
  #               final_list.append(thing)

print(final_list)


final_list2 = []
for item in nested_items:
    cleaned = []
    for thing in item:
        if isinstance(thing, str):
            if thing.strip():
                cleaned.append(thing.strip())
    if cleaned:
        final_list2.append(cleaned)
print(final_list2)


