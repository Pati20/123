# Author: Patrycja Paradowska
# 28 marca 2020r. Lista 3. Python, Zadanie 2. Generator, ktory przechodzi dowolna liste i podaje jej elementy

def flatten(lista):
    for element in lista:
        if isinstance(element, list):
            for e in flatten(element):
                yield e
        else:
            yield element

l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6], 7, [[9, [123, [[123]]]], 10]]
print(list(flatten(l)))