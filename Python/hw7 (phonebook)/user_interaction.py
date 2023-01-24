main_menu_list = [
    'Считать файл',
    'Сохранить файл',
    'Показать статус файла',
    'Показать все контакты',
    'Найти контакт',
    'Создать контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход',
]
ru_dict = {
    'lastname': ('фамилия', 'фамилии', 'фамилии', 'фамилию', 'фамилией', 'о фамилии', 'по фамилии'),
    'firstname': ('имя', 'имени', 'имени', 'имя', 'именем', 'об имени', 'в имени'),
    'phone': ('телефон', 'телефона', 'телефону', 'телефон', 'телефоном', 'о телефоне', 'в телефоне'),
    'comment': ('комментарий', 'комментария', 'комментарию', 'комментарий', 'комментарием',
                'о комментарии', 'в комментарии'),
}


def show_main_menu():
    print('================================Главное меню================================')
    menu_lst = []
    for i in range(len(main_menu_list)):
        menu_lst.append(f'[{i + 1}] {main_menu_list[i]}')
    print(f'{menu_lst[0]}          | {menu_lst[1]}  | {menu_lst[2]}')
    print(f'{menu_lst[3]} | {menu_lst[4]}   | {menu_lst[5]}')
    print(f'{menu_lst[6]}      | {menu_lst[7]} | {menu_lst[8]}')


def user_informing(prefix: str, message: str):
    print(f'[{prefix}] {message}')


def file_has_been_read(func):
    '''Рудимент. Декоратор, который я использовал чтобы действия,
    требовавшие чтобы файл был открыт, не вызывали исключения.
    В текущей реализации проверки происходят в контроллере'''

    def wrapper(db, *args, **kwargs):
        file_status = db.status()
        if file_status != 'Файл не был загружен.':
            return func(db, *args, **kwargs)
        else:
            print(file_status)
            return None

    return wrapper


def input_validator(data_type: type, message: str = '', size=None) -> int | str | bool:
    '''Валидатор пользовательского ввода'''
    if data_type == int:
        while True:
            user_input = input(message)
            while not user_input.isdigit():
                print('ОШИБКА: Необходимо указать число.')
                break
            else:
                user_input = int(user_input)
                if not size:
                    return user_input
                else:
                    while not 0 < user_input <= size:
                        print('ОШИБКА: Необходимо указать существующий пункт меню.')
                        break
                    else:
                        return user_input

    elif data_type == bool:
        while True:
            user_input = input('[1] да, [2] нет >: ').lower()
            while user_input not in ('1', '2', 'да', 'нет'):
                print('ОШИБКА: Необходимо указать 1/2 или да/нет.')
                break
            else:
                if user_input in ('1', 'да'):
                    return True
                else:
                    return False

    elif data_type == str:
        return input('Введите команду >: ')


@file_has_been_read
def show_contact(db, index: int):
    '''Отображение пользователю одного контакта по его индексу в БД'''
    contact = db.get_contact(index)
    print(f'\tid: {index + 1}', end='. ')
    print(' '.join(contact.values()))


@file_has_been_read
def show_contacts(db, contacts_list: list):
    '''Отображение пользователю нескольких контактов по их индексам в БД'''
    for index in contacts_list:
        show_contact(db, index)


@file_has_been_read
def show_all_contacts(db):
    '''Отображение пользователю всех контактов'''
    print('================================Все контакты================================')
    all_contacts = db.get_all()
    if all_contacts:
        for i in range(len(all_contacts)):
            print(f'\tid: {i + 1}', end='. ')
            print(' '.join(all_contacts[i].values()))


@file_has_been_read
def create_new_contact(db) -> dict:
    '''Создание словаря с новым контактом'''
    print('==============================Создание контакта=============================')
    new_contact = dict.fromkeys(db.fields)
    for key in new_contact.keys():
        new_contact[key] = input(f'\tВведите {ru_dict[key][3]} >: ').capitalize()
    print('Контакт успешно создан.')
    return new_contact


@file_has_been_read
def get_contact_for_remove(db) -> int:
    '''Запрос контакта на удаление'''
    print('==============================Удаление контакта=============================')
    size = len(db.get_all())
    if size > 0:
        show_all_contacts(db)
        idx = input_validator(int, 'Введите номер контакта для удаления >: ', size) - 1
        print('Вы хотите удалить этот контакт?')
        show_contact(db, idx)
        user_choice = input_validator(bool)
        if user_choice == 1:
            return idx
        elif user_choice == 2:
            pass
    else:
        return -1


@file_has_been_read
def get_contact_for_change(db):
    '''Запрос контакта на изменение'''
    print('=============================Изменение контакта=============================')
    size = len(db.get_all())
    return_lst = []
    if size > 0:
        show_all_contacts(db)
        idx = input_validator(int, 'Введите номер контакта для изменения >: ', size) - 1
        print('Вы хотите изменить этот контакт?')
        show_contact(db, idx)
        user_choice = input_validator(bool)
        if user_choice:
            return_lst.append(idx)
            fields = db.get_pattern()
            for i in range(len(fields)):
                print(f'{i + 1}. {ru_dict[fields[i]][3].capitalize()}.')
            field_choice = input_validator(int, 'Введи команду >: ', size) - 1
            field = fields[field_choice]
            changing_for = input('Введите на что требуется изменить :> ').capitalize()
            return idx, field, changing_for
        else:
            pass
    else:
        return -1


# @file_has_been_read
def get_looking_for(db):
    '''Запрос контакта на поиск'''
    print('===============================Поиск контакта===============================')
    all_contacts = db.get_all()
    if all_contacts:
        fields = db.get_pattern() + ('All',)
        size = len(fields)
        for i in range(size - 1):
            print(f'{i + 1}. По {ru_dict[fields[i]][2]}.')
        else:
            print(f'{size}. По всем полям.')
        field_choice = input_validator(int, 'Введи команду >: ', size) - 1
        search_field = fields[field_choice]
        looking_for = input('Введите что требуется найти :> ').lower()
        return looking_for, search_field
    else:
        return -1, -1


def get_action_on_unsaved(bd):
    '''При имеющихся несохраненных изменениях запрашивает и возвращает булево значение.
    Если изменений не было, то возвращает True'''
    if bd.status() == 'Имеются несохраненные изменения.':
        user_informing('!!', 'Имеются несохраненные изменения.')
        user_informing('?', 'Продолжить без сохранения изменений?')
        user_input = input_validator(bool)
        return user_input
    else:
        return True


def opened_and_filled(bd):
    not_loaded = bd.status() == 'Файл не был загружен.'
    empty_bd = len(bd) == 0
    if not_loaded:
        user_informing('!!', 'Файл не был загружен.')
    if empty_bd:
        user_informing('!!', 'Записная книга пуста.')
    if any((not_loaded, empty_bd)):
        return False
    else:
        return True
