import user_interaction as ui
from database_class import Database

phonebook = Database()
main_menu_size = len(ui.main_menu_list)
file_path = 'database.txt'


def input_handler(user_input: str):
    match user_input:
        case 'Считать файл':
            if ui.get_action_on_unsaved(phonebook):
                if phonebook.open(file_path):
                    ui.user_informing('OK', phonebook.status())
                else:
                    ui.user_informing('!!', phonebook.status())

        case 'Сохранить файл':
            if phonebook.save():
                ui.user_informing('OK', 'Файл был успешно сохранен.')
            else:
                ui.user_informing('!!', 'Ошибка при сохранении файла.')

        case 'Показать все контакты':
            if ui.opened_and_filled(phonebook):
                ui.show_all_contacts(phonebook)

        case 'Создать контакт':
            new_contact = ui.create_new_contact(phonebook)
            if phonebook.add(new_contact):
                ui.user_informing('OK', 'Контакт успешно создан.')
            else:
                ui.user_informing('!!', 'Ошибка при создании контакта.')

        case 'Найти контакт':
            if ui.opened_and_filled(phonebook):
                looking_for, search_field = ui.get_looking_for(phonebook)
                search_result = phonebook.find(looking_for, search_field)
                if search_result:
                    ui.show_contacts(phonebook, search_result)
                else:
                    ui.user_informing('!', 'Контактов по указанному критерию не найдено.')

        case 'Изменить контакт':
            if ui.opened_and_filled(phonebook):
                idx, field, changing_for = ui.get_contact_for_change(phonebook)
                if phonebook.change(idx, field, changing_for):
                    ui.user_informing('OK', 'Контакт успешно изменен.')
                else:
                    ui.user_informing('!!', 'При изменении контакта произошла ошибка.')

        case 'Удалить контакт':
            if ui.opened_and_filled(phonebook):
                contact_id = ui.get_contact_for_remove(phonebook)
                if phonebook.remove(contact_id):
                    ui.user_informing('OK', 'Контакт успешно удалён.')
                else:
                    ui.user_informing('!!', 'Ошибка при удалении контакта.')
                    if len(phonebook) == 0:
                        ui.user_informing('!!', 'Записная книга пуста.')

        case 'Показать статус файла':
            ui.user_informing('!', phonebook.status())

        case 'Выход':
            if ui.get_action_on_unsaved(phonebook):
                ui.user_informing('OK', 'Завершение программы.')
                exit()


def start():
    while True:
        ui.show_main_menu()
        action_idx = ui.input_validator(int, 'Введите команду >: ', main_menu_size) - 1
        action_str = ui.main_menu_list[action_idx]
        ui.user_informing('>>', action_str)
        input_handler(action_str)
