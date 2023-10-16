# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)


from string import ascii_lowercase
import doctest


def clear_test(text: str) -> str:
    """
    >>> clear_test('text')
    'text'

    >>> clear_test('TeXt')
    'text'

    >>> clear_test('te,xt!')
    'text'

    >>> clear_test('техt')
    't'

    >>> clear_test('тE,хT!')
    'et'

    Функция удаляет из текста все символы
    кроме букв латинского алфавита и пробелов.
    :param text: входной текст
    :return: новая строка, состоящая из символов латинского алфавита и пробелов строки text
    """
    result = ''
    if text is not None:
        for c in text:
            if c.lower() in ascii_lowercase + ' ':
                result += c
        return result.lower()
    else:
        raise ValueError


if __name__ == '__main__':
    doctest.testmod(verbose=True)
