# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
import pytest

from task import clear_test


def test1():
    assert clear_test('text') == 'text'


def test2():
    assert clear_test('TeXt') == 'text'


def test3():
    assert clear_test('te,xt!') == 'text'


def test4():
    assert clear_test('tтехext') == 'text'


def test5():
    assert clear_test('teЯЯЯ,xt!') == 'text'


if __name__ == '__main__':
    pytest.main(['-v'])
