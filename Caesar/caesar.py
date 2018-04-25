import  string
secretMsg = ''
alpha_lower = str('абвгдежзийклмнопрстуфхцчшщъыьэюя.')
alpha_upper = str('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.')
alpha_special = str(string.punctuation + ' ')
res = []

print('1.Зашифровать сообщение')
print('2.Расшифровать сообщение')
choice = int(input('Выберите режим: '))
if choice == 1:
    message = input("Введите текст: ")
    print(message, '\n')
    key = int(input("Введите ключ: "))
    print(key)
    for letter in message:
        if letter in alpha_lower:
            res.append(alpha_lower[(alpha_lower.find(letter) + key) % len(alpha_lower)])
        elif letter in alpha_upper:
            res.append(alpha_upper[(alpha_upper.find(letter) + key) % len(alpha_upper)])
        else:
            res.append(alpha_special[(alpha_special.find(letter) + key) % len(alpha_special)])

    print('Зашифрованное сообщение: ', ''.join(res), sep='')
elif choice == 2:
    message = input("Введите зашифрованный текст: ")
    print(message, '\n')
    key = int(input("Введите ключ: "))
    print(key)
    for letter in message:
        if letter in alpha_lower:
            res.append(alpha_lower[(alpha_lower.find(letter) - key) % len(alpha_lower)])
        elif letter in alpha_upper:
            res.append(alpha_upper[(alpha_upper.find(letter) - key) % len(alpha_upper)])
        else:
            res.append(alpha_special[(alpha_special.find(letter) - key) % len(alpha_special)])

    print('Зашифрованное сообщение: ', ''.join(res), sep='')
