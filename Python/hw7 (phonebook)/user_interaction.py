def file_status_decorator(func):
    def a_wrapper_accepting_arguments(db, *args, **kwargs):
        file_status = db.status()
        if file_status == 'Файл успешно загружен.':
            return func(db, *args, **kwargs)
        else:
            print(file_status)
            return None

    return a_wrapper_accepting_arguments


def input_validator(message: str, data_type: type, size=None):
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
    if data_type == str:
        return input('Введите команду >: ')


def main_menu():
    print('=====Главное меню=====')
    main_menu_list = [
        'Открыть файл',
        'Сохранить файл',
        'Показать все контакты',
        'Создать контакт',
        'Найти контакт',
        'Удалить контакт',
        'Выход',
    ]
    size = len(main_menu_list)
    for i in range(size):
        print(f'\t{i + 1}. {main_menu_list[i]}')
    user_input = input_validator('Введи команду >: ', int, size)
    print(f'>> {main_menu_list[user_input - 1]}')
    return main_menu_list[user_input - 1]


def contact_menu():
    contact_menu_list = [
        'Изменить контакт',
        'Удалить контакт',
        'Главное меню',
        'Выход',
    ]


def show_file_status(db):
    print(db.status())


@file_status_decorator
def show_contact(db, index: int):
    contact = db.get_contact(index)
    print(f'\t{1}', end='. ')
    print(' '.join(contact.values()))


@file_status_decorator
def show_all_contacts(db):
    all_contacts = db.get_all()
    for i in range(len(all_contacts)):
        print(f'\t{i + 1}', end='. ')
        print(' '.join(all_contacts[i].values()))


@file_status_decorator
def create_new_contact(db):
    new_contact = dict.fromkeys(db.pattern)
    for key in new_contact.keys():
        new_contact[key] = input(f'\tВведите {ru_dict[key][3]} >: ').capitalize()
    if db.add(new_contact):
        print('Контакт успешно создан.')


@file_status_decorator
def remove_contact(db):
    show_all_contacts(db)
    size = len(db.get_all())
    idx = input_validator('Введите номер контакта для удаления >: ', int, size) - 1
    print('Вы хотите удалить этот контакт?')
    show_contact(db, idx)
    user_choice = input_validator('[1] да, [2] нет >: ', int, 2)
    if user_choice == 1:
        if db.remove(idx):
            print('Контакт успешно удалён.')
        else:
            print('Ошибка при удалении контакта.')
    elif user_choice == 2:
        pass


@file_status_decorator
def search(db):
    print('=====Поиск контакта=====')
    all_contacts = db.get_all()
    criterion = db.pattern
    size = len(criterion)
    for i in range(size):
        print(f'{i + 1}. По {ru_dict[criterion[i]][2]}.')
    else:
        print(f'{size + 1}. По всем полям.')
    search_choice = input_validator('Введи команду >: ', int, size + 1) - 1
    what_search = input('Введите что требуется найти :> ').lower()
    searched_list = []
    if search_choice in range(len(criterion)):
        for idx in range(len(all_contacts)):
            if what_search in all_contacts[idx][criterion[search_choice]].lower():
                searched_list.append(idx)
    elif search_choice == len(criterion):
        for idx in range(len(all_contacts)):
            for c in range(len(criterion)):
                if what_search in all_contacts[idx][criterion[c]].lower():
                    searched_list.append(idx)
                    break
    print(f'Найдено {len(searched_list)} контакта(-ов).')
    for idx in searched_list:
        show_contact(db, idx)


@file_status_decorator
def save_file(db):
    if db.save():
        print('Файл успешно сохранен.')


def exit_program():
    print('Завершение программы.')
    exit()


ru_dict = {
    'lastname': ('фамилия', 'фамилии', 'фамилии', 'фамилию', 'фамилией', 'о фамилии', 'по фамилии'),
    'firstname': ('имя', 'имени', 'имени', 'имя', 'именем', 'об имени', 'в имени'),
    'phone': ('телефон', 'телефона', 'телефону', 'телефон', 'телефоном', 'о телефоне', 'в телефоне'),
    'comment': ('комментарий', 'комментария', 'комментарию', 'комментарий', 'комментарием',
                'о комментарии', 'в комментарии'),
}
