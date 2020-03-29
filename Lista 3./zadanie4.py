# Author: Patrycja Paradowska
# 28 marca 2020r. Lista 3. Python, Zadanie 4. Quicksort

from typing import List

def quicksort(l: List):
    if len(l) == 0 or len(l) == 1:
        return l
    first, others = l[0], l[1:]
    elts_lt_x = list(filter(lambda x: x <= first, others))
    elts_greq_x = list(filter(lambda x: x > first, others))
    return quicksort(elts_lt_x) + [first] + quicksort(elts_greq_x)

L = [9,-2, 1, 2, 0, 4, 5, 7, 8, 6, 3, -1]
print(quicksort(L))