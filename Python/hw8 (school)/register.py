class Register():
    _register_dict = dict()
    _path = ''
    _unsaved_changes = False

    def __len__(self):
        return len(self._register_dict)

    def __getitem__(self, item):
        if item in self._register_dict:
            return self._register_dict[item]
        else:
            raise IndexError("Неверный индекс")

    def open(self, path: str):
        self._path = path
        with open(self._path, 'r', encoding='UTF-8') as file:
            file_data = file.readlines()
        # parsing & filling part
        for subject in file_data:
            cut_place = subject.find(': [')
            key = subject[:cut_place].strip()
            value = subject[cut_place + 1:].strip()
            for c in ',[]{}':
                value = value.strip(c)
            value = value.split('}, {')
            students_lst = []
            for i in range(len(value)):
                student_dict = dict()
                student_str = value[i]
                cut_place = student_str.find(',')
                fullname_part = student_str[:cut_place]
                fullname_part = fullname_part.split(': ')
                student_dict[fullname_part[0]] = fullname_part[1]
                marks_part = student_str[cut_place + 1:]
                marks_part = marks_part.strip().split(': ')
                marks_part[1] = [int(x) for x in marks_part[1] if x.isdigit()]
                student_dict[marks_part[0]] = marks_part[1]
                students_lst.append(student_dict)
            self._register_dict[key] = students_lst
        return True

    def save(self):
        with open(self._path, 'w', encoding='UTF-8') as file:
            data_lst = []
            for k, v in self._register_dict.items():
                line = f'{k}: {v}'.replace("'", "")
                data_lst.append(line)
            file.write(',\n'.join(data_lst))
        self._unsaved_changes = False
        return True

    def get_all(self):
        return self._register_dict

    def get_subjects(self):
        return self._register_dict.keys()

    def get_status(self):
        if self._path:
            if self._unsaved_changes:
                return 'opened & changed'
            elif not self._register_dict:
                return 'opened & empty'
            elif self._register_dict:
                return 'opened'
        else:
            return 'not opened'

    def add_mark(self, subject, student_id, mark):
        self._register_dict[subject][student_id]['Оценки'].append(mark)
        self._unsaved_changes = True
        return True

    def pop_mark(self, subject, student_id):
        if self._register_dict[subject][student_id]['Оценки']:
            self._unsaved_changes = True
            return self._register_dict[subject][student_id]['Оценки'].pop()
        else:
            return None

    def find_student_id(self, subject, name):
        list_of_found = []
        for index in range(len(self._register_dict[subject])):
            if name.lower() in self._register_dict[subject][index]['ФИО'].lower():
                list_of_found.append(index)
        return list_of_found

    def is_changed(self):
        return self._unsaved_changes
