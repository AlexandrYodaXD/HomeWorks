import user_interaction as ui
from database_class import Database


phonebook = Database()


def start():
    while True:
        action = ui.main_menu()
        input_handler(action)


def input_handler(user_input: str):
    match user_input:
        case 'Открыть файл':
            phonebook.open('database.txt')
            ui.show_file_status(phonebook)
        case 'Сохранить файл':
            ui.save_file(phonebook)
        case 'Показать все контакты':
            ui.show_all_contacts(phonebook)
        case 'Создать контакт':
            ui.create_new_contact(phonebook)
        case 'Найти контакт':
            ui.search(phonebook)
        case 'Удалить контакт':
            ui.remove_contact(phonebook)
        case 'Выход':
            ui.exit_program()
