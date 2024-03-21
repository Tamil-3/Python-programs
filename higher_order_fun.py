# map(), filter(), reduce()
from functools import reduce

def check(fruit):
    return fruit[0] == 'A'

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# result = map(check, fruit)
result = filter(check, fruit)
print(list(result))


def multiply(n1, n2):
    return n1 + n2

nums = [10, 23, 45, 67]
print(reduce(multiply, nums))