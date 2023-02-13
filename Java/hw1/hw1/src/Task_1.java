/*
1. Вычислить n-ое треугольного число(сумма чисел от 1 до n),
    n! (произведение чисел от 1 до n)
*/

import java.util.Scanner;

public class Task_1 {
    public static void main(String[] args) {
        Scanner iScanner = new Scanner(System.in);
        System.out.print("Введи число n >: ");
        int n = iScanner.nextInt();
        iScanner.close();

        int triangle = n * (n + 1) / 2;
        int factorial = factorial(n);
        System.out.printf("%d-е треугольное число это %d.\n", n, triangle);
        System.out.printf("Факториал числа %d это %d.", n, factorial);
    }

    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        }
        return n * factorial(n - 1);
    }
}
