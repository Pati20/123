# Author: Patrycja Paradowska
# 28 marca 2020r. Lista 3. Python, Zadanie 5. Program, który generuje wszystkie podzbiory danego zbioru

def allsubsets(set):
    if len(set) == 0:
        return [[]]
    first, others = set[0], set[1:]
    return allsubsets(others) + list(map(lambda x: [first, *x], allsubsets(others)))

set = [1, 2, 3]
print(allsubsets(set))