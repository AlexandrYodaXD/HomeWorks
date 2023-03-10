import Animal.Animal;
import Animal.petAnimal.Cat.Cat;
import Animal.petAnimal.Dog.Dog;
import Zoo.Zoo;

import java.time.LocalDate;
import java.util.*;

public class Program {
    public static void main(String[] args) {
        Zoo zoo = new Zoo();
        zoo.add(new Cat(25, 5, "зеленый", "Белка", "Ангорская", true,
                "Белый", LocalDate.of(2018, 4, 13), true));
        zoo.add(new Dog(62, 35, "желтый", "Мухтар", "немецкая овчарка", true,
                "черно-бежевый", LocalDate.of(2015, 5, 11), false));

        Scanner scanner = new Scanner(System.in);
        workWithZoo(scanner, zoo);

    }

    static void workWithZoo(Scanner scanner, Zoo zoo) {

        while (true) {
            System.out.println("Главное меню виртуального зоопарка \"Мартышкин труд\"");
            System.out.println("\t1. Добавить животное в зоопарк");
            System.out.println("\t2. Убрать животное из зоопарка");
            System.out.println("\t3. Посмотреть информацию о животном");
            System.out.println("\t4. Заставить животное издать звук");
            System.out.println("\t5. Напечатать информацию о животных в зоопарке");
            System.out.println("\t6. Заставить всех животных издать звук");
            System.out.println("\t0. Выход");
            System.out.println("Выбери действие >: ");

            int input = scanner.nextInt();

            switch (input){
                case 1:
                    getAnimalToAdd(scanner, zoo);
                case 0:
                    System.out.println("Досвидания! Приходи ещё!");
                    return;
            }
        }
    }

    static void getAnimalToAdd(Scanner scanner, Zoo zoo) {
        System.out.println("Меню добавления животного");
        System.out.println("\t1. Добавить кошку");
        System.out.println("\t2. Добавить собаку");
        System.out.println("\t3. Добавить волка");
        System.out.println("\t4. Добавить тигра");
        System.out.println("\t5. Добавить курицу");
        System.out.println("\t6. Добавить аиста");
        System.out.println("\t0. Отмена");
        System.out.println("Выбери действие >: ");

        HashMap<String, Object> properties = new HashMap<>();
        int input = scanner.nextInt();

        switch (input){
            case 1:
                properties.putAll(getAnimalProperties(scanner));
                properties.putAll(getPetProperties(scanner));
                properties.putAll(getCatProperties(scanner));
                zoo.add(getNewCat(properties));
            case 2:
                properties.putAll(getAnimalProperties(scanner));
                properties.putAll(getPetProperties(scanner));
                properties.putAll(getDogProperties(scanner));
                zoo.add(getNewDog(properties));

            case 0:
                System.out.println("До свидания!");
                return;
        }
    }

    static HashMap<String, Object> getAnimalProperties(Scanner scanner){
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Введи высоту животного: ");
        map.put("growth", scanner.nextInt());
        System.out.print("Введи вес животного: ");
        map.put("weight", scanner.nextInt());
        System.out.print("Введи цвет глаз животного: ");
        map.put("eyeColor", scanner.next());
        return map;
    }

    static HashMap<String, Object> getPetProperties(Scanner scanner){
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Введи кличку животного: ");
        map.put("name", scanner.next());
        System.out.print("Введи породу: ");
        map.put("breed", scanner.next());
        System.out.print("Введи вакцинированно ли животное (да/нет): ");
        map.put("vaccinated", scanner.next().equalsIgnoreCase("да"));
        System.out.print("Введи цвет шерсти животного: ");
        map.put("coatColor", scanner.next());
        System.out.print("Введи дату рождения животного (день.месяц.год): ");
        map.put("dateOfBirth", parseDate(scanner.next()));
        return map;
    }

    static HashMap<String, Object> getCatProperties(Scanner scanner){
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Введи наличие шерсти у животного (есть/нет): ");
        map.put("presenceOfWool", scanner.next().equalsIgnoreCase("есть"));
        return map;
    }

    static HashMap<String, Object> getDogProperties(Scanner scanner){
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Введи наличие дрессировки (есть/нет): ");
        map.put("presenceOfWool", scanner.next().equalsIgnoreCase("есть"));
        return map;
    }

    static Animal getNewCat(HashMap<String, Object> properties){
        return new Cat((int) properties.get("growth"),
                (int) properties.get("weight"),
                (String) properties.get("eyeColor"),
                (String) properties.get("name"),
                (String) properties.get("breed"),
                (boolean) properties.get("vaccinated"),
                (String) properties.get("coatColor"),
                (LocalDate) properties.get("dateOfBirth"),
                (boolean) properties.get("presenceOfWool"));
    }

    static Animal getNewDog(HashMap<String, Object> properties){
        return new Cat((int) properties.get("growth"),
                (int) properties.get("weight"),
                (String) properties.get("eyeColor"),
                (String) properties.get("name"),
                (String) properties.get("breed"),
                (boolean) properties.get("vaccinated"),
                (String) properties.get("coatColor"),
                (LocalDate) properties.get("dateOfBirth"),
                (boolean) properties.get("trained"));
    }

    static LocalDate parseDate(String date){
        String[] dateArr = date.split("\\.");
        int day = Integer.parseInt(dateArr[0]);
        int month = Integer.parseInt(dateArr[1]);
        int year = Integer.parseInt(dateArr[2]);
        return LocalDate.of(day, month, year);
    }
}

