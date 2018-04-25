sbox = (
    (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
    (14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9),
    (5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11),
    (7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3),
    (6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2),
    (4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14),
    (13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12),
    (1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12),
) # таблица замены(она заранее известна, определена в стандарте ЦБР или можно взять любую другую)


def _bit_length(x): # конвертация числа int  в binary string prefixed with “0b” и получение длины этой строки
    assert x >= 0 # проверка, что число на вход больше нуля
    return len(bin(x)) - 2 #возвращаем длину числа - 2, (-2 это вначале префикс hex=0x)


def f_function(var, key): # функция работы с блоками R и L
    assert _bit_length(var) <= 32  # проверка, что длина блока меньше или равна 32
    assert _bit_length(key) <= 32  # проверка, что длина Ki меньше или равна 32

    temp = (var + key) % (1 << 32) # (R+Ki) mod 2**32

    output = 0
    for i in range(8): # блок R заменяется каждый символ на новый по таблице
        output |= ((sbox[i][(temp >> (4 * i)) & 0b1111]) << (4 * i)) #i-строка в таблице, temp=значение, которое ищем в строке i

    output = ((output >> (32 - 11)) | (output << 11)) & 0xFFFFFFFF # Полученный R сдвигается на 11 бит влево и делается побитовая операция OR(или)(одинаковые циферки 0, разные 1)

    return output #возвращаем полученный новый Ri


def round_encryption(input_left, input_right, round_key): #функция замены после преобразования R блока(шифр)
    output_left = input_right #Lчасть становится R
    output_right = input_left ^ f_function(input_right, round_key) # R = L часть xor R(исходная, функция выше)

    return output_left, output_right #возвращает L и R


def round_decryption(input_left, input_right, round_key): #функция замены после преобразования R блока(расшифр)
    output_right = input_left #R становится L
    output_left = input_right ^ f_function(input_left, round_key) # L = R часть xor R(исходная, функция выше) mod2

    return output_left, output_right #возвращает L и R


class GOST:
    def __init__(self):
        self.master_key = [None] * 8 #конструктор, инициализируем 8 пустых списком для ключа 256 бит по 32 бит

    def set_key(self, master_key): #функция генерации ключа
        assert _bit_length(master_key) <= 256 #проверка на длину (assert сразу вызывает исключение, если меньше 256)
        for i in range(8):
            self.master_key[i] = (master_key >> (32 * i)) & 0xFFFFFFFF # i-ый лист заполняется 32битами со сдвигом вправо, чтобы в следующий лист пошли новые значения
        print('master_key',[hex(i) for i in self.master_key]) #вывод ключа 256 по 32 бита списками

    def encrypt(self, plaintext): #функция шифрования
        assert _bit_length(plaintext) <= 64 #блок текста должен быть 64 бита, иначе исключение
        text_left = plaintext >> 32 #блок текста 64 разбивается на два 32 со сдвигом вправо(Старшие биты)
        text_right = plaintext & 0xFFFFFFFF #оставшиеся 32 записываются в R(младшие биты), если не хватает добавляем 0xFFFFFFFF
        print('text: L={} R={}'.format(hex(text_left), hex(text_right))) #вывод L и R частей

        for i in range(24): #с 1 по 24 ключи идут k1,k2..k8 и снова повторяются
            text_left, text_right = round_encryption( #вызываем функцию шифрования раунда, см выше
                text_left, text_right, self.master_key[i % 8])

        for i in range(8): #с 25 по 32 ключи идут k8,k7..k1 и так далее
            text_left, text_right = round_encryption( #вызываем функцию шифрования раунда, см выше
                text_left, text_right, self.master_key[7 - i])

        return (text_left << 32) | text_right  #L сдвигается влево на 32 бита и OR(или) с правой частью(тупо склеиваются в один)

    def decrypt(self, ciphertext): #функция расшифровки
        assert _bit_length(ciphertext) <= 64 #разбивается на блоки по 64, меньше 64 бит исключение
        text_left = ciphertext >> 32 #блок текста 64 разбивается на два 32 со сдвигом вправо(Старшие биты)
        text_right = ciphertext & 0xFFFFFFFF #оставшиеся 32 записываются в R(младшие биты)

        for i in range(8): #ключи начинаются в обратном порядке с k8...k1 (32..25)
            text_left, text_right = round_decryption( #вызываем функцию расшифрования раунда, см выше
                text_left, text_right, self.master_key[i])

        for i in range(24): #ключи начинаются по порядку с k1...k8 (24..1)
            text_left, text_right = round_decryption( #вызываем функцию расшифрования раунда, см выше
                text_left, text_right, self.master_key[(7 - i) % 8])

        return (text_left << 32) | text_right #L сдвигаем влева на 32 бита и OR с  К частью(тупо склеиваем два блока)


if __name__ == '__main__': #тут думаю всё понятно
    text = 0x68656c6c6f21 #0x префикс hex, нужно именно так записывать, тк считывание должно быть с файла
    text_string = bytearray.fromhex("68656c6c6f21").decode()
    #cipher_text = bytearray.fromhex("f30a4e65e31c25d9").decode()
    print("Текст: {}".format(text_string))
    # 0xfedcba0987654321
    key = 0x4f6e6520686f757220696e20746865206d6f726e696e6720636f73742074776f #0x префикс hex, нужно именно так записывать, тк считывание должно быть с файла
    key_string = bytearray.fromhex("4f6e6520686f757220696e20746865206d6f726e696e6720636f73742074776f").decode()
    print("Ключ: {}".format(key_string))
    #ключ состоит из 64 символов * 4(256 бит ключ), тк 1 символ 4
    my_GOST = GOST() #созадём объект класса
    my_GOST.set_key(key) #вызываем функцию инициализации ключа

    num = 32 #число раундов  (гост 28147-89 тут их 32)

    for i in range(num):
        text = my_GOST.encrypt(text)
    print ("Зашифрованный текст: hex= {}".format(hex(text)))

    for i in range(num):
        text = my_GOST.decrypt(text)
    print ("Расшифрованный текст: hex= {}, string= {}".format(hex(text),text_string))
    