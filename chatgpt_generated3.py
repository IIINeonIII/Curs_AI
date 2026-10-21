#1


for i in range(1, 11):
    print(i)
    if i ==4:
        break

#2

for z in range(1, 11):
    if z ==5 or z ==8:
        continue
    print(z)

#3

def validate_age(age):
    if age <= 0:
        return 'Invalid age'
    elif age <=18:
        return 'Too young'
    else:
        return 'Access granted'

print(validate_age(18))
print(validate_age(0))
print(validate_age(28))

#4

for y in range(1, 21):
    if y % 3 == 0 or y % 5 == 0:
        continue
    if y == 17:
        break
    print(y)

#5

# def menu():
#     option = input("Press 1 to say Hello, press 2 to say hi, press 3 to quit: '"
#                    "Enter your option: ")
#     i = 0
#     while i < 3:
#          if option == '1':
#              print("Hello")
#              i +=1
#              continue
#          if option == '2':
#              print("Hi")
#              i+=1
#              continue
#          if option == '3':
#              print("Quit")
#              break


# def menu():
#     while True:
#         print("1 - Say Hello")
#         print("2 - Say Bye")
#         print("3 - Quit")
#
#
#         user_input = int(input("Enter your choice: "))
#         if user_input == 1:
#             print("Hello")
#         elif user_input == 2:
#             print("Bye")
#         elif user_input == 3:
#             print("Quit")
#             return
#         else:
#            print("Invalid input")





#6

def categorize(temp):
    if temp <= 0:
        return 'Freezing'
    if temp <= 20:
        return 'Cold'
    if temp <= 30:
        return 'Warm'
    else:
        return 'Hot'

print(categorize(18))


#7

def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return 'No even number'

print(find_first_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))


#8

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#
#     # Check odd divisors up to sqrt(n)
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# def first_prime(numbers):
#     for num in numbers:
#         if is_prime(num):
#             return num
#     return "No prime found"
#
# print(first_prime([4, 6, 8, 9, 11, 13]))
#






def is_prime(numbers):
    for n in numbers:
        if n < 2:
            continue
        if n == 2:
            return n
        if n % 2 == 0:
            continue

        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:    # this means NOT prime
                break
        else:
            # Only happens if inner loop never hit a break
            return n

    return "No prime found"

print(is_prime([4, 4, 7, 64, 7, 8, 9]))

print("---")

#9

def rrun(list_of_words):
    output = []
    for word in list_of_words:

        # Stop condition first
        if word.lower() == "stop":
            break

        # Skip if word contains 'x'
        if "x" in word:
            continue

        print(word)
        output.append(word)

print(rrun(['cat', 'xenon', 'dog', 'stop', 'machine']))


#10

names = ["Tom", "Anna", "Bob", "STOP", "Lucy"]

for name in names:
    if name.lower() == "stop":
        break
    print(name)

#11

def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return 'No even number'

print(find_first_even([1, 20, 3, 4, 5, 6, 7, 8, 9]))

#12

words = ["apple", "box", "cat", "xray", "dog"]

for word in words:
    if 'x' in word:
        continue
    print(word)


#13

for i in range(1, 31):
    if i % 3 == 0:
        continue
    if i == 25:
        break
    if str(i)[-1] == '7':
        continue
    print(i)


#14

def first_long_word(words):
    for word in words:
        if len(word) >= 6:
            return word
    return 'No long word'

print(first_long_word(['apple', 'box', 'catcat', 'xray', 'dog']))

#15

nums = [3, 0, -2, 5, 0, 8, 100, 9, 10]

for num in nums:
    if num <= 0:
        continue
    if num == 100:
        break
    print(num)

#16

def first_long(words):
    for word in words:
        if word == 'end':
            break
        if any(c in word for c in ".,-"):
            continue
        if len(word) >= 8:
            return word
print(first_long(['apple', 'box', 'cat-cat', 'xray,,,,,,', 'dogdogdoggo']))


#17

def sum_until(numbers1):
    running_total = 0
    for number in numbers1:
        running_total += number
        if running_total > 10:
            break
    return running_total

print(sum_until([6, 1, 0, 5, 20]))


#18

def closest_to_zero(numbers):
    smallest = abs(numbers[0])
    for num in numbers:
        if num == 0:
            continue
        if num == 1:
            break
        if abs(num) < abs(smallest):
            smallest = abs(num)
    return smallest

print(closest_to_zero([6, 10, 0, 5, 20, 1]))


#19

def scan_matrix(matrix):
    sum = 0
    for row in matrix:
        for number in row:
            if number == 0:
                return sum            # return escapes both loops
            if number <= 0:
                continue
            sum += number
    return sum

print(scan_matrix([
  [3, 5, 0],
  [7, -2, 9],
  [4, 8, 6]
]))


#20

def menu_simulator5(commands):
    result = []
    for command in commands:
        if command == '2':
            continue
        elif command == '1':
            result.append("Processed ")
        elif command == '3':
            break
    return result

print(menu_simulator5(['1', '2','3']))

#21


def first_clean_word(words):
    for word in words:
        if word == "STOP":
            return "Process stopped"
        if len(word) <= 4:
            continue
        if any(char.isdigit() for char in word):
            continue
        if any(c in word for c in ".,!?;-_"):
            continue
        if str(word)[0] == 'x':
            continue
        return word
    return " No clean word"


print(first_clean_word(["he!!o", "xxcat", "apple", "STOP", "banana"]))

