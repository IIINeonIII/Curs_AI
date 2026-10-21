#1

words = ['dog', 'cat', 'horse', 'crow', 'duck', 'elephant']

sorted_words = sorted(words, key=lambda word: (str(word)[-1], word))
print(sorted_words)

#2

def sum_of_positives(nums):
    sum = 0
    for num in nums:
        if float(num) < 0:
            return ("List has negative numbers. The sum so far is " + str(sum))
        if float(num) == 0:
            continue
        sum += float(num)
    return sum

nums1 = [12, '39', 25, 47, 53, 18, 0, 91, 60]
print(sum_of_positives(nums1))
nums2 = [12, '39', -25, 47, 53, 18, 0, 91, 60]
print(sum_of_positives(nums2))

#3

def clean_username(usernames):
    for username in usernames:
        if any(x.isdigit() for x in username):
            continue
        if any(c in username for c in ".,!?;-_@"):
            continue
        if str(username)[0] == 'x':
            continue
        return username
    return "No valid username"

usernames = ['Apokkal!!pti&', '$o!!rz', 'Kitty-katty', 'llegolas@', 'xbob', 'bill', 'jen']
print(clean_username(usernames))

#4

products = [
    ("apple", 3.50),
    ("banana", 2.10),
    ("cake", 10.99),
    ("milk", 2.10),
    ("xylophone", 9.99)
]

sorted_products = sorted(products, key=lambda product: (0 if product[1] < 3 else 1, len(product[0]) if product[1] < 3 else product[1], product[0]  ))
print(sorted_products)

#5

def get_safe_values(dicts, keys):
    list_of_values = []
    for dict in dicts:
        try:
            current = dict
            for key in keys:
                try:
                     current = current[key]
                except KeyError:
                    continue
            list_of_values.append(current)

        except:
            continue
    return list_of_values



#6

expressions = ["10/2", "5*6", "4/0", "abc+3"]

def safe_eval3(expression):
    try:
        expr = expression.replace(' ','')
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
               try:
                   if op == '+': return a + b
                   if op == '-': return a - b
                   if op == '*': return a * b
                   if op == '/': return a / b
                   if op == '**': return a ** b
               except (ZeroDivisionError):
                   return "Division by zero"
    except (ValueError, TypeError):
        return "Invalid expression"
    return get_safe_values(expression)


def safe_eval_list(expressions):
    return [safe_eval3(expr) for expr in expressions]


print(safe_eval_list(expressions))

#7

items = [
    ("apple", 12),
    ("watermelon", 5),
    ("kiwi", 5),
    ("banana", 30),
    ("xenon", 12),
    ("pear", 8)
]

vowels = ['a', 'e', 'i', 'o', 'u']

sorted_items = [x for x in sorted(items, key=lambda x: (0 if x[0][0] in vowels else 1, x[1] if x[0][0] in vowels else len(x[0]), x[0] ))]
print(sorted_items)

#8

def deep_safe_extract(dicts, key_paths, default):
    extracted = []
    for dict in dicts:
        value_found = False
        for path in key_paths:
            try:
                current = dict
                for key in path:
                    current = current[key]
                extracted.append(current)
                value_found = True
                break
            except (KeyError, TypeError):
                continue
        if not value_found:
             extracted.append(default)
    return extracted




#9

# def safe_first(expressions):
#     try:
#         expr = expressions.replace(' ','')
#         for op in ['+', '-', '**', '/', '*']:
#              if op in expr:
#                parts = expr.split(op)
#                if len(parts) != 2:
#                     continue
#                a, b = parts
#                try:
#                      a = float(a)
#                      b = float(b)
#                except (ValueError, TypeError):
#                     return "Invalid"
#                try:
#                    if op == '+': return a + b
#                    if op == '-': return a - b
#                    if op == '*': return a * b
#                    if op == '/': return a / b
#                    if op == '**': return a ** b
#                except (ZeroDivisionError):
#                    return "ZeroDivision"
#     except (ValueError, TypeError):
#         return "Invalid"



def safe_first(expr):
    expr = expr.replace(' ', '')
    operators = ['**', '+', '-', '/', '*']  # correct order

    found = 0
    detected_op = None

    # Count operators
    for op in operators:
        if op in expr:
            found += expr.count(op)
            detected_op = op

    if found != 1:
        return "Invalid"

    parts = expr.split(detected_op)
    if len(parts) != 2:
        return "Invalid"

    a, b = parts

    try:
        a = float(a)
        b = float(b)
    except:
        return "Invalid"

    try:
        if detected_op == '+': return a + b
        if detected_op == '-': return a - b
        if detected_op == '*': return a * b
        if detected_op == '/': return a / b
        if detected_op == '**': return a ** b
    except ZeroDivisionError:
        return "ZeroDivision"



def safe_batch_eval(expressions):
    return [safe_first(expr) for expr in expressions]

expressions = ["10/2", "5*6", "4/0", "abc+3", "1+4+5"]
print(safe_batch_eval(expressions))


# v2

import re

def safe_eval_two(expr):
    expr = expr.replace(" ", "")
    tokens = re.findall(r'\d+\.?\d*|[+\-*/]{1,2}', expr)

    if len(tokens) not in (3, 5):
        return "Invalid"

    try:
        values = [float(tokens[0])]
        ops = []

        for i in range(1, len(tokens), 2):
            ops.append(tokens[i])
            values.append(float(tokens[i+1]))
    except:
        return "Invalid"

    def apply(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/':
            if b == 0: raise ZeroDivisionError
            return a / b
        if op == '**': return a ** b
        raise ValueError

    try:
        result = values[0]
        for i, op in enumerate(ops):
            result = apply(result, values[i+1], op)
        return result
    except ZeroDivisionError:
        return "ZeroDivision"

def safe_batch_eval_two(expressions):
    return [safe_eval_two(expr) for expr in expressions]

expressions = ["100000/2+1", "5*6*1", "4/0/0", "abc+3-5", "1+4+5", "1+2"]
print(safe_batch_eval_two(expressions))



#
#
# import ast
# import operator
#
# # Allowed operators
# OPS = {
#     ast.Add: operator.add,
#     ast.Sub: operator.sub,
#     ast.Mult: operator.mul,
#     ast.Div: operator.truediv,
#     ast.Pow: operator.pow
# }
#
# def safe_eval(expr):
#     try:
#         tree = ast.parse(expr, mode="eval")
#     except SyntaxError:
#         return "Invalid"
#
#     def eval_node(node):
#         if isinstance(node, ast.Expression):
#             return eval_node(node.body)
#
#         if isinstance(node, ast.Constant):  # numbers only
#             if isinstance(node.value, (int, float)):
#                 return node.value
#             raise ValueError
#
#         if isinstance(node, ast.BinOp):
#             op_type = type(node.op)
#             if op_type not in OPS:
#                 raise ValueError
#
#             left = eval_node(node.left)
#             right = eval_node(node.right)
#
#             try:
#                 return OPS[op_type](left, right)
#             except ZeroDivisionError:
#                 raise ZeroDivisionError
#
#         # Anything else is forbidden
#         raise ValueError
#
#     try:
#         return eval_node(tree)
#     except ZeroDivisionError:
#         return "ZeroDivision"
#     except:
#         return "Invalid"



#10


def menu_system(commands):
    value = 1
    for command in commands:
        parts = command.split()
        a = parts[0]
        b = int(parts[1]) if len(parts) > 1 else None
        try:
            if a == 'ADD':
                value = value + int(b)
            elif a == 'MUL':
                value = value * int(b)
            elif a == 'STOP':
                return value
            elif a == 'DIV':
                value = value / int(b)
        except ZeroDivisionError:
            continue
        except (ValueError, TypeError):
            continue
    return value

print(menu_system(['ADD 5', 'MUL 1', 'STOP']))

#11

def choose_clean_word(words):
    for word in words:
        if any(x.isdigit() for x in word):
            continue
        if any(c in word for c in "!?;-_"):
            continue
        if len(word) < 5:
            continue
        if word == 'END':
            break
        return word
    return 'No valid words'


#12


inventory = [
    {"name": "apple",     "qty": 50, "price": 2.5},
    {"name": "banana",    "qty": 10, "price": 1.2},
    {"name": "watermelon","qty": 5,  "price": 7.0},
    {"name": "pear",      "qty": 0,  "price": 3.0},
    {"name": "kiwi",      "qty": 25, "price": 1.8},
]

def filter_and_sort_inventory(items):
    valid_items = []

    for item in items:
        try:
            if item["qty"] == 0:
                continue
            # Access all keys to validate
            item["name"]
            item["price"]
            valid_items.append(item)
        except (KeyError, TypeError):
            continue

    return sorted(
        valid_items,
        key=lambda item: (item["price"], -item["qty"], item["name"])
    )


print(filter_and_sort_inventory(inventory))




