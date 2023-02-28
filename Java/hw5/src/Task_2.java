import java.util.*;

/*
Пусть дан список сотрудников:
Иван Иванов,
Светлана Петрова,
Кристина Белова,
Анна Мусина,
Анна Крутова,
Иван Юрин,
Петр Лыков,
Павел Чернов,
Петр Чернышов,
Мария Федорова,
Марина Светлова,
Мария Савина,
Мария Рыкова,
Марина Лугова,
Анна Владимирова,
Иван Мечников,
Петр Петин,
Иван Ежов.
Написать программу, которая найдет и выведет повторяющиеся имена с количеством повторений.
Отсортировать по убыванию популярности. Для сортировки использовать TreeMap.
 */
public class Task_2 {
    public static void main(String[] args) {
        String data = "Иван Иванов,\n" +
                "Светлана Петрова,\n" +
                "Кристина Белова,\n" +
                "Анна Мусина,\n" +
                "Анна Крутова,\n" +
                "Иван Юрин,\n" +
                "Петр Лыков,\n" +
                "Павел Чернов,\n" +
                "Петр Чернышов,\n" +
                "Мария Федорова,\n" +
                "Марина Светлова,\n" +
                "Мария Савина,\n" +
                "Мария Рыкова,\n" +
                "Марина Лугова,\n" +
                "Анна Владимирова,\n" +
                "Иван Мечников,\n" +
                "Петр Петин,\n" +
                "Иван Ежов.";

        LinkedList<String> parsedData = parsingNames(data);

        System.out.println("unsortedMap");
        TreeMap<String, Integer> unsortedMap = getFillingMap(parsedData);
        System.out.println(unsortedMap);

        TreeMap<String, Integer> sortedMap = getSortedByValue(unsortedMap);
        System.out.println("sortedMap");
        System.out.println(sortedMap);
    }

    static LinkedList<String> parsingNames(String data) {
        LinkedList<String> list = new LinkedList<>();
        String[] dataArr = data.replaceAll(",", "")
                .replaceAll("\\.", "")
                .split("\n");
        for (String fullName :
                dataArr) {
            list.add(fullName.split(" ")[0]);
        }
        return list;
    }

    static TreeMap<String, Integer> getFillingMap(LinkedList<String> data) {
        TreeMap<String, Integer> map = new TreeMap<String, Integer>() {
        };
        for (String name : data) {
            if (map.containsKey(name)) {
                map.put(name, map.get(name) + 1);
            } else {
                map.put(name, 1);
            }
        }
        return map;
    }

    static TreeMap<String, Integer> getSortedByValue(TreeMap<String, Integer> unsortedMap) {
        ValueComparator vc = new ValueComparator(unsortedMap);
        TreeMap<String, Integer> sortedMap = new TreeMap<String, Integer>(vc) {};
        sortedMap.putAll(unsortedMap);
        return sortedMap;
    }
}