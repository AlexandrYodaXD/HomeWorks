import os

menu_dict = {
    'not opened': (
        'Открыть классный журнал',
        'Завершение работы',
    ),
    'opened & no subject chosen': (
        'Выбрать предмет',
        'Показать все предметы, всех учеников и все их оценки',
        'Показать всех учеников, все предметы и оценки по ним',
        'Закрыть текущий журнал',
    ),
    'opened & subject chosen': (
        'Показать всех учеников и их оценки по текущему предмету',
        'Управление оценками',
        'Выбрать другой предмет',
        'Закрыть текущий журнал',

    ),
    'assessment management': (
        'Найти и выбрать ученика',
        'Назад',
    ),
    'assessment management for student': (
        'Показать ФИО и оценки ученика',
        'Добавить оценку',
        'Удалить последнюю оценку',
        'Назад',
    ),
    'opened & changed': (
        'Показать всех учеников и их оценки по текущему предмету',
        'Контроль знаний ученика',
        'Сохранить изменения',
        'Закрыть текущий журнал',
    ),
    'opened & empty': (
        'Закрыть текущий журнал',
    )
}


def show_menu(menu: str):
    for item in enumerate(menu_dict[menu], 1):
        print(f'\t{item[0]}. {item[1]}.')


def get_registers(path: str):
    '''Возвращает все файлы. Возможно, перемудрил и можно было проще.'''
    run_path = os.path.abspath(__file__)  # получение абсолютного пути запущенного скрипта
    dir_path = run_path[:run_path.rindex('\\') + 1]  # вычленение папки с запущенным скриптом
    class_registers_dir = dir_path + '\\' + path
    dir_content = os.listdir(class_registers_dir)
    return [x for x in dir_content if x[-4:].lower() == '.txt']


def show_registers(registers):
    '''Вывод доступных журналов'''
    if registers:
        user_informing('OK', 'Доступные журналы:')
        for item in enumerate(registers, 1):
            print(f'\t{item[0]}. {item[1]}')
    else:
        user_informing('!!', 'Журналы отсутствуют.')


def show_enumerated_collection(collection):
    '''Вывод пронумерованных элементов итерируемых объектов'''
    for item in enumerate(collection, 1):
        print(f'\t{item[0]}. {item[1]}')


def user_informing(prefix: str, message: str):
    '''Информирование пользователя. Эмуляция/симуляция интерфейса графического отображения.'''
    print(f'[{prefix}] {message}')


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


def show_student_by_subject(reg, subject, student_id, sym=''):
    '''Показывает выбранного студента по выбранному предмету'''
    full_name = reg[subject][student_id]['ФИО']
    marks = reg[subject][student_id]['Оценки']
    if marks:
        marks_str = ', '.join([str(x) for x in marks])
        average_mark = round(sum(marks) / len(marks), 2)
    else:
        marks_str = 'Отсутствуют.'
        average_mark = 'Отсутствует.'
    print(f'{sym}\tФИО:', full_name, '\n',
          f'{sym}\tСредняя оценка по предмету "{subject}": {average_mark}\n',
          f'{sym}\tВсе оценки по предмету "{subject}": {marks_str}\n', sep='', end='')


def show_all_students_by_subjects(reg, subjects: str | list):
    '''Показывает всех студентов по выбранному предмету или списку предметов'''
    if isinstance(subjects, str):
        subjects = [subjects]

    for subject in subjects:
        print('╔' + '═'*63)
        print(f'║{subject}:')
        print('╠' + '═' * 63)
        students_list = reg[subject]
        for student_id in range(len(reg[subject])):
            show_student_by_subject(reg, subject, student_id, sym='║')
            if student_id != len(reg[subject]) - 1:
                print('╟' + '─' * 63)
        print('╚' + '═'*63)

def show_all_subjects_by_all_students(reg):
    '''Показывает все предметы, по предметам показывает всех учеников и их оценки'''
    register = reg.get_all()
    students_dict = dict()
    for subj, lst in register.items():
        for stud in lst:
            full_name = stud['ФИО']
            marks = stud['Оценки']
            students_dict.setdefault(full_name, [])
            my_dict = {
                'Предмет': subj,
                'Оценки': marks
            }
            students_dict[full_name].append(my_dict)
    # код ниже за исключением переменных повторяется в функции show_all_students_by_subjects
    # стоило бы переделать...
    for student, lst in students_dict.items():
        print('╔' + '═' * 63)
        print(f'║{student}:')
        print('╠' + '═' * 63)
        for subj_index in range(len(lst)):
            subj = lst[subj_index]
            subject = subj['Предмет']
            marks = subj['Оценки']
            marks_str = ', '.join([str(x) for x in marks])
            average_mark = round(sum(marks) / len(marks), 2)
            print('║\tПредмет:', subject, '\n',
                  '║\tСредняя оценка:', average_mark, '\n',
                  '║\tВсе оценки:', marks_str, '\n', sep='', end='')
            if subj_index != len(lst) - 1:
                print('╟' + '─' * 63)
        print('╚' + '═'*63)


def get_assessed_student(reg, current_subject):
    '''Получение ID студента по выбранному предмету'''
    find_answer = input('Введите полностью или частично ФИО отвечающего >: ')
    list_of_found = reg.find_student_id('Русский язык', find_answer)
    list_of_found_size = len(list_of_found)
    if list_of_found_size == 0:
        user_informing('!!', 'По указанному критерию учеников не найдено.')
        return None
    elif list_of_found_size == 1:
        index = list_of_found[0]
        full_name = reg[current_subject][index]['ФИО']
        marks = reg[current_subject][index]['Оценки']
        user_informing('OK', 'Найден ученик: ' + full_name)
        return index
    else:
        user_informing('!', f'Найдено {list_of_found_size} учеников:')
        for index in list_of_found:
            full_name = reg[current_subject][index]['ФИО']
            marks = reg[current_subject][index]['Оценки']
            user_informing('>', full_name)
        user_informing('!', 'Необходимо уточнить запрос.')
        return None
