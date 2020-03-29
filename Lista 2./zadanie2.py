# Author: Patrycja Paradowska
# 21.03.2020r. Lista 2., Zadanie 2. Kodowanie i dekodowanie dowolnego pliku w kodzie Base64

import sys

BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

def get_char_on_bit():
    dict_char_on_bit = {'A': '000000', '=': '0'}
    adder = '000001'
    last = '000000'
    for char in (BASE64[1:63]):
        last = bin(int(last, 2) + int(adder, 2))
        dict_char_on_bit[char] = last[2:].rjust(6, '0')
    return dict_char_on_bit

char_on_bit = get_char_on_bit()
bit_on_char = dict((bin_representation, char) for char, bin_representation in char_on_bit.items())


def encoding(data: bytes):
    result = []
    bin_form = ""
    for i in range(0, len(data), 3):
        piece_ = data[i:i + 3]
        remaining_part = (3 - len(piece_))
        for j in range(len(piece_)):
            bin_form += '{0:08b}'.format(piece_[j])
        bin_form = bin_form.ljust(24, '0')

        for k in range(0, len(bin_form), 6):
            result.extend(bit_on_char[bin_form[k:k + 6]])
        bin_form = ""

        for w in range(remaining_part):
            result[-w - 1] = "="

    str_result = ''.join(s for s in result)
    return str_result


def decoding(data2: str):
    skipping = data2.count('=')
    tmp = []
    for i in range(0, len(data2), 4):
        piece_ = data2[i:i + 4]
        tmp.extend([
            int('0b' + char_on_bit[piece_[0]] + char_on_bit[piece_[1]][:2], 2),
            int('0b' + char_on_bit[piece_[1]][2:] + char_on_bit[piece_[2]][:4], 2),
            int('0b' + char_on_bit[piece_[2]][4:] + char_on_bit[piece_[3]], 2)])
    for i in range(skipping):
        tmp.pop()
    return bytearray(tmp)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Niepoprawna liczba argumentów. Podaj:")
        print("a) --encode <plik WEJŚCIOWY> <plik WYJŚCIOWY>")
        print("b) --decode <plik WEJSCIOWY> <plik WYJSCIOWY>")
        exit(1)

    input = open(sys.argv[2], 'rb')
    output = open(sys.argv[3], 'wb')

    for f in iter(lambda: input.read(240000), b''):
        if sys.argv[1] == '--encode':
            output.write(encoding(f).encode())
        elif sys.argv[1] == '--decode':
            output.write(decoding(f.decode()))
        else:
            print("Nieprawidłowa komenda.")
            exit(1)