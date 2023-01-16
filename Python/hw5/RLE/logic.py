def encrypter(data: str) -> str:
    encrypted_data = ''
    c_data = data # chars data: 'aaaaabbbccccaaddd' -> 'abcad'
    for c in set(data):
        while 2 * c in c_data:
            c_data = c_data.replace(2 * c, c) # 'aaaabbc' -> 'abc'

    for c in c_data:
        new_data = data.lstrip(c) # 'aaaaabbbccccaaddd' -> lstrip('a') -> 'bbbccccaaddd'
        count = len(data) - len(new_data.lstrip(c)) # разница длинн стрипнутой и исходной строки есть кол-во букв
        data = new_data
        if count == 1:
            encrypted_data += c
        else:        
           encrypted_data += str(count) + c

    return encrypted_data

def decrypter(data: str) -> str:
    decrypted_data = ''
    while data:
        i = 0 # константа, указывающая на первый элемент строки с данными
        if data[i].isdigit():
            factor = int(data[i]) # множитель кол-ва буквы
            j = 1 # указатель индекса
            while data[i + j].isdigit(): # проверяем не являлось ли число многоразрядным
                factor = factor * 10 + int(data[i + j]) # сборка числа из разрядов
                j += 1
            char = data[i+j]
            decrypted_data += factor * char
            data = data[i + j + 1:] # обрезаем строку с данными чтобы не проходиться по пройденным эл-ам
        else:
            char = data[i]
            decrypted_data += char
            data = data[i + 1:] # обрезаем строку с данными чтобы не проходиться по пройденным эл-ам
    
    return decrypted_data