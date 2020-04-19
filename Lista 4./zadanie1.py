# Author: Patrycja Paradowska
# 6 kwietnia 2020r. Lista 4. Python, Zadanie 1.
# Napisac dekorator, ktory drukuje informacje o czasie wykonywania funkcji.
# Jako testujaca funkcje uzyto funkcji primes(n) zwracajaca liste liczb pierwszych nie wiekszych niz n

from time import time
import math

def function_time(f):
    def internal(*args):
        start = time()
        f(*args)
        end = time() - start
        print(f'Function execution time: {end}')
    return internal

@function_time
def testing_function(n):
    prime_numbers = []
    for i in range(2, n):
        if all(i % j > 0 for j in range(2, int(math.sqrt(i) + 1))):
            prime_numbers.append(i)
    return prime_numbers

if __name__ == '__main__':
    testing_function(100000)