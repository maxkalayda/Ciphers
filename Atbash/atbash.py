upperCased = list(map(chr, range(ord('А'), ord('Я') + 1)))
lowerCased = list(map(chr, range(ord('а'), ord('я') + 1)))
otherSymbols = [' ', '?', '!', '.', ':', '-', '_', '(', ')', ',']

Alphabet = upperCased + lowerCased + otherSymbols
AlphabetReversed = list(reversed(Alphabet))


def main():
    print("AtbashCipher_Demo")
    clearText = input('Введите текст: ')
    print("Исходный текст: " + clearText)
    cipherText = cipher(clearText)
    print("Зашифрованный текст: {0}".format(cipherText))
    decipherText = decipher(cipherText)
    print("Расшифрованный текст: {0}".format(decipherText))
    return


def cipher(clearText):
    result = ""

    for c in clearText:
        idx = Alphabet.index(c)

        result += AlphabetReversed[idx]

    return result


def decipher(cipherText):
    result = ""

    for c in cipherText:
        idx = AlphabetReversed.index(c)

        result += Alphabet[idx]

    return result


main()





