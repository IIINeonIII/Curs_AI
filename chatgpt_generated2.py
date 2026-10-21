# 1

# value = input("Enter a number: ")
# try :
#     value = int(value)
#     print(f"Value {value} is a valid integer " )
# except ValueError :
#         print("Invalid input")
# except TypeError :
#         print("Invalid input")

# 2

# filename = input("Enter a filename: ")
#
# try:
#     with open(filename, "r") as f:
#         content = f.read()
#         print("File contents:")
#         print(content)
#
# except FileNotFoundError:
#     print("Error: That file does not exist.")
#
# except PermissionError:
#     print("Error: You do not have permission to read this file.")
#
# except IsADirectoryError:
#     print("Error: That path is a directory, not a file.")
#


# 3

def division(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return None


print(division(2, 0))

# 4

dictionary = {'name': 'a',
              'age': 22,
              'b': 2, 'c': 3}

dictionary2 = {'name': 'a'}


def age(dictionary):
    try:
        return dictionary['age']
    except KeyError:
        return 'Value doesn\'t exist'


print(age(dictionary))
print(age(dictionary2))


# 5

def convert(a):
    try:
        float(a)
        return float(a)
    except ValueError:
        return 'Value cannot be converted'


print(convert(1))
print(convert('lol'))

# 6

list5 = ['eggs', 'cheese', 'butter', 'ham', 'water']


def ulu(list):
    try:
        return list5[4]
    except IndexError:
        return 'Index out of range'


print(ulu(list5))


# 7

def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return "Invalid"


print(safe_divide(1, 2))
print(safe_divide(1, 0))


# 8

def con(a):
    try:
        return int(a)
    except (ValueError, TypeError):
        pass

    try:
        return float(a)
    except (ValueError, TypeError):
        return 'Not a number'


print(con(1))
print(con("2.2"))

# 9

list7 = [1, 5, 8, 4.4, 10, 2]


def f(list7):
    result = 0
    for x in list7:
        try:
            result += x
        except TypeError:
            return 'Invalid element'
    return result


print(f(list7))

# 10


users = [
    {'user': 'John',
     'age': 22,
     'profile': 'yahoo',
     'email': 'john@yahoo.com'},
    {'user': 'Johnny',
     'age': 18,
     'profile': 'yahoo',
     'email': 'johnny@yahoo.com'},
]
# print("DEBUG print is:", print)
#
# def info(data):
#     print("DEBUG received:", data)
#     print("DEBUG global user:", globals().get("user"))
#     for item in data:
#         print("DEBUG item:", item, type(item))
#
#     try:
#         if isinstance(data, list):
#             return [user['email'] for user in data]
#         return data['email']
#     except (KeyError, TypeError):
#         return 'Invalid or missing field'
# print(info(users))


def info(data):
    print("DEBUG received:", data)

    try:
        if isinstance(data, list):
            result = [user['email'] for user in data]
            print("DEBUG computed result:", result)
            return result

        result = data['email']
        print("DEBUG computed result:", result)
        return result

    except Exception as e:
        print("DEBUG actual exception type:", type(e))
        print("DEBUG actual exception message:", e)
        return "Invalid or missing field"
print(info(users))


# 11

def safe_eval(expr):
    try:
        # Remove spaces
        expr = expr.replace(" ", "")

        # Determine operator
        for op in ['+', '-', '*', '/', '**']:
            if op in expr:
                parts = expr.split(op)
                if len(parts) != 2:
                    return "Invalid expression"

                a, b = parts
                a = float(a)
                b = float(b)

                if op == '+':
                    return a + b
                elif op == '-':
                    return a - b
                elif op == '*':
                    return a * b
                elif op == '/':
                    return a / b
                elif op == '**':
                    return a ** b

        return "Invalid expression"

    except (ValueError, TypeError, ZeroDivisionError):
        return "Invalid expression"


print(safe_eval(' 3 + 2'))
print(safe_eval('334 * 2'))

#12
lll = [ "1", "2"]
lll1, lll2 = lll
print(lll1)
print(lll2)

#13

llis = [ "1", "2", 3, 4, 8.0, 1]

def ff(lll):
    jeh = []
    for x in lll:
        try:
            x = float(x)  # test if it can be converted to a number
            jeh.append(x)
        except (ValueError, TypeError):
            jeh.append(None)
        return jeh

print(ff(llis))

#14

def calculator(a, operator, b):
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
        elif operator == '**':
            return a ** b
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid numbers"

print(calculator(2, '+', 8))
print(calculator(10, '*', 8))
print(calculator(30, '6', 8))


#15

def safe_run(func, *args):
    try:
        return func(*args)
    except (ZeroDivisionError, TypeError):
        return "Invalid function"

def divide(a, b):
    return a / b

print(safe_run(divide, 10, 2))   # 5.0
print(safe_run(divide, 10, 0))   # Invalid function
print(safe_run(len, 10))

#16

class SafeList:
    def __init__(self, items):
        self.items = items

    def get(self, index):
        try:
            return self.items[index]
        except IndexError:
            return 'Index out of range'

sak = SafeList([1, 2, 3])

print(sak.get(0))     # 1
print(sak.get(10))    # Index out of range
print(sak.items)


#17

def safe_merge(dict1, dict2):
    try:
        if not isinstance(dict1, dict) or not isinstance(dict2, dict):
            return ('Invalid input')
        for key in dict1:
             if key in dict2 and type(dict1[key]) != type(dict2[key]):
                 return ('Type mismatch')

        merged = dict1.copy()
        merged.update(dict2)
        return merged

    except Exception:
        return "Invalid input"

print(safe_merge({"a": 1}, {"b": 2}))
print(safe_merge({"a": 1}, {"a": "hello"}))
print(safe_merge(5, {"b": 2}))


#18



# def convert_list(values):
#     converted = []
#     try:
#         if isinstance(values, list):
#              for value in values:
#                   try:
#                        value = int(value)
#                        converted.append(value)
#                   except (ValueError, TypeError):
#                        converted.append(None)
#     except(TypeError, ValueError):
#         return "Invalid list"
#     return converted


def convert_list(values):
    if not isinstance(values, list):
        return 'Invalid input'
    converted = []
    for value in values:
        try:
            converted.append(int(value))
        except (ValueError, TypeError):
            converted.append(None)
    return converted




print(convert_list(['1', '2', '3', 'cat']))
print(convert_list(('1')))


#19

def safe_math(a, b, op):
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return 'Invalid input'

    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return "Division by zero"
            return a / b
        elif op == '%':
            if b == 0:
                return "Division by zero"
            return a % b
        elif op == '**':
            return a ** b
        else:
            return "Invalid operator"
    except Exception:
        return "Invalid number"



#20

def safe_eval2(expr):
    try:
        expr = expr.replace(" ", "")
        for op in ['+', '-', '**', '/', '*']:
            if op in expr:
                parts = expr.split(op)
                if len(parts) != 2:
                    return "Invalid expression"
                a, b = parts
                try:
                    a = float(a)
                    b = float(b)
                except (ValueError, TypeError):
                    return "Invalid expression"
                if op == '+':
                    return a + b
                elif op == '-':
                    return a - b
                elif op == '*':
                    return a * b
                elif op == '/':
                    if b == 0:
                        return ('Division by zero')
                    else:
                        return a / b
                elif op == '**':
                    return a ** b
                else:
                    return "Invalid expression"

    except (ValueError, TypeError):
        return "Invalid expression"

print(safe_eval2("3+5"))
print(safe_eval2("10 / 2"))
print(safe_eval2("8*abc"))
print(safe_eval2("4/0"))
print(safe_eval2("3++2"))


#21



def deep_get(dictionary, keys):
    try:
        current = dictionary
        for key in keys:
            current = current[key]   # walk deeper
        return current               # reached final value
    except (KeyError, TypeError):
        return "Missing key"




print(deep_get( {
    "user": {
        "profile": {
            "email": "abc@gmail.com"
        }
    }
}
,["user", "profile", "email"]))


print(deep_get({
    "user": {
        "profile": {
            "email": "abc@gmail.com"
        }
    }
}, ["user", "age"]))

#22



def deep_get2(list_of_dictionaries, keys):
    list_of_emails = []

    for dictionary in list_of_dictionaries:

        try:
            current = dictionary
            for key in keys:
                current = current[key]   # walk deeper
            list_of_emails.append(current)

        except (KeyError, TypeError):
            return "Missing key"
    return list_of_emails  # reached final value



print(deep_get2( [{
    "user": {
        "profile": {
            "email": "abc@gmail.com"
        }
    }
},
    {"user": {
        "profile": {
            "email": "dfg@gmail.com"
        }
    }
}]
,["user", "profile", "email"]))












