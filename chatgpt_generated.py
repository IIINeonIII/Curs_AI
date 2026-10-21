#  The key= argument tells Python:
# “Before comparing the items, transform each item using this function.”
# So instead of comparing items directly, Python compares the result of the key function

#1

nums = [5, -1, 10, -3, 2]

nums2 = sorted(nums, key=abs)
print(nums2)
nums3 = sorted(nums)
print(nums3)

#2

words = ["apple", "hi", "zebra", "dog"]
ss = sorted(words, key=len)
print(ss)

#3

words = ["cat", "education", "strength", "queueing"]
vowels = ['a', 'e', 'i', 'o', 'u']

vow = sorted(words, key=lambda x: sum(1 for ch in x if ch in vowels))  # sorted sends all str from words in lambda and l stores it in x and ch checks the vowels, sum counts
print(vow)

#4

pairs = [(3, 10), (0, 2), (5, -1)]

ssss = sorted(pairs, key=lambda x: x[1])
print(ssss)


#5

products = [
    {"name": "Book", "price": 12},
    {"name": "Laptop", "price": 900},
    {"name": "Pen", "price": 2}
]

sorted_products = sorted(products, key=lambda x: x["price"])

#6

names = ["alice", "Bob", "claire", "dave"]

#iar = sorted(names, key=lambda x: x.isupper())

iar = sorted(names, key=lambda x: x.lower())
print(iar)

#7

nums = [5, 2, 9, 8, 7, 4]

sorted_nums = sorted(nums, key=lambda x: (x % 2, x if x%2 == 0 else -x))
print(sorted_nums)

#8

logs = [
    ("INFO", "System started"),
    ("ERROR", "File missing"),
    ("WARNING", "Low battery"),
    ("ERROR", "Crash detected")
]
priority_map = {"ERROR": 0, "WARNING": 1, "INFO": 2}
custom_priority = sorted(logs, key=lambda x: priority_map[x[0]] )
print(custom_priority)

#9

words = ["apple", "banana", "pear", "kiwi", "plum"]

sortoo = sorted(words, key=lambda x: x[-1])
print(sortoo)

#10

employees = [
    {"name": "Alice", "age": 30, "salary": 4000},
    {"name": "Bob",   "age": 30, "salary": 5500},
    {"name": "Cara",  "age": 22, "salary": 3800},
    {"name": "Dan",   "age": 40, "salary": 9000}
]

sorted_employees = sorted(employees, key=lambda x: x["age"] if x["age"] >=30 else x["salary"])
print(sorted_employees)

orted_employees2 = sorted(employees, key=lambda x: (x["age"], -x["salary"]))
print(orted_employees2)


#11

files = ["report.pdf", "image.jpeg", "script.py", "data.csv"]

sorted_files = sorted(files, key=lambda x: x.split(".")[1])
print(sorted_files)

#12

sentences = [
    "Hello worldooooooooo",
    "This is a test sentence",
    "Python is great"
]

count = sorted(sentences, key=lambda x: sum(1 for ch in x if ch == " "))
print(count)

#key=lambda s: len(s.split())

#13

data = [
    {"name": "A", "items": [1,2]},
    {"name": "B", "items": [4,5,6,7]},
    {"name": "C", "items": []}
]

longest = sorted(data, key=lambda x: len(x["items"]))
print(longest)

longest2 = max(data, key=lambda x: len(x["items"]))
print(longest2)

#14

students = [
    ("Alice", 90),
    ("Bob", 85),
    ("Clara", 90),
    ("Dave", 70)
]

sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
print(sorted_students)

#15

codes = ["a1b2", "xyz", "88", "abc123"]
sorted_codes = sorted(codes, key=lambda x: (len(x)))
print(sorted_codes)

sorted_codes = sorted(codes, key=lambda x: (sum(ch.isdigit() for ch in x), len(x)))
print(sorted_codes)
#16

people = ["Alice-1994", "Bob-1980", "Cara-2002"]
sorted_people = sorted(people, key=lambda x: x.split("-")[1])
print(sorted_people)

sorted_people = sorted(people, key=lambda x: int(x.split("-")[1]))

#17
import math

points = [(3,4), (1,1), (10,0), (0,0)]

sorted_points = sorted(points, key=lambda x: math.sqrt(x[0]**2 + x[1]**2))
print(sorted_points)

sorted(points, key=lambda x: x[0]**2 + x[1]**2)

#18

transactions = [
    ("USD", 20),
    ("EUR", 15),
    ("JPY", 3000),
    ("GBP", 10)
]

priority = {
    "EUR":0,
    "USD":1,
    "GBP":2,
    "JPY":3
}
sorted_transactions = sorted(transactions, key=lambda x: priority[x[0]])
print(sorted_transactions)

#19

words = ["hello", "banana", "abc", "aaaa", "Python"]

sorted_words = sorted(words, key=lambda x: len(set(x)))
print(sorted_words)

#20

data = [
    {"name": "A", "score": 90, "age": 20},
    {"name": "B", "score": 90, "age": 18},
    {"name": "C", "score": 80, "age": 25}
]

sorted_data = sorted(data, key=lambda x: (-x["score"], x["age"], x["name"]))
print(sorted_data)

#21

words = ["banana", "apple", "cherry", "orange", "grape"]

sorted_words = sorted(words, key=lambda x: x)
print(sorted_words)
vowels = ['a', 'e', 'i', 'o', 'u']
sorted_words2 = sorted(sorted_words, key=lambda x: 0 if x[0] in vowels else 1)
print(sorted_words2)

#22

nums = [4, 9, 3, 6, 7, 8, 12, 5]


from functools import cmp_to_key


def compare(a, b):
    # First: sort by divisibility by 3 (divisible numbers come first)
    a_div = a % 3 == 0
    b_div = b % 3 == 0

    if a_div and not b_div:
        return -1
    if b_div and not a_div:
        return 1

    # If both are divisible or both are not, sort numerically
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

sorted_nums = sorted(nums, key=cmp_to_key(compare))
print(sorted_nums)


sorted_nums2 = sorted(nums, key=lambda x: (x % 3 != 0, x))
print(sorted_nums2)


#23

nums = [4, 9, 3, 6, 7, 8, 12, 5, 15, 10]


#sorted_nums = sorted(nums, key=lambda x: (x % 2 == 0, x % 3 == 0))
#print(sorted_nums)


sorted_nums2 = sorted(nums, key=lambda x: (0 if x % 2 == 0 else 1 if x % 3 == 0 else 2, x))
print(sorted_nums2)

#24

words = ["banana", "fig", "apple", "kiwi", "cherry", "pear"]

sorted_words = sorted(words, key=lambda x: (len(x), x))
print(sorted_words)

#25

nums = [12, 39, 25, 47, 53, 18, 91, 60]

sorted_nums = sorted(nums, key=lambda x : (x%10))
print(sorted_nums)

#26

people = [
    ("Alice", 32),
    ("Bob", 17),
    ("Charlie", 25),
    ("Dave", 30),
    ("Eve", 17)
]

sorted_people = [x for x in sorted(people, key=lambda x: (x[1], x))]
print(sorted_people)

#27

items = ["hello", "sky", "education", "python", "queue"]

vowels = ['a', 'e', 'i', 'o', 'u']

sorted_items = sorted(items, key=lambda x: (sum(1 for x in x if x in vowels), x))
print(sorted_items)

#28

pairs = [(5, 2), (3, 1), (7, 1), (8, 3), (4, 2)]

sorted_pairs = sorted(pairs, key=lambda x: (x[1], -x[0]))
print(sorted_pairs)

#29

people = [
    ("Alice", 25),
    ("Bob", 17),
    ("Charlie", 32),
    ("Dave", 14),
    ("Eve", 25),
]

sorted_people = sorted(people, key=lambda x: (0 if x[1] <= 17 else 1 if 18 <= x[1] <=30 else 2, x[0]))
print(sorted_people)


#30
#Sort the list so that numbers divisible by 3 come first.
#If a number is divisible by 3, sort it by last digit.
#If a number is not divisible by 3, sort it by the number of vowels in the word (fewest vowels first).
#If multiple items have the same number of vowels or last digit, sort alphabetically by the word.
#Return the result as a new list using list comprehension around a sorted() call.



data = [
    ("apple", 12),
    ("banana", 9),
    ("cherry", 7),
    ("date", 18),
    ("fig", 5),
    ("grape", 15)
]

sorted_data = [x for x in sorted(data, key=lambda x: ( 0 if x[1] % 3 == 0 else 1, x[1] % 10 if x[1] % 3 == 0 else sum(1 for ch in x[0] if ch in vowels), x[0]))]
print(sorted_data)

