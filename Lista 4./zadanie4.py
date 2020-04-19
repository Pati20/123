# Author: Patrycja Paradowska
# 12 kwietnia 2020r. Lista 4. Python, Zadanie 4.
# Napisz dekorator @overload, ktory pozwoli na "przeciazenie" funkcji.

import math
from inspect import getfullargspec

class overload:
    map = {}
    def __init__(self, function):
        self.function_name = function.__name__
        self.map[(function.__name__, len(getfullargspec(function).args))] = function

    def __call__(self, *args, **kwargs):
        return self.map[self.function_name, len(args)](*args, **kwargs)

@overload
def norm(x, y):
    return math.sqrt(x * x + y * y)

@overload
def norm(x, y, z):
    return abs(x) + abs(y) + abs(z)

@overload
def notnorm(x, y):
    return 1

@overload
def area(a, b):
    return a * b

@overload
def area(a):
    return a ** 2

@overload
def area(a, b, h):
    return ((a + b) * h)/2

if __name__ == '__main__':
    print(f"norm(2,4) = {norm(2, 4)}")
    print(f"norm(2,3,4) = {norm(2, 3, 4)}")
    print(f"notnorm(2, 4) = {notnorm(2,4)}")
    print(f"Pole kwadratu o boku a = 5:  {area(5)}")
    print(f"Pole prostokata o bokach (a=2, b=5) = {area(2, 5)}")
    print(f"Pole trapezu o podstawach a=3 i b=7 oraz wysokosci h=5: = {area(3,7,5)}")

