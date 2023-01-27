import register
import user_interaction as ui

class_register = register.Register()
path = 'class registers\\'
menu_log = ['not opened']
current_subject = ''
current_student_id = None


def input_handler(user_input: str):
    global path
    global menu_log
    global current_subject
    global current_student_id
    match user_input:
        # not opened
        case 'Открыть классный журнал':
            registers = ui.get_registers(path)
            ui.show_registers(registers)
            choice = ui.input_validator(int, 'Выберите журнал >: ', len(registers)) - 1
            register_choice = registers[choice]
            path = 'class registers\\'
            file_path = path + register_choice
            if class_register.open(file_path):
                ui.user_informing('OK', f'Открыт журнал [{register_choice}].')
                status = class_register.get_status()
                if status == 'opened':
                    menu_log.append('opened & no subject chosen')

        case 'Завершение работы':
            ui.user_informing('OK', 'Программа завершила работу.')
            exit()

        # opened & no subject chosen
        case 'Выбрать предмет' | 'Выбрать другой предмет':
            subjects = list(class_register.get_subjects())
            ui.show_enumerated_collection(subjects)
            choice = ui.input_validator(int, 'Выберите предмет >: ', len(subjects)) - 1
            current_subject = subjects[choice]
            ui.user_informing('OK', current_subject)
            menu_log.append('opened & subject chosen')

        case 'Показать все предметы, всех учеников и все их оценки':
            subjects_list = list(class_register.get_all().keys())
            ui.show_all_students_by_subjects(class_register, subjects_list)

        case 'Показать всех учеников, все предметы и оценки по ним':
            ui.show_all_subjects_by_all_students(class_register)

        case 'Закрыть текущий журнал':
            if class_register.is_changed():
                ui.user_informing('!', 'Имеются несохраненные изменения. Сохранить?')
                answer = ui.input_validator(bool)
                if answer:
                    class_register.save()
            menu_log.clear()
            menu_log.append('not opened')

        # opened & subject chosen
        case 'Показать всех учеников и их оценки по текущему предмету':
            ui.show_all_students_by_subjects(class_register, current_subject)

        case 'Управление оценками':
            menu_log.append('assessment management')

        # assessment management
        case 'Найти и выбрать ученика':
            current_student_id = ui.get_assessed_student(class_register, current_subject)
            if current_student_id is not None:
                menu_log.append('assessment management for student')

        # assessment management for student
        case 'Показать ФИО и оценки ученика':
            ui.show_student_by_subject(class_register, current_subject, current_student_id)

        case 'Добавить оценку':
            new_mark = ui.input_validator(int, 'Введите оценку (1-5) >: ', 5)
            if class_register.add_mark(current_subject, current_student_id, new_mark):
                ui.user_informing('OK', f'Оценка {new_mark} добавлена.')
            else:
                ui.user_informing('!!', 'Ошибка при добавлении оценки. Эта ошибка не должна была возникнуть.')

        case 'Удалить последнюю оценку':
            last_mark = class_register.pop_mark(current_subject, current_student_id)
            if last_mark:
                ui.user_informing('OK', f'Последняя оценка "{last_mark}" удалена.')
            else:
                ui.user_informing('!', 'Невозможно удалить последнюю оценку, оценки отсутствуют.')

        case 'Назад':
            previous_menu = menu_log.pop()
            if previous_menu == 'assessment management for student':
                current_student_id = None


def start():
    while True:
        menu_size = len(ui.menu_dict[menu_log[-1]])
        ui.show_menu(menu_log[-1])
        action_idx = ui.input_validator(int, 'Введите команду >: ', menu_size) - 1
        action_str = ui.menu_dict[menu_log[-1]][action_idx]
        ui.user_informing('>>', action_str)
        input_handler(action_str)
