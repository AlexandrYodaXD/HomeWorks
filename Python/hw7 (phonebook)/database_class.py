def load_success_decorator(func):
    def wrapper(self, *args, **kwargs):
        if self.path:
            return func(self, *args, **kwargs)
        else:
            return False

    return wrapper


class Database:
    path = ''
    database = []
    fields = ('lastname', 'firstname', 'phone', 'comment')
    unsaved_changes = False

    def __len__(self):
        return len(self.database)

    def open(self, path: str):
        self.path = path
        self.database = list()
        with open(self.path, 'r', encoding='UTF-8') as file:
            file_data = file.readlines()
            for line in file_data:
                line = line.strip().split(';')
                user_dict = dict()
                for key, value in zip(self.fields, line):
                    user_dict[key] = value
                self.database.append(user_dict)
        self.unsaved_changes = False
        return True

    def status(self):
        if self.path:
            if self.unsaved_changes:
                return 'Имеются несохраненные изменения.'
            elif not self.database:
                return 'Файл был успешно загружен, но он пуст.'
            elif self.database:
                return 'Файл был успешно загружен.'
        else:
            return 'Файл не был загружен.'

    @load_success_decorator
    def save(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            for user in self.database:
                line = ';'.join(user.values())
                file.write(line + '\n')
        self.unsaved_changes = False
        return True

    @load_success_decorator
    def get_all(self):
        return self.database

    @load_success_decorator
    def get_contact(self, index: int):
        return self.database[index]

    def get_pattern(self):
        return self.fields

    @load_success_decorator
    def add(self, new_contact: dict):
        self.database.append(new_contact)
        self.unsaved_changes = True
        return True

    @load_success_decorator
    def remove(self, index: int):
        if 0 <= index < len(self.database):
            self.database.pop(index)
            self.unsaved_changes = True
            return True
        else:
            return False

    @load_success_decorator
    def change(self, index: int, field: str, new_data: str):
        self.database[index][field] = new_data
        self.unsaved_changes = True
        return True

    @load_success_decorator
    def find(self, looking_for: str, search_field: str = 'All') -> list:
        list_of_found = []
        if search_field == 'All':
            for idx in range(len(self.database)):
                for c in range(len(self.fields)):
                    if looking_for in self.database[idx][self.fields[c]].lower():
                        list_of_found.append(idx)
                        break
            return list_of_found
        elif search_field in self.fields:
            for idx in range(len(self.database)):
                if looking_for in self.database[idx][search_field].lower():
                    list_of_found.append(idx)
            return list_of_found
