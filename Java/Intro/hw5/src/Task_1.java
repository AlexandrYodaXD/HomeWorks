import java.util.HashMap;
import java.util.LinkedList;

/*
Реализуйте структуру телефонной книги с помощью HashMap, учитывая, что 1 человек может иметь несколько телефонов.
 */
public class Task_1 {
    public static void main(String[] args) {
        Phonebook phonebook = new Phonebook();
        phonebook.showAll(); // Телефонный справочник пуст.
        phonebook.add("Василий", 9324425);
        phonebook.add("Василий", 9324426);
        phonebook.add("Николай", 9955332);
        phonebook.showAll();
        phonebook.showByName("Игорь"); // По "Игорь" не найдено ни одной записи.
        phonebook.showByName("Василий");

    }
}
