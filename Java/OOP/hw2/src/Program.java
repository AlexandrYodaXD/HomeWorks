import animal.Animal;
import animal.bird.Fly;
import animal.bird.chicken.Chicken;
import animal.bird.stork.Stork;
import animal.petAnimal.Cat.Cat;
import animal.petAnimal.ShowAffection;
import animal.petAnimal.dog.Dog;
import animal.petAnimal.dog.Train;
import animal.wildAnimal.tiger.Tiger;
import animal.wildAnimal.wolf.Wolf;
import zoo.Zoo;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Program {
    public static void main(String[] args) {
        Zoo zoo = new Zoo();
        zoo.add(new Cat(25, 5, "зеленый", "Белка", "Ангорская", true,
                "Белый", LocalDate.of(2018, 4, 13), true));
        zoo.add(new Dog(62, 35, "оранжевый", "Мухтар", "немецкая овчарка",
                true, "черно-бежевый", LocalDate.of(2015, 5, 11), false));
        zoo.add(new Wolf(73, 54, "желтый", "Лес",
                LocalDate.of(2014, 6, 7), true));
        zoo.add(new Tiger(82, 65, "зеленый", "Джунгли",
                LocalDate.of(2013, 2, 4)));
        zoo.add(new Chicken(13, 8, "красный", 1));
        zoo.add(new Stork(33, 18, "бежевый", 112));

        try (Scanner scanner = new Scanner(System.in)) {
            workWithZoo(scanner, zoo);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    static void workWithZoo(Scanner scanner, Zoo zoo) {
        while (true) {
            System.out.println("Главное меню виртуального зоопарка \"Мартышкин труд\"");
            System.out.println("\t1. Посмотреть информацию о конкретном животном");
            System.out.println("\t2. Показать информацию о всех животных в зоопарке");
            System.out.println("\t3. Добавить животное в зоопарк");
            System.out.println("\t4. Удалить животное из зоопарка");
            System.out.println("\t5. Заставить животное издать звук");
            System.out.println("\t6. Заставить всех животных издать звук");
            System.out.println("\t7. Показать кто что может (тест интерфейсов)");
            System.out.println("\t0. Выход");
            System.out.print("Выбери действие >: ");

            int input = scanner.nextInt();

            switch (input) {
                case 1 -> getAnimalToShow(scanner, zoo);
                case 2 -> {
                    System.out.println("Все животные зоопарка:");
                    zoo.showAll();
                }
                case 3 -> getAnimalToAdd(scanner, zoo);
                case 4 -> getAnimalToRemove(scanner, zoo);
                case 5 -> getAnimalForMakeSound(scanner, zoo);
                case 6 -> zoo.makeSoundAll();
                case 7 -> showAllActivities(zoo);
                case 0 -> {
                    System.out.println("До свидания! Приходи ещё!");
                    return;
                }
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
        System.out.print("Выбери действие >: ");

        Map<String, Object> properties = new HashMap<>();
        int input = scanner.nextInt();

        switch (input) {
            case 1 -> {
                properties.putAll(getAnimalProperties(scanner));
                properties.putAll(getPetProperties(scanner));
                properties.putAll(getCatProperties(scanner));
                zoo.add(getNewCat(properties));
                System.out.println("Кошка добавлена в зоопарк!");
                return;
            }
            case 2 -> {
                properties.putAll(getAnimalProperties(scanner));
                properties.putAll(getPetProperties(scanner));
                properties.putAll(getDogProperties(scanner));
                zoo.add(getNewDog(properties));
                System.out.println("Собака добавлена в зоопарк!");
                return;
            }
            case 3 -> {
                properties.putAll(getAnimalProperties(scanner));
                properties.putAll(getWildAnimalProperties(scanner));
                properties.putAll(getWolfProperties(scanner));
                zoo.add(getNewWolf(properties));
                System.out.println("Волк добавлен в зоопарк!");
                return;
            }
            case 4 -> {
                properties.putAll(getAnimalProperties(scanner));
                properties.putAll(getWildAnimalProperties(scanner));
                zoo.add(getNewTiger(properties));
                System.out.println("Тигр добавлен в зоопарк!");
                return;
            }
            case 5 -> {
                properties.putAll(getAnimalProperties(scanner));
                properties.putAll(getBirdProperties(scanner));
                zoo.add(getNewChicken(properties));
                System.out.println("Курица добавлена в зоопарк!");
                return;
            }
            case 6 -> {
                properties.putAll(getAnimalProperties(scanner));
                properties.putAll(getBirdProperties(scanner));
                zoo.add(getNewStork(properties));
                System.out.println("Аист добавлен в зоопарк!");
                return;
            }
            case 0 -> {
                return;
            }
        }
    }

    static void getAnimalToRemove(Scanner scanner, Zoo zoo) {
        System.out.println("Меню удаления животного");
        zoo.showAll();
        System.out.print("Введи номер животного для удаления >: ");
        int input = scanner.nextInt() - 1;
        zoo.remove(input);
        System.out.println("Животное удалено!");
    }

    static void getAnimalToShow(Scanner scanner, Zoo zoo) {
        System.out.println("Меню просмотра информации о животном");
        zoo.showAll();
        System.out.print("Введи номер животного просмотра информации >: ");
        int input = scanner.nextInt() - 1;
        zoo.show(input);
        showActive(zoo.getAnimal(input));
    }

    static void showActive(Animal animal) {
        if (animal instanceof ShowAffection) {
            System.out.println(animal.getClass().getSimpleName() + " может " +
                    ((ShowAffection) animal).showAffection());
        }
        if (animal instanceof Train) {
            System.out.println(animal.getClass().getSimpleName() + " может " +
                    ((Train) animal).train());
        }
        if (animal instanceof Fly) {
            System.out.println(animal.getClass().getSimpleName() + " может " +
                    ((Fly) animal).fly());
        }

    }

    static void showAllActivities(Zoo zoo){
        for (Animal animal :
                zoo.getAll()) {
            showActive(animal);
        }
    }

    static void getAnimalForMakeSound(Scanner scanner, Zoo zoo) {
        System.out.println("Меню звуков животных");
        zoo.showAll();
        System.out.print("Введи номер животного для извлечения из него звука >: ");
        int input = scanner.nextInt() - 1;
        zoo.makeSound(input);
    }

    static HashMap<String, Object> getAnimalProperties(Scanner scanner) {
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Введи высоту животного >: ");
        map.put("growth", scanner.nextInt());
        System.out.print("Введи вес животного >: ");
        map.put("weight", scanner.nextInt());
        System.out.print("Введи цвет глаз животного >: ");
        map.put("eyeColor", scanner.next());
        return map;
    }

    static HashMap<String, Object> getPetProperties(Scanner scanner) {
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Введи кличку животного >: ");
        map.put("name", scanner.next());
        System.out.print("Введи породу >: ");
        map.put("breed", scanner.next());
        System.out.print("Введи вакцинированно ли животное (да/нет) >: ");
        map.put("vaccinated", scanner.next().equalsIgnoreCase("да"));
        System.out.print("Введи цвет шерсти животного >: ");
        map.put("coatColor", scanner.next());
        System.out.print("Введи дату рождения животного (день.месяц.год) >: ");
        map.put("dateOfBirth", parseDate(scanner.next()));
        return map;
    }

    static HashMap<String, Object> getWildAnimalProperties(Scanner scanner) {
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Введи место обитания животного >: ");
        map.put("habitat", scanner.next());
        System.out.print("Введи дату нахождения (день.месяц.год) >: ");
        map.put("dateOfLocation", parseDate(scanner.next()));
        return map;
    }

    static HashMap<String, Object> getBirdProperties(Scanner scanner) {
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Введи высоту полёта >: ");
        map.put("flightAltitude", scanner.nextInt());
        return map;
    }

    static HashMap<String, Object> getCatProperties(Scanner scanner) {
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Наличие шерсти у животного (да/нет) >: ");
        map.put("presenceOfWool", scanner.next().equalsIgnoreCase("да"));
        return map;
    }

    static HashMap<String, Object> getDogProperties(Scanner scanner) {
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Дрессирован(-на) (да/нет) >: ");
        map.put("presenceOfWool", scanner.next().equalsIgnoreCase("да"));
        return map;
    }

    static HashMap<String, Object> getWolfProperties(Scanner scanner) {
        HashMap<String, Object> map = new HashMap<>();
        System.out.print("Вожак стаи (да/нет) >: ");
        map.put("packLeader", scanner.next().equalsIgnoreCase("да"));
        return map;
    }

    static Cat getNewCat(Map<String, Object> properties) {
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

    static Dog getNewDog(Map<String, Object> properties) {
        return new Dog((int) properties.get("growth"),
                (int) properties.get("weight"),
                (String) properties.get("eyeColor"),
                (String) properties.get("name"),
                (String) properties.get("breed"),
                (boolean) properties.get("vaccinated"),
                (String) properties.get("coatColor"),
                (LocalDate) properties.get("dateOfBirth"),
                (boolean) properties.get("trained"));
    }

    static Wolf getNewWolf(Map<String, Object> properties) {
        return new Wolf((int) properties.get("growth"),
                (int) properties.get("weight"),
                (String) properties.get("eyeColor"),
                (String) properties.get("habitat"),
                (LocalDate) properties.get("dateOfLocation"),
                (boolean) properties.get("packLeader"));
    }

    static Tiger getNewTiger(Map<String, Object> properties) {
        return new Tiger((int) properties.get("growth"),
                (int) properties.get("weight"),
                (String) properties.get("eyeColor"),
                (String) properties.get("habitat"),
                (LocalDate) properties.get("dateOfLocation"));
    }

    static Chicken getNewChicken(Map<String, Object> properties) {
        return new Chicken((int) properties.get("growth"),
                (int) properties.get("weight"),
                (String) properties.get("eyeColor"),
                (int) properties.get("flightAltitude"));
    }

    static Stork getNewStork(Map<String, Object> properties) {
        return new Stork((int) properties.get("growth"),
                (int) properties.get("weight"),
                (String) properties.get("eyeColor"),
                (int) properties.get("flightAltitude"));
    }

    static LocalDate parseDate(String date) {
        String[] dateArr = date.split("\\.");
        int day = Integer.parseInt(dateArr[0]);
        int month = Integer.parseInt(dateArr[1]);
        int year = Integer.parseInt(dateArr[2]);
        return LocalDate.of(year, month, day);
    }
}
