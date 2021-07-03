from math import sin

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
            total += str(ord(letter) ^ key) + ' '
            key = int(abs(sin(key)) * 2048)
        while memory < 1000:
            memory += 137
            key_memory += 1
        total += str(memory) + ' '
        if key_memory > 0:
            total += str(key_memory * 1009)
        else:
            total += '1469'
    else:
        text = text.strip().split(' ')
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
