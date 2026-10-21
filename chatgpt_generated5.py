#1



class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof !!! ")

Lis = Dog("Lis", 20)
Lis.bark()
Keo = Dog("Keo", 2)
Keo.bark()
Nina = Dog("Nina", 3)

#2

class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def info(self):
        print(f"{self.brand} {self.color} {self.year} ")

#3

class Book:
    def __init__(self, title, author, pages=100):
        self.title = title
        self.author = author
        self.pages = pages

    def lenght(self):
        if self.pages <= 100:
            print (f"{self.title} is a short book of {self.pages} pages. ")
        else:
            print (f"{self.title} is a long book of {self.pages} pages. ")

count_of_Monte_Cristo = Book("Count of Monte Cristo", 'Alexander Dumas', pages=400)
count_of_Monte_Cristo.lenght()


#4

class Counter:
    def __init__(self, value=0):
        self.value = value
    def inc(self):
        self.value += 1
    def dec(self):
        self.value -= 1
    def reset(self):
        self.value = 0
    def show(self):
        print(f"Current value is : {self.value}")


value1 = Counter()
value1.inc()
value1.inc()
value1.show()


# new batch
# 1

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        if self.grade >= 60:
            return "Passing"
        else:
            return "Failing"

Jean = Student("Jean", 90)
print(Jean.is_passing())

#2


class Rectangle:
    def __init__(self, width, height):
         self.width = width
         self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rec1 = Rectangle(100, 110)
print(rec1.perimeter())

#3

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"{self.owner}'s current balance is {self.balance} ")

account_1 = BankAccount("Jean", 100)
account_1.deposit(100)
account_1.show_balance()

#4

class Timer:
    def __init__(self, seconds=0):
        self.seconds = seconds

    def add_seconds(self, x):
        self.seconds += x

    def reset(self):
        self.seconds = 0

    def show_time(self):
        print(f"{self.seconds} seconds remaining")

c1 = Timer()
c1.add_seconds(100)
c1.show_time()


#5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def introduce(self):
        print(f"{self.name} is {self.age} years old and has a salary of {self.salary} USD")

pers1 = Person("John", 18)
emp1 = Employee("John", 18, 1000)
emp1.introduce()

#6

class LibraryBook:
    def __init__(self, title, available=True):
        self.title = title
        self.available = available

    def borrow(self):
        if self.available:
            print(f"{self.title} is available")
            self.available = False
        elif not self.available:
            print(f"{self.title} is not available")

    def return_book(self):
        if self.available:
            print(f"{self.title} is already present in the library")
        elif not self.available:
            print(f"{self.title} has been returned ")
            self.available = True

book1 = LibraryBook("1984", True)
book1.borrow()
book1.return_book()
book1.return_book()

#7

class ShoppingCart:
    def __init__(self, list_of_items):
        self.list_of_items = list_of_items

    def add_item(self, item):
        self.list_of_items.append(item)

    def remove_item(self, item):
        self.list_of_items.remove(item)

    def show_items(self):
        for item in self.list_of_items:
            print(item)

cart1 = ShoppingCart(['eggs', 'milk'])
cart1.add_item('cheese')
cart1.show_items()

#8

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def to_kelvin(self):
        return (self.celsius + 273)


temp1 = Temperature(27)
print(temp1.to_fahrenheit())
print(temp1.to_kelvin())

#9

class GameCharacter:
    def __init__(self, name, health, attack_power, alive=True):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.alive = alive

    def attack(self, other_character):
        if not other_character.alive:
            return

        other_character.health -= self.attack_power

        if other_character.health <= 0:
            other_character.health = 0
            other_character.alive = False

    def show_health(self):
        print(f"{self.name}'s current health is {self.health}")

    def show_alive(self):
        if self.alive:
            print(f"{self.name} is alive")
        elif not self.alive:
            print(f"{self.name} is not alive")

bill = GameCharacter('Bill', 100, 60)
bob = GameCharacter('Bob', 50, 150)
bill.attack(bob)
bob.show_health()
bob.show_alive()

#10


class Logger:
    def __init__(self, name, list):
        self.name = name
        self.list = list

    def log(self, message):
        self.list.append(message)
        print(f"{message} has been stored")

    def show_logs(self):
        if self.list == []:
            print("No logs")
        elif self.list != []:
            print(self.list)

    def clear_logs(self):
        self.list = []

log_batch = Logger("Bills", ["electricity 05"])
log_batch.show_logs()
log_batch.log("electricity 06")
log_batch.show_logs()
log_batch.clear_logs()
log_batch.show_logs()

#11

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_price(self):
        inventory_price = 0
        for item in self.items:
            inventory_price = inventory_price + item.price
        print(f"Inventory's current price is {inventory_price}")

book = Item("book1", 100)
laptop = Item("laptop", 10000)
my_basket = Inventory([book, laptop])
my_basket.calculate_price()


#12

class User:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

class Account:
    def __init__(self, user, balance):
        self.user = user
        self.balance = balance

    def transfer(self, other_account, amount):
        if self.user != other_account.user:
            raise ValueError("You can only transfer between your own accounts")
        if self.balance < amount:
            print ("Insufficient balance")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred {amount} from {self.user.name} to {other_account} succesfully"
                  f"Your balance is now {self.balance}")


# 3rd batch
#1

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __str__(self):
        return f"{self.title} (Rating: {self.rating})"

movie1 = Movie("Inception", 9)
print(movie1)


#2
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# circle1 = Circle(2)
# print(circle1.area())
# circle1.radius = 10
# print(circle1.area())

# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         self._radius = value
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# circle1 = Circle(2)
# print(circle1.area())
# circle1.radius = 10
# print(circle1.area())

# import math

# class Circle:
#      def __init__(self, radius):
#          self._radius = radius
#
#      @property
#      def radius(self):
#          return self._radius
#
#      @radius.setter               # with a setter the property becomes modifiable, without it's read only
#      def radius(self, value):
#          if value < 0:
#              raise ValueError("Radius cannot be negative")
#          self._radius = value
#
#      def area(self):
#          return math.pi * self._radius ** 2
#
#
# c1 = Circle(-2)
# print(c1.area())
# print(c1.radius)
# c1.radius = 1

import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def area(self):
        return math.pi * self._radius ** 2


c1 = Circle(2)
print(c1.radius)
print(c1.area())

#3


class Counter:
    def __init__(self, value=0):
        self.value = value
    def inc(self):
        self.value += 1
        if self.value > 100:
            print("Maximum value (100) reached")
            self.value = 100
    def dec(self):
        self.value -= 1
        if self.value < 0:
           print("Minimum value (0) reached")
           self.value = 0
    def reset(self):
        self.value = 0
    def show(self):
        print(f"Current value is : {self.value}")


#4

class Player:
    player_count = 0
    def __init__(self, name):
        self.name = name
        Player.player_count += 1

    def __del__(self):
        Player.player_count -= 1

#5

class Engine:
    def __init__(self, model):
        self.model = model

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

#6

class User:
    def __init__(self, username):
        if len(username) < 5:
            raise ValueError("Username cannot be less than 5 characters")
        self.username = username

#7

class Builder:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        return self

    def build(self):
        return self.items


b11 = Builder()
chain = b11.add('block1').add('block2').add('block3').build()
print(b11.build())
print(chain)

#8

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# class Shape:
#     def area(self):
#         raise NotImplementedError("All shapes must implement area()")

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):                         # never give an attribute the same name as a method. Like self.area
        return (self.side1 * self.side2) * self.side3

class Rectangle(Shape):
    def __init__(self, sides1_3, sides2_4):
        self.sides1_3 = sides1_3
        self.sides2_4 = sides2_4

    def area(self):
        return self.sides1_3 * self.sides2_4


def print_area(shape: Shape):                   # example of usage for Shape idea and polymorphism
    print(shape.area())

shapes = [
    Triangle(1, 2, 3),
    Rectangle(4, 5)
]

for s in shapes:
    print_area(s)

#9

class BankAccount:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
        self.history = []

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Amount can't be greater than your account's balance")
        self.balance -= amount
        self.history.append("-")
        self.history.append(amount)

    def deposit(self, amount):
        self.balance += amount
        self.history.append("+")
        self.history.append(amount)

    def statement(self):
        print(f"Here is the history of transactions: {self.history}\n"
              f"Current balance: {self.balance}")

account1 = BankAccount("John", 100)
account1.withdraw(100)
account1.deposit(200)
account1.statement()


#10

class Weapon:
    def __init__(self, damage):
        self.damage = damage

class Character:
    def __init__(self, name, health, attack_power, weapon):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapon = weapon

    def attack(self, other):
        other.health -= self.attack_power + self.weapon.damage


sword = Weapon(5)

hero = Character("Hero", 100, 10, sword)
enemy = Character("Enemy", 80, 8, sword)

hero.attack(enemy)
print(enemy.health)


#11


class Circle:
    def __init__(self, radius, thickness):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
        self._thickness = thickness

    @property
    def radius(self):
        return self._radius

    @property
    def thickness(self):
        return self._thickness

    def define_radius(self, value):
        self._radius = value

    def define_thickness(self, value):
        self._thickness = value



#12


class Product:
    def __init__(self, name, price):
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price

class Cart:
    def __init__(self, products=None):
        self.products = products if products else []

    @property
    def cost(self):
        return sum(product.price for product in self.products)

    def add_product(self, product):
        self.products.append(product)
        self.cost += product.price
        print(
            f"{product.name} has been added for a cost of {product.price}. "
            f"The cart cost is now {self.cost}."
        )

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            self.cost -= product.price
            print(f"{product.name} has been removed from the cart.")
        else:
            print("Product not found in cart.")

    def clear_cart(self):
        self.products.clear()
        self.cost = 0
        print("Your cart has been cleared.")


class User:
    def __init__(self, name, balance, cart):
        self.name = name
        self.balance = balance
        self.cart = cart

    def checkout(self):
        if self.cart.cost > self.balance:
            print("Insufficient balance.")
            return
        if self.cart is None:
            raise ValueError("Cart can't be empty")

        self.balance -= self.cart.cost
        product_names = [product.name for product in self.cart.products]

        print(
            f"Thank you for shopping with us! "
            f"You have purchased {product_names} for {self.cart.cost}. "
            f"Your balance is now {self.balance}."
        )

        self.cart.clear_cart()



# 4th batch
#1


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self._isbn = isbn

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return f"{self.title} {self.author}"

b1 = Book("Book Title", "Author", "132")
print(b1.isbn)
b1.title = "Psychonauts"
print(b1)

#2

class Temperature:
    def __init__(self, celsius):
        if celsius < -273.15:
            raise ValueError("Temperature cannot go under -273.15 Celsius degrees")
        self._celsius = celsius

    def to_fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


#3

class Animal:
    @abstractmethod
    def speak(self):
        print("some sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("woof")


a1 = Animal()
a1.speak()
a2 = Dog()
a2.speak()


#4

class School:
    def __init__(self, name, students_count=0):
        self.name = name
        self.students_count = students_count

    def get_students_count(self):
        return self.students_count

#5

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width cannot be negative or zero")
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height cannot be negative or zero")
        self._height = value

    def area(self):
        return self._width * self._height


#6

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.battery = battery

    def use(self, minutes):
        remaining_battery = self.battery.capacity - (minutes)
        if remaining_battery <= 0:
            raise ValueError("Battery capacity cannot be less than 0")
        self.battery.capacity = remaining_battery
        return "Battery is now " + str(self.battery.capacity)

#7

class PaymentMethod:
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.amount = amount




