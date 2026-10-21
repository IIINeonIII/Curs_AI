'''
This file contains various exercises.
This is a Docstring.
'''
house_goods = [ {
    "object": "Fridge",
    " type" : "Electronics",
    "age" : 10 },
    {  "object": "Couch",
       " type" : "Furniture",
       "age" : 20 },
    { "object": "Laptop",
      " type" : "Electronics",
      "age" : 3 }
]

old_goods = ""
new_goods = ""
for house_good in house_goods:
    if house_good["age"] >= 5:
        old_goods = house_good
        print(f"Old goods are {house_good}")
    elif house_good["age"] <= 5:
        new_goods = house_good
        print(f"New goods are {house_good}")

# Min, max
print(max(house_goods, key=lambda x: x["age"]))

longest_name_item = max(house_goods, key=lambda x: len(x["object"]))
shortest_name_item = min(house_goods, key=lambda x: len(x["object"]))

print(longest_name_item["object"])
print(shortest_name_item["object"])

print(max(house_goods, key=len))

print(min(house_goods, key=lambda x: x.get("age"))["age"])

# abs, round
print(abs(len(longest_name_item["object"]) - len(shortest_name_item["object"])))

print(round(2.456, 1))



def text_into_integer(text):
     numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
        }
     for number, value in numbers.items():
         if number == text:
             return value
            #return numbers.get(text.lower)


#input_number = int(input(f"Introduce the number : "))

#for word, value in numbers.items():
#    if value == input_number:
#        print(f"The word for {input_number} is '{word}'.")
#        break
#else:
#     print(f"{input_number} is not in the dictionary")


print(text_into_integer("one"))
print(text_into_integer("five"))


def text_into_integer2(text):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }

    text = text.lower().strip()

    if text in numbers:
        return numbers[text]
    else:
        print(f"'{text}' is not a valid number word.")

text_into_integer2("one")
text_into_integer2("five")
text_into_integer2("seven")


print(sum([1, 5, 10]))

numberrs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
xl = sum( int(x) for x in numberrs)
print(xl)

numbs = ["1", "2", "3", "4", "5", "-6", "-7", "-8", "-9"]
numbss = sum ( int(x) for x in numbs if int(x) > 0 )
print(numbss)
# complex nr

print(complex(1,2))

z = 1 + 2j
print(z.real)

import math

print(math.log10(10000))

print(math.log(1))

import random

i = random.randint(1,10)
print(i)

choice = random.choice(["one", "two", "three", "four", "five"])
print(choice)

# Project Mrs Halpert

def odd_or_even(num):
    if num % 2 ==0:
        return "even"
    else:
        return "odd"

print(odd_or_even(3))

def basic_operations(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error, division by zero is not possible."
        else:
            return num1 / num2
    else:
        return "Operation not available."

print(basic_operations("add", 1, 2))
print(basic_operations("subtract", 1, 2))
print(basic_operations("divide", 1, 0))
print(basic_operations("logaritm", 1, 2))



numbers = [1, 9, 56, 25, 2, 7, 138]


def even_or_odd_extended(numbers):
    if numbers == []:
        return [], []
    odd_numbers = []
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    sorted_even = sorted(even_numbers)
    sorted_odd = sorted(odd_numbers, reverse=True)

    return sorted_even, sorted_odd

even_list, odd_list = even_or_odd_extended(numbers)

print("Even numbers (ascending):", even_list)
print("Odd numbers (descending):", odd_list)


def odd_or_even_sort(numbers):
    if not numbers:
        return [], []
    even_list = sorted([number for number in numbers if number % 2 == 0])
    odd_list = sorted([number for number in numbers if number % 2 == 1], reverse=True)
    return even_list, odd_list

# 1:31  13/10/25


def total_points(results):
    total = 0
    for result in results:
        x, y = map(int, result.split(":"))
        if x > y:
            total += 3
        elif x == y:
            total += 1
        else:
            total += 0
    return total

results = ["1:0", "2:3", "3:0", "4:4"]
print(total_points(results))

def largest_number(a,b,c):
    return  max((a*b*c), (a+b)*c, a*(b+c), a+b+c)

print(largest_number(1,2,3))
print(largest_number(1,1,2))
print(largest_number(10,2,3))


def index(list, number):
    if number > len(list) or number < 1:
        return -1
    i = list[number]
    return i ** number


print(index([1,2,3,4,5,6],3))
print(index([1,2,3,4,5,6],8))


def index2(list, number):
    try:
        return list[number]**number
    except:
        return -1

def index3(list, number):
    return list[number]**number if number > 0 and number < len(list) else -1

print(index3([1,2,3,4,5,6],8))

def quarter_of_the_year(month):
    '''

    :param month: the month of the year
    :return: the quarter of the year
    '''
    if 0 < month < 4 :
        return 1
    elif 3 < month < 7 :
        return 2
    elif 6 < month < 10 :
        return 3
    elif 9 < month < 12 :
        return 4
    else:
        return "Out of range"

print(quarter_of_the_year(3))
help(quarter_of_the_year)

def century(year):
     i = year // 100.000000000001 + 1
     return int(i)

print(century(1573))
print(century(2000))
print(century(1))


def form_the_minimum(list):
    unique = set(list)
    unique_sorted = sorted(unique)
    return int("".join(str(d) for d in unique_sorted))

list =[1,2,2,3,0]
print(form_the_minimum(list))

def form_the_minimum2(list):
    unique = set(list)
    unique_sorted = sorted(unique)
    i = ""
    for d in unique_sorted:
        i = i + str(d)

    return int(i)

print(form_the_minimum2(list))







