# Отличия от предыдущей версии:
# - Преобразование каждого числа в 36-ричную систему счисления

from math import sin


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def coder(text, encoding=True):
    total = ''
    key = 0
    key_memory = 0
    recorded = False

    if encoding:
        for key_part in text:
            key += ord(key_part)
        key = int(key)
        key *= 8

        for letter in text:
            while key >= 2048:
                key -= 2047
            if not(recorded):
                memory = key
                recorded = True   
            total += convert_base(str(ord(letter) ^ key), to_base=36) + ' '
            key = int(abs(sin(key)) * 2048)
        while memory < 1000:
            memory += 137
            key_memory += 1
        total += convert_base(str(memory), to_base=36) + ' '
        if key_memory > 0:
            total += convert_base(str(key_memory * 1009), to_base=36)
        else:
            total += convert_base('1469', to_base=36)
    else:
        text = list(map(lambda num: convert_base(num, from_base=36), text.strip().split(' ')))
        if text[-1] == '1469':
            key = int(text[-2])
        else:
            key = int(text[-2]) - (137 * int(int(text[-1]) / 1009))
        for symbol in text[0:-2]:
            while key >= 2048:
                key -= 2047
            total += chr(int(symbol) ^ key)
            key = int(abs(sin(key)) * 2048)
    return total


while True:
    choice = input('1 - зашифровать\n2 - расшифровать\n: ')
    text = input('text: ')
    if choice == '1':
        print(coder(text))
    else:
        print(coder(text, encoding=False)) 
