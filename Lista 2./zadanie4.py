# Author: Patrycja Paradowska
# 21.03.2020r. Lista 2., Zadanie 4. Znajdowanie plików powtarzających się więcej niż raz.

import os
import sys
import hashlib
from pathlib import Path
from collections import defaultdict


def get_file_hash(filename, blocksize=65536):
    h = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            h.update(block)
    return h.hexdigest()


def repchecker(dir: str):
    file_list = defaultdict(list)
    root = Path(dir)
    for path in filter(Path.is_file, root.rglob("*")):
        hash = get_file_hash(path)
        size_file = os.path.getsize(path)
        file_list[hash+str(size_file)].append(path)
    return file_list


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Niepoprawna liczba argumentów!! Użycie: python zadanie4.py path")
        exit(1)

    for key, value in ((k, v) for k, v in repchecker(sys.argv[1]).items() if len(v) > 1):
        print("-----------------------------------------------------")
        for x in value:
            print(x)