# Author: Patrycja Paradowska
# 28 marca 2020r. Lista 3. Python, Zadanie 1. Transpozycja macierzy

from typing import List

def transposition(matrix: List[str]) -> List[str]:
    return [" ".join(row.split()[i] for row in matrix) for i in range(len(matrix))]

matrix = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
print(transposition(matrix))