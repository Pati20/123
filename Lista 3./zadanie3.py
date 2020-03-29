# Author: Patrycja Paradowska
# 28 marca 2020r. Lista 3. Python, Zadanie 3. Odczyt pliku tekstowego i pobieranie ostatniej kolumny

def last_column_bytes(path: str) -> int:
    with open(path) as file:
        return sum(int(line.split()[-1]) for line in file)

print(last_column_bytes('zadanie3_test.txt'))