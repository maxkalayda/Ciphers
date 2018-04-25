msg = "один час утром стоит двух часов вечером"
msg_bin = ' '.join(format(ord(x),'b')for x in msg)
len_msg_bin = len(msg_bin)
print(msg_bin)
for i in msg_bin:
    print(chr(int(msg_bin[i],2)))



'''for i in range(len(msg_bin)):
    #msg_bin_list.append(msg_bin[i])
    msg_bin_list.append(chr(int(msg_bin[i*8:8*8+8],2)) for i in range (len_msg_bin))
print(msg_bin_list)
'''
'''
1. Перевод текста в биты
2. Генератор гаммы битовых
3. Xor исходного текста по битам с гаммой
4. Если число раундов чётное, то мы получаем исходное значение
5. Расшифровка: шифр-текст xor с гаммой, получаем исходный текст
'''