# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите
# 4 успешных расстановки.
import random as rnd


class Queen:
    _X_STR = 'ABCDEFGH'
    _Y_STR = '12345678'
    _BOARD_SIZE = 8

    def __init__(self, coord: str):
        self._x, self._y = self.coord_parse(coord)

    def __str__(self):
        return f'Q({self._X_STR[self._x]}{self._Y_STR[self._y]})'

    def __repr__(self):
        return f'Q({self._X_STR[self._x]}{self._Y_STR[self._y]})'

    def __hash__(self):
        return self._x * 10 + self._y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, new_x):
        if new_x.upper() not in self._X_STR:
            raise ValueError('Недопустимое значение для координаты X')
        self._x = self._X_STR.find(new_x)

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, new_y):
        if new_y.upper() not in self._Y_STR:
            raise ValueError('Недопустимое значение для координаты Y')
        self._y = self._Y_STR.find(new_y)

    def coord_parse(self, coord) -> tuple[int, int]:
        x, y, *z = coord.upper()
        if any((z, x not in self._X_STR, y not in self._Y_STR)):
            raise ValueError('Недопустимое значение для координат')
        return self._X_STR.find(x), self._Y_STR.find(y)

    def check_cross(self, other) -> bool:
        start_d1_x = self.x - min(self.x, self.y)
        start_d1_y = self.y - min(self.x, self.y)
        d1 = zip(range(start_d1_x, self._BOARD_SIZE), range(start_d1_y, self._BOARD_SIZE))

        start_d2_x = self.x - min(self.x, self._BOARD_SIZE - 1 - self.y)
        start_d2_y = self.y + min(self.x, self._BOARD_SIZE - 1 - self.y)
        d2 = zip(range(start_d2_x, self._BOARD_SIZE), range(start_d2_y, -1, -1))

        if any((self.x == other.x,
                self.y == other.y,
                (other.x, other.y) in d1,
                (other.x, other.y) in d2)):
            return True

        return False

    @staticmethod
    def get_rnd_coord():
        x = rnd.choice(Queen._X_STR)
        y = rnd.choice(Queen._Y_STR)
        return x + y

    def set_rnd_coord(self):
        self._x = rnd.randint(0, 7)
        self._y = rnd.randint(0, 7)


if __name__ == '__main__':
    # 1 часть задания
    q_lst = [Queen('A4'),
             Queen('B1'),
             Queen('C5'),
             Queen('D8'),
             Queen('E2'),
             Queen('F7'),
             Queen('G3'),
             Queen('H6')]
    flag = True
    for i in range(len(q_lst)):
        for j in range(i + 1, len(q_lst)):
            if q_lst[i].check_cross(q_lst[j]):
                print(f'{q_lst[i]=}, {q_lst[j]}')
                flag = False
                break
        if not flag:
            print(f'В комбинации {q_lst} есть бьющие друг друга ферзи')
            break
    else:
        print(f'В комбинации {q_lst} нет бьющих друг друга ферзей')

    # 2 часть задания
    successful_arrangement = []
    max_attempts = 1000
    while len(successful_arrangement) < 4:
        q_lst = []
        attempts = 0
        while len(q_lst) < 8:
            new_q = Queen(Queen.get_rnd_coord())
            flag = True
            for q in q_lst:
                if q.check_cross(new_q):
                    flag = False
                    break
            if flag:
                q_lst.append(new_q)
                attempts = 0
            else:
                attempts += 1
                if attempts >= max_attempts:
                    break
        else:
            q_set = set(q_lst)
            if q_set not in successful_arrangement:
                successful_arrangement.append(q_set)
    print('4 разные комбинации 8-ми небьющих друг друга ферзей: ')
    for item in successful_arrangement:
        print(item)
