
# a = [1, 2, 3, 4]
# for item in a:
#     print(item)

# a = "Alice has a cat"
# for item in a:
#     print(item, end=" ")

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 6
#
# for item in my_generator():
#     print(item)


from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


iter = PrimeIterator(10)
for elem in iter:
    print(elem)


#  in iterators, avem o clasa care repreinta un iterabil, in timp ce next(), generatorul e o functie care reprezinta un iterabil

