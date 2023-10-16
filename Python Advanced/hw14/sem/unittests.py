# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest
from task import clear_test


class TestClearTest(unittest.TestCase):
    def setUp(self) -> None:
        self.correct = 'text'
        self.text_1 = 'text'
        self.text_2 = 'TeXt'
        self.text_3 = 'te,xt!'
        self.text_4 = 'техt'
        self.text_5 = 'teЯЯЯ,xt!'

    def test1(self):
        self.assertEqual(self.correct, clear_test(self.text_1))

    def test2(self):
        self.assertTrue(self.correct == clear_test(self.text_2))

    def test3(self):
        self.assertFalse(self.correct is clear_test(self.text_3))

    def test4(self):
        self.assertRaises(ValueError, clear_test, None)

    def test5(self):
        self.assertEqual(self.correct, clear_test(self.text_5))


if __name__ == '__main__':
    unittest.main(verbosity=2)
