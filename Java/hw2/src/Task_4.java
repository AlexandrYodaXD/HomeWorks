//4*. К калькулятору из предыдущего дз добавить логирование.
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Scanner;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Task_4 {
    // создание глобального логгера
    private static Logger logger;
    public static void main(String[] args) {
        Scanner iScanner = new Scanner(System.in);

        // создание и настройка логгера
        FileHandler fileHandler;
        try {
            fileHandler = new FileHandler("Task_4_log.log", true);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        SimpleFormatter sFormatter = new SimpleFormatter();
        fileHandler.setFormatter(sFormatter);
        logger = Logger.getLogger(Task_4.class.getName());
        logger.addHandler(fileHandler);
        // ОТКЛЮЧЕНИЕ ВЫВОДА СООБЩЕНИЙ ЛОГГИРОВАНИЯ В КОНСОЛЬ
        logger.setUseParentHandlers(false);

        logger.info("Новый расчет.\n=====================================================================");
        double a = get_num("Введи первое число >: ", iScanner);
        String operation = get_operation("Введи операцию [+, -, *, /] >: ", iScanner);
        double b = get_num("Введи второе число >: ", iScanner);
        double result = calc(a, b, operation);
        // Убирание незначащих нулей и округление до 3 знаков после запятой
        DecimalFormat df = new DecimalFormat("#.###");
        String resultAsString = String.format("Результат: %s %s %s = %s", df.format(a), operation, df.format(b), df.format(result));
        System.out.println(resultAsString);

        logger.info(resultAsString);
        logger.info("Расчет закончен.\n=====================================================================\n");

        iScanner.close();
    }

    public static double get_num(String message, Scanner scanner) {
        while (true) {
            System.out.print(message);
            if (scanner.hasNextDouble()) {
                double num = scanner.nextDouble();
                scanner.nextLine();
                logger.info(String.format("%s %f", message, num));
                return num;
            } else {
                logger.warning(String.format("Введено некорректное число: %s", scanner.next()));
                System.out.println("Ошибка: введено некорректное число.");
                scanner.nextLine();
            }
        }
    }

    public static String get_operation(String message, Scanner scanner) {
        String[] operations = new String[]{"+", "-", "*", "/"};

        while (true) {
            System.out.print(message);
            String inputString = scanner.next();

            for (String operation : operations) {
                if (inputString.equals(operation)) {
                    logger.info(String.format("%s %s", message, inputString));
                    return inputString;
                }
            }
            // else
            System.out.println("Ошибка: введен некорректный оператор.");
            logger.warning(String.format("Введен некорректный оператор: %s", inputString));
        }
    }

    public static double calc(double a, double b, String operation) {

        switch (operation) {
            case "+" -> {
                return a + b;
            }
            case "-" -> {
                return a - b;
            }
            case "*" -> {
                return a * b;
            }
            case "/" -> {
                if (b == 0) {
                    System.out.println("Ошибка: на ноль в данной программе делить нельзя.");
                    logger.warning(String.format("Деление на ноль: %f %s %f", a, operation, b));
                    return a / b;
                }
                return a / b;
            }
            default -> {
                System.out.println("Ошибка оператора.");
                return 0;
            }
        }
    }
/*
    public static Logger getLogger(FileHandler fh) {
        Logger logger = Logger.getLogger(Task_4.class.getName());
        SimpleFormatter sFormatter = new SimpleFormatter();
        fh.setFormatter(sFormatter);
        // ОТКЛЮЧЕНИЕ ВЫВОДА СООБЩЕНИЙ ЛОГГИРОВАНИЯ В КОНСОЛЬ
        logger.setUseParentHandlers(false);
        logger.addHandler(fh);
        return logger;
    }*/
}
