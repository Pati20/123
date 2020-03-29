# Author: Patrycja Paradowska
# 21.03.2020r. Lista 2., Zadanie 1. Wyswietlanie informacji o pliku

import sys

def file_information(file):
    lines = 0
    words = 0
    bytes = 0
    line_max_length = 0

    data = open(file, "rb")
    for line in data:
        lines += 1
        if len(line) > line_max_length:
            line_max_length = len(line)
        bytes += len(line)
        words += len(line.split())

    data.close()
    print("Liczba bajtów: ", bytes)
    print("Liczba słów: ", words)
    print("Liczba linii: ", lines)
    print("Maksymalna długość linii: ", line_max_length)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Niewłaściwa liczba argumentów!")
        exit(1)
    file_information(sys.argv[1])