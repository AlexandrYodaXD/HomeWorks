from logic import *

encrypted_data = encrypter(input('Введи строку, которую надо сжать >: '))
print('Строка после сжатия:', encrypted_data)
decrypted_data = decrypter(encrypted_data)
print('Строка после разжатия:', decrypted_data)
