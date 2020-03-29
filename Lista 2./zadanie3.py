# Author: Patrycja Paradowska
# 21.03.2020r. Lista 2., Zadanie 3. Zamiana nazw plików w danym katalogu oraz podkatalogach na małe litery

import sys
import os

def replacing_files_names(path):
    for name in os.listdir(path):
        if os.path.isfile(path + '/' + name):
            path2 = path + '/' + name.lower()
            os.rename(path + '/' + name, path2)
        elif os.path.isdir(path):
            replacing_files_names(path + '/' + name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Niepoprawna liczba argumentów! Podaj nazwę katalogu.")
        exit(1)
    replacing_files_names(sys.argv[1])