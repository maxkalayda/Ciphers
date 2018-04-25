alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
                  'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
                  'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
                  'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
                  'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
                  'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
                  'ю':30, 'я':31, ' ':32, ",":33, ".":34
                  }
msg = input("Введите текст:")
test = list()

for letter in msg:
    test.append(int(alphabet_lower.get(letter)))

print("Исходный текст",test)

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

encrypted = list()
# шифрование
for i in range(len(test)):
    encrypted.append(int((test[i] + i)% len(alphabet_lower)))

print('Зашифрованный текст: ', encrypted)

test_decrypted = list()
for i in range(len(encrypted)):
        test_decrypted.append(int((encrypted[i] - i)%len(alphabet_lower)))

print('Расшифрованный текст: ', test_decrypted)

rarp = ''
for i in range(len(test_decrypted)):
    rarp += str(get_key(alphabet_lower, test_decrypted[i]))

print(rarp)