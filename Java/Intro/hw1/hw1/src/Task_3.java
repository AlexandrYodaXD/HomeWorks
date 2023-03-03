//3. Реализовать простой калькулятор

import java.util.Scanner;

public class Task_3 {
    public static void main(String[] args) {
        Scanner iScanner = new Scanner(System.in);

        System.out.print("Введи первое число >: ");
        double a = get_num(iScanner);
        System.out.print("Введи операцию (+, -, *, /) >: ");
        char operation = get_operation(iScanner);
        System.out.print("Введи второе число >: ");
        double b = get_num(iScanner);

        double result = calc(a, b, operation);
        System.out.printf("%f %c %f = %f", a, operation, b, result);

        iScanner.close();
    }

    public static double get_num(Scanner scanner) {
        return scanner.nextInt();
    }

    public static char get_operation(Scanner scanner) {
        String operation_as_string = scanner.next();
        if (operation_as_string.length() == 1) {
            char operation = operation_as_string.toCharArray()[0];
            char[] operations = new char[]{'+', '-', '*', '/'};
            for (char c : operations) {
                if (c == operation) {
                    return operation;
                }
            }
        }
        return '∅';
    }

    public static double calc(double a, double b, char operation) {
        switch (operation) {
            case '+' -> {
                return a + b;
            }
            case '-' -> {
                return a - b;
            }
            case '*' -> {
                return a * b;
            }
            case '/' -> {
                return a / b;
            }
            default -> {
                System.out.println("Ошибка оператора.");
                return 0;
            }
        }
    }
}
