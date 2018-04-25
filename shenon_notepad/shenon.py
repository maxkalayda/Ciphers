import random
alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
                  'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
                  'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
                  'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
                  'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
                  'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
                  'ю':30, 'я':31, ' ':32, ",":33, ".":34
                  }
'''
a = bin(12)[2:]
print(int(a,base=2))
'''
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

msg = input("Введите текст:")
msg_list = list(msg)
msg_list_len = len(msg_list)
msg_code_bin_list = list()
for i in range(len(msg_list)):
    msg_code_bin_list.append(alphabet_lower.get(msg_list[i]))

print("Исходный текст:={}".format(msg_code_bin_list))
key_list = list()
for i in range(msg_list_len):
    key_list.append(random.randint(0,40))

print("Ключ:={}".format(key_list))
cipher_list = list()
#шифрование по с = m xor k
for i in range(msg_list_len):
    m = int(msg_code_bin_list[i])
    k = int(key_list[i])
    cipher_list.append(int(bin(m^k),base=2))

print("Шифротекст:={}".format(cipher_list))
#расшифрование по m = c xor k
decipher_list = list()
for i in range(msg_list_len):
    c = int(cipher_list[i])
    k = int(key_list[i])
    decipher_list.append(int(bin(c^k),base=2))

deciphered_str = ""
for i in range(len(decipher_list)):
    deciphered_str += get_key(alphabet_lower,decipher_list[i])

print("Расшифрованный код:={}".format(decipher_list))
print("Расшифрованный текст:={}".format(deciphered_str))

