def gtfo():
    print("Can anybody hear me ?")

gtfo()

greet = lambda : print("F there!")

greet()

x = 10

def multiply_by_two():
    pass

print(multiply_by_two())

y = 2
def multiply_two():
    return x * y

print(multiply_two())

# parameters, arguments

def multiplication_of_two(i, j):
    return i * j

print(multiplication_of_two(10, 20))

def greet( name = "Anonymous" ):
    print(f"Hello {name}")
greet()
greet("Jean")


def calculate_area(radius):
    pi = 3.14159  # local variable
    area = pi * radius * radius
    print(f"The area of a circle with radius {radius}m is {area}m")

calculate_area(10)


def compute_bmi(weight, height):
    bmi = weight / height ** 2

    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'


    return weight, height, result
    print("Oops!")

print(compute_bmi(63, 1.74))

my_weight, my_height, my_bmi = compute_bmi(50, 175)




def greet(name):
    print("Hello, " + name + "!")
    return

assert greet("Jerry")==None



def get_available_books(books):
    available_titles = ""
    for book in books:
        if book['stock'] > 0:
            available_titles += f"{book['title']} \n"
    return f"The following books are available: {available_titles}"

books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "stock": 0
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "stock": 5
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "stock": 3
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "stock": 2
    }
]

available_books_message = get_available_books(books)
print(available_books_message)
print(type(available_books_message))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
        else:
            return True

print(is_prime(2564645657))

def main(name):
    def greeto(text):
        return f"Hello {name}! {text}"
    return greeto("Have a great day!")

print(main("Jean"))


def calculate_final_price(price, vta_procent):

    def calculate_vta(price):
        return price * vta_procent / 100

    vta = calculate_vta(price)
    final_price = price + vta
    return final_price

print(calculate_final_price(150,25))

def summ_3(a, b, c):
    return a + b + c
print(summ_3( 4, 8, 9))


def hotel_reservation ( name, nights, price_per_night):
    total_price = price_per_night * nights
    print(f"The hotel reservation for {name} is a total of {total_price}, for {nights} nights.")

hotel_reservation( "Jane Austen", 15, 25)
hotel_reservation( "Billy Jean", 30, 18)

# lamda
aduna_lamda = lambda x, y: x + y
print(aduna_lamda(5, 10))
print(aduna_lamda(5, 11))


numbers_list = [4, 8, 11, 24, 40]
squared = map(lambda num: num ** 2, numbers_list)
print(list(squared))

squared = [num ** 2 for num in numbers_list]
print(squared)

divisible_list = filter(lambda num: num % 2 == 0, numbers_list)
print(list(divisible_list))

pare = list(map(lambda num : num % 2 == 0, numbers_list))
print(list(pare))

calc = list(filter(lambda x : x * 5 <= 25 and x % 2 == 0, numbers_list))
print(list(calc))


products = [{ "name" : "laptop", "price" : 5000 },
            { "name" : "mouse", "price" : 55 },
            { "name" : "desktop", "price" : 6000 },
            { "name" : "monitor", "price" : 500 }, ]

cheap = list(filter(lambda x : x["price"] < 1000, products))
item_cheap = [item["name"] for item in cheap]
print(f"Products cheaper than 1000 are: {', '.join(item_cheap)}")

sorte = sorted(numbers_list, key=lambda x:x**2, reverse=True)
print(sorte)


numbers = [ 12, 13, 18, 19, 27, 50]
sorto = sorted(numbers, key=lambda x : 0 if x % 2 == 0 else 1)
print(sorto)


students = [('Van Damme', 10),( 'Stalone', 9),('Arnold', 8)]
students_sorta = sorted(students, key=lambda x : x[0])  # first x : represents each student ; 2nd x : takes the grade; [0] takes 1st elem and s() orders
print(students_sorta)

# Decorators

def my_decorator(original_function):
    def new_func():
        print("Before the function")
        original_function()
        print("After the function")
    return new_func        #()  paratezele sunt pentru apelarea unei functii

@my_decorator     # replaces hello() with my_decorator(hello)
def hello():
    print("Hello")

hello()

def double_result(functionn):
    def neww_func():
        result = functionn()
        return result*2
    return neww_func

@double_result
def func_one():
    return 2

print(func_one())
# Organising operations

this_text = "Global text"
def log_into_terminal ():
    def fourth_function():
        print("Hello")
    fourth_function()
    print(this_text)
    local_text = ("Local text")
    print(local_text)


log_into_terminal()

def another_fuction():
    log_into_terminal()
    return ("Another function")
print(another_fuction())


def factorial(n):
    if n < 0:
        return ("Factorial is not defined for negative numbers.")
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(-4))

def log_into_terminal2():
    return another_fuction

print(log_into_terminal2()())

def log_into_terminal3(message, number):
    print(f"Message recieved {message} {number}")

def function3():
    log_into_terminal3("from another function", 5)

function3()
log_into_terminal3("a new message", 3)

def greetings(name):
        if len(name) < 3:
            print(f"Hello {name}!")
        elif len(name) < 5:
            print(f"Shakalaka {name}!")
        elif len(name) < 10:
            print(f"Howdy {name}!")
        else:
            print(f"Whoops {name}!")

greetings("Alice")
greetings("Arandula")
greetings("Bob")
greetings("Michizukisanishiro")

# Generator

def generator(n):
    for n in range(n):
        if n % 2 == 0:
             yield n

list = list(generator(12))
print(list)

# Try_except

try :
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero")


def division(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    except ZeroDivisionError:
        print("You can't divide by zero")
    finally:
        print("What an insight!")

division(4, 5)
division(4, 0)




