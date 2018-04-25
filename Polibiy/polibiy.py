text = input('Введите текст: ')

alphabet_lower = {'а':'11', 'б':'12', 'в':'13', 'г':'14', 'д':'15',
                  'е':'16', 'ж':'17', 'з':'18', 'и':'19', 'й':'20',
                  'к':'21', 'л':'22', 'м':'23', 'н':'24', 'о':'25',
                  'п':'26', 'р':'27', 'с':'28', 'т':'29', 'у':'30',
                  'ф':'31', 'х':'32', 'ц':'33', 'ч':'34', 'ш':'35',
                  'щ':'36', 'ъ':'37', 'ы':'38', 'ь':'39', 'э':'40',
                  'ю':'41', 'я':'42', ' ':'43', '.':'44'
                  }

crypt = ''
for letter in text:
    if letter in alphabet_lower:
        letter = alphabet_lower.get(letter) #возвращает значение ключа
        crypt += str(letter)
        crypt += ' '
print(crypt)

temp = ''
decrypt = ''
for i in crypt:
    if i != ' ':
        temp += i
    else:
        for j in alphabet_lower:
            if alphabet_lower[j] == temp:
                decrypt +=j
        temp = ''
print(decrypt)
