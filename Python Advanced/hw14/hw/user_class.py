import json
import os


class User:
    def __init__(self, name: str, id_: int, level: int = 1):
        if not isinstance(name, str):
            raise ValueError('Имя должно быть текстового вида')
        self.name = name
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError('Личный идентификатор должен быть целым числом')
        self.id_ = id_
        if not isinstance(level, int) or level not in range(1, 8):
            raise ValueError('Уровень доступа должен быть целым числом от 1 до 7')
        self.level = level

    def __str__(self):
        return f'{self.name = }, {self.id_ = }, {self.level = }'

    def __hash__(self):
        return hash(self.name) + hash(self.id_)

    def __eq__(self, other):
        return all((self.name == other.name, self.id_ == other.id_))

    def create_user(self, name_, id_, level_):
        if self.level < level_:
            raise Exception(f'Пользователь с уровнем {self.level} не может создавать пользователя с уровнем {level_}')
        else:
            return User(name_, id_, level_)


def load_json(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def worker():
    while True:
        try:
            name = input('Введите имя: ')
            the_id = int(input('Введите личный идентификатор: '))
            level = int(input('Введите уровень доступа: '))
            return User(name, the_id, level)
        except ValueError as e:
            print(e)


def save_json(path, _user_db):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(_user_db, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    PATH = 'my_json.json'
    user_db = load_json(PATH)
    new_user = worker()
    if str(new_user.id_) in user_db:
        raise Exception('Пользователь с этим ID уже записан в базу')
    else:
        user_db[new_user.id_] = {'name': new_user.name, 'level': new_user.level}
        save_json(PATH, user_db)
