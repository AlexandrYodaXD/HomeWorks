import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.TreeMap;

public class Phonebook {
    TreeMap<String, LinkedList<Integer>> phonebook = new TreeMap<>();

    void add(String name, int number){
        if (phonebook.containsKey(name)){
            phonebook.get(name).add(number);
        }else {
            LinkedList<Integer> list = new LinkedList<>();
            list.add(number);
            phonebook.put(name,list);
        }
    }

    void showByName(String name){
        if (phonebook.containsKey(name)){
            System.out.printf("=========Записи по \"%s\"=========\n", name);
            int count = 0;
            for (int number : phonebook.get(name)){
                System.out.printf("\t%d. %d\n", ++count, number);
            }
            System.out.println("============Конец списка===========");
        }else {
            System.out.printf("По \"%s\" не найдено ни одной записи.%n", name);
        }
    }

    void showAll(){
        if (!phonebook.isEmpty()){
            System.out.println("============Все записи===========");
            for (String name : phonebook.keySet()) {
                System.out.println(name + ":");
                int count = 0;
                for (int number : phonebook.get(name)){
                    System.out.printf("\t%d. %d\n", ++count, number);
                }
            }
            System.out.println("============Конец списка===========");
        }else {
            System.out.println("Телефонный справочник пуст.");
        }
    }
}
