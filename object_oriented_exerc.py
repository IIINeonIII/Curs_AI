
+# Procedural programming

lst = [2,5,8]
for x in lst:
    results = [x*2 for x in lst]
print(results)

# Functional programming  ( map, filter, reduce )

results2 = list(map(lambda x : x * 2, lst))
print(results2)

def x(num):
    num2 = list(map(lambda x : x*2, num))
    return num2

num = [3,7,10]
print(x(num))

# OOP  - an object has a status ( values saved internally ), contains data, and has specific methods that apply to it
# methods, attributes, class constructor, self

class MyName:
    pass

class Car:                  # the blueprint class
    acceleration = 10       # general class attributes
    wheels = 4

    def __init__(self, registration_number, mileage):               # the Constructor : a special function that initialises initial values
        self.registration_number = registration_number     # instance attribute
        self.in_motion = False
        self.speed = 0

    def drive(self):                     # a method, that can modify an attribute, which can be used anytime
        self.in_motion = True

    def accelerate(self):
        self.speed += self.acceleration

    def stop(self):
        self.in_motion = False
        self.speed = 0

my_car_Audi = Car("B-123-LMN", 1000)      # an object belonging to the class Car, being an instance of it

my_car_Audi.drive()
print(my_car_Audi.in_motion)

my_car_Audi.accelerate()
my_car_Audi.accelerate()

print(my_car_Audi.speed)

my_car_Audi.stop()
print(my_car_Audi.in_motion)

# Bank Account

class BankAccount:
    def __init__(self, name, balance):
        self.name = name                     # this line, stores the name within the object
        self.balance = balance

    def show_balance(self):
        print(f'{self.name} | balance: {self.balance} USD')

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} USD have been deposited. The new sold is {self.balance} USD. ')

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f'{amount} USD have been withdrawn. The new sold is {self.balance} USD. ')

account1 = BankAccount("Billy Jean", 1000)
account1.show_balance()
account1.deposit(100)
account1.withdraw(100)
account1.withdraw(2000)

# Favourite movie

class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating
        self.is_in_top = self.rating > 8.5

    def description(self):
        print(f'{self.title} | year: {self.year} | rating: {self.rating}')

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.is_in_top = self.rating > 8.5
        print(f'The rating of the movie {self.title} has been updated to {self.rating}.')

    def check_top_status(self):
        if self.is_in_top:
            print(f'The movie "{self.title}" has a top rating of {self.rating}.')
        else:
            print(f'The movie "{self.title}" does not have a top rating.')


Inception = Movie("Inception", 1990, 9.0)
Inception.description()
Inception.check_top_status()
Inception.update_rating(8.2)
Inception.check_top_status()



class Calculator:
    def __init__ (self):
        self.total = 0

    def add(self, num):
        self.total += num

    def sub(self, num):
        self.total -= num

    def multiply(self, num):
        self.total *= num

    def divide(self, num):
        if num == 0:
            raise ZeroDivisionError
        else:
            self.total /= num

    def show(self):
        print(f'The total is: {self.total}')



c1 = Calculator()
c1.add(2)
c1.show()
c1.multiply(20)
c1.divide(2)
c1.show()


# Employee

class Employee():
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = (f"{first_name}.{last_name}@company.com").lower()


    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



employee1 = Employee("Ion", "Ion", 50000)
employee2 = Employee("Ion", "Ionescu", 60000)

print(employee1.raise_amount)
print(employee1.email)

employee1.apply_raise()
print(employee1.pay)
employee1.apply_raise()
print(employee1.pay)
employee2.apply_raise()
print(employee2.pay)


class Employee2():
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = (f"{first_name}.{last_name}@company.com").lower()


    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount



employee1 = Employee2("Vasile", "Vasilica", 50000)
employee2 = Employee2("Vasilica", "Vasilescu", 60000)

Employee2.set_raise_amount(1.10)

employee2.apply_raise()
print(employee2.pay)


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_text(cls, text):      # this class method creates a new object Date, through Factory method
        year, month, day = map(int, text.split('-'))     # map in this case, turns the split results into 'int'
        return cls(year, month, day)


d = Date.from_text('1999-12-31')
print(d.year)



# Static methods ( no self / cls )
from datetime import datetime

class Employee3:
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = (f"{first_name}.{last_name}@company.com").lower()


    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @staticmethod
    def is_workday(day):
        return day.weekday() < 6



today = datetime(2025, 11, 2)
wednesday = datetime(2025, 11, 5)

print(Employee3.is_workday(today))
print(Employee3.is_workday(wednesday))


# Inheritance in OOP

class Employee():
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = (f"{first_name}.{last_name}@company.com").lower()


    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.15

    def __init__(self, first_name, last_name, pay, prog_language):
       super().__init__(first_name, last_name, pay)
       self.prog_language = prog_language

developer1 = Developer("Ben", "Dover", 50000, prog_language="Pascal")
print(developer1.email)



# Vehicle exercise

class Vehicle():
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def description(self):
        return f"{self.brand} {self.model}, year {self.year}, priced {self.price}."

    def how_old(self, current_year):
        return f"Model is {current_year - int(self.year) } years old"

    def apply_discount(self):
        self.price = int(self.price * 0.95)

class Car(Vehicle):
    def __init__(self, brand, model, year, price, nr_doors, fuel_type):
        super().__init__(brand, model, year, price)
        self.nr_doors = nr_doors
        self.fuel_type = fuel_type

    @property       # built-in decorator that turns the method into an attribute, accessible without ()
    def is_electric(self):
        return self.fuel_type.lower() == "electric"

    def apply_discount(self):
        self.price = int(self.price * 0.90)

class Truck(Vehicle):
    def __init__(self, brand, model, year, price, cargo_load):
        super().__init__(brand, model, year, price)
        self.cargo_load = cargo_load

    def transport_cost(self, nr_km):
        return int(self.cargo_load) * nr_km * 0.5

    def apply_discount(self):
        self.price = int(self.price * 0.92)

class Bus(Vehicle):
    def __init__(self, brand, model, year, price, nr_seats):
        super().__init__(brand, model, year, price)
        self.nr_seats = nr_seats

    def luxury(self):
        return self.nr_seats > 40 and self.price > 100000

    def apply_discount(self):
        self.price = int(self.price * 0.94)

class Manager():
    def __init__(self, name, vehicles = None):
        self.name = name
        self.vehicles = vehicles if vehicles is not None else []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def show_vehicles(self):
        print(f"The vehicles of manager {self.name} are:")
        for vehicle in self.vehicles:
            print(vehicle.description())

    def discount_all(self):
        for vehicle in self.vehicles:
            vehicle.apply_discount()


car = Car("Tesla", "Model 3", 2023, 40000, 4, "electric")
car2 = Car("BMW", "Model 2", 2023, 40000, 4, "gasoline")
truck = Truck("Volvo", "FH16", 2020, 80000, 20000)
bus = Bus("Mercedes", "Tourismo", 2019, 120000, 45)

print(truck.how_old(2025))

manager = Manager("Arisu")
manager.add_vehicle(car)
manager.add_vehicle(truck)
manager.add_vehicle(bus)
manager.show_vehicles()


print("\nBefore discounts:")
manager.show_vehicles()

manager.discount_all()

print("\nAfter discounts:")
manager.show_vehicles()

print(bus.luxury())
print(truck.transport_cost(40))
print(car.is_electric)
print(car2.is_electric)