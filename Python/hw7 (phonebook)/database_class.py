class Database:
    path = ''
    database = []
    pattern = ('lastname', 'firstname', 'phone', 'comment')
    saved = False

    def __init__(self):
        pass

    def open(self, path: str):
        self.path = path
        with open(self.path, 'r', encoding='UTF-8') as file:
            file_data = file.readlines()
            for line in file_data:
                line = line.strip().split(';')
                user_dict = dict()
                for key, value in zip(self.pattern, line):
                    user_dict[key] = value
                self.database.append(user_dict)
        return True

    def load_success(self):
        if self.database:
            return True
        else:
            return False

    def status(self):
        if self.path:
            if self.database and not self.saved:
                return 'Файл успешно загружен.'
            elif not self.database and not self.saved:
                return 'Файл успешно загружен, но он пуст.'
            elif self.database and self.saved:
                return 'Файл успешно сохранен.'
        else:
            return 'Файл не был загружен.'

    def save(self):
        if self.load_success():
            with open(self.path, 'w', encoding='UTF-8') as file:
                for user in self.database:
                    line = ';'.join(user.values())
                    file.write(line + '\n')
            self.saved = True
            return True
        else:
            return False

    def get_all(self):
        if self.load_success():
            return self.database

    def get_contact(self, index: int):
        if self.load_success():
            return self.database[index]

    def add(self, new_contact: dict):
        if self.load_success():
            self.database.append(new_contact)
            self.saved = False
            return True
        else:
            return False

    def remove(self, index: int):
        if self.database[index]:
            self.database.pop(index)
            return True
        else:
            return False
