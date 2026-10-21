# 1 - 6

class Student():
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    def grade_mean(self):
        total = sum(self.grades)
        return total / len(self.grades)

Taylor = Student("Taylor", [5,6,8,9,8])
print(Taylor.grade_mean())

# 1 - 9

class Temperature():
    def __init__(self, celsius):
        if celsius < -273:
            raise ValueError("Celsius cannot go under -273 degrees ")
        self.celsius = celsius
    def temperature_fahrenheit(self):
        fahrenheit = self.celsius * 9 / 5 + 32
        return fahrenheit

obs1 = Temperature(-27)
print(obs1.temperature_fahrenheit())


# 2 - 5

class Product():
    def __init__(self, name, price):
        self.name = name
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price = price


bread = Product("Bread", 10)
print(bread.price)

bread.price = 5
print(bread.price)


# 3 - 1

class Animal():
    def __init__(self, name):
        self.name = name
    def sound(self):
        return("some sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        return("woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        return("meow!")


animal = Animal("Animal")
print(animal.sound())
cat1 = Cat("Tibby")
print(cat1.sound())


# 3 - 9

class Vehicle():
    def __init__(self):
        self.speed = 0
        self.in_motion = False

    def show_speed(self):
        print(self.speed)

    def stop(self):
        self.in_motion = False
        self.speed = 0

class Nissan(Vehicle):
    def __init__(self, max_speed = 250):
        super().__init__()
        self._max_speed = max_speed

    @property
    def max_speed(self):
        return self._max_speed

    def accelerate(self):
        self.speed += 150
        if self.speed > self._max_speed:
            self.speed = self._max_speed
            print (f"Maximum speed of {self._max_speed} reached")
        self.in_motion = True


class Mercedes(Vehicle):
    def __init__(self, max_speed = 300):
        super().__init__()
        self._max_speed = max_speed

    @property
    def max_speed(self):
        return self._max_speed

    def accelerate(self):
        self.speed += 150
        if self.speed > self._max_speed:
            self.speed = self._max_speed
            print(f"Maximum speed of {self._max_speed} reached")
        self.in_motion = True


car1 = Mercedes()
car1.accelerate()
car1.accelerate()
car1.accelerate()

car2 = Nissan()
car2.accelerate()
car2.accelerate()
print(car1.speed)
print(car2.speed)

# car2.max_speed = 100


# 4 - 1

class Cat():
    def __init__(self, name):
        self.name = name
    def sound(self):
        return("Meow!")

class Goose():
    def __init__(self, name):
        self.name = name
    def sound(self):
        return("Honk!")

def animal_speak(animal):
    return animal.sound()

billy = Goose("Billy")
whiskers = Cat("Whiskers")

print(animal_speak(billy))       # the object becomes argument of the function
print(animal_speak(whiskers))


# 4 - 3

class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Employee(name={self.name}, age={self.age})"

class Department():
    def __init__(self, name, age, list_of_employees=None):
        self.name = name
        self.age = age
        self.list_of_employees = list_of_employees if list_of_employees is not None else []


billy = Employee("Billy", 18)
sarah = Employee("Sarah", 21)

finance = Department("Finance", 18, [billy, sarah])
print(finance.list_of_employees)




# 4 - 6

class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order():
    def __init__(self, name, list_of_products=None):
        self.name = name
        self.list_of_products = list_of_products if list_of_products is not None else []

    @property
    def cost(self):
        return sum(product.price for product in self.list_of_products)


cheese = Product("Cheese", 10)
butter = Product("Butter", 5)

order = Order("Billy's order", [cheese, butter])
print(order.cost)


# 5 - 1

class Person():
    def __init__(self, name):
        self.name = name

    def from_string(self, string):
        name, age = string.split(",")
        return name, int(age)

bob = Person("Bob")
print(bob.from_string("Bob,34"))





