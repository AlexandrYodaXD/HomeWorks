from user_class import User, load_json, save_json


class Logger:
    PATH: str
    db: dict
    users: dict

    def __new__(cls, path):
        cls.PATH = path
        cls.db = dict()
        cls.users = dict()
        instance = super().__new__(cls)
        return instance

    def __init__(self, path):
        self.__class__.db = load_json(path)
        self.level = None
        self.loader()

    def authorize(self, the_id, name):
        user = User(name, the_id)
        for obj in self.__class__.users.values():
            if user == obj:
                self.level = self.__class__.db[str(the_id)]['level']
                return self.level
        else:
            raise PermissionError('Пользователь с такими данными не найден')

    def loader(self):
        for _id in Logger.db:
            _name = self.__class__.db[_id]['name']
            _the_id = int(_id)
            _level = self.__class__.db[_id]['level']
            self.__class__.users[_the_id] = User(_name, _the_id, _level)

    def create_user(self, _name, _the_id, _level):
        if self.level <= _level:
            raise ValueError(f'Пользователь с уровнем {self.level} не может создавать пользователя с уровнем {_level}')
        else:
            new_user = User(_name, _the_id, _level)
            self.__class__.users[_the_id] = new_user
            self.__class__.db[str(_the_id)] = {'name': _name, 'level': _level}
            save_json(self.__class__.PATH, self.__class__.db)
            return new_user
