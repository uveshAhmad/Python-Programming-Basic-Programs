# n! = 1X2X3X4....Xn

# from itertools import product


# n = 5
# product = 1
# for i in range(n):
#     product=product*(i+1)

# print(product)    


from itertools import product
from math import prod


def factorial_iter(n):
    product = 1
    for i in range (n):
        return product

print(factorial_iter(5))        