import numpy
row = 3
col = 3
row_1 = [1,2,3]
row_2 = [2,4,1]
row_3 = [3,2,1]
matrix_key = [row_1,row_2,row_3]
for i in range(row):
    print(matrix_key[i])

det = numpy.linalg.det(matrix_key)
print('Det:',det)

#matrix_text = [1,2,3]
#кодировка текста
open_message = input("Введите текст:")
#условие на чётность списка
if len(open_message) % 3 == 0:
    print('Длина исходного сообщения:',len(open_message))
else:
    open_message += '11'
    print('Длина исходного сообщения с добавлениями:',len(open_message))
# ОТКРЫТОЕ СООБЩЕНИЕ str ПЕРЕВОДИМ В UNICODE И ЗАПСИЫВАЕМ В СПИСОК
message_code_char = list()
for letter in open_message:
    message_code_char.append(ord(letter))
#РАЗДЕЛЯЕМ СИМВОЛЫ ЮНИКОДА ПО 3
split_open_message = [message_code_char[i:i + 3] for i in range(0,len(message_code_char),3)]
print('Закодированное сообщение:',split_open_message)
#ШИФРОВАНИЕ
cipher_code_matrix = []
for i in range(len(split_open_message)):
    cipher_code_matrix.append(numpy.dot(split_open_message[i],matrix_key))

print('Шифрованное сообщение:',cipher_code_matrix)
#РАСШИФРОВКА
reverse_matrix_key = numpy.linalg.inv(matrix_key)
decipher_code_matrix = []
for i in range(len(cipher_code_matrix)):
    decipher_code_matrix.append(numpy.dot(cipher_code_matrix[i],reverse_matrix_key))

print('Расшифрованное сообщение сообщение:', decipher_code_matrix)
#ДЕКОДИРОВАНИЕ СООБЩЕНИЯ ПО ЮНИКОДУ
print(type(decipher_code_matrix))
temp_decode_list = list()
for i in range(len(decipher_code_matrix)):
    for j in range(len(decipher_code_matrix[i])):
        temp_decode_list.append(int(round((decipher_code_matrix[i][j]),1)))

print(temp_decode_list)
str_full_decode = ''
for i in range(len(temp_decode_list)):
    str_full_decode += str(chr(temp_decode_list[i]))

print(str_full_decode)
print(str_full_decode.split('.1'))

