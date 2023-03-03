import java.util.Scanner;

//2. Вывести все простые числа от 1 до 1000
public class Task_2 {
    public static void main(String[] args) {
        Scanner iScanner = new Scanner(System.in);
        System.out.print("Введи число n >: ");
        int n = iScanner.nextInt();
        iScanner.close();

        if (is_simple(n)) {
            System.out.printf("%d - простое число.", n);
        } else {
            System.out.printf("%d - не простое число.", n);
        }

    }

    public static boolean is_simple(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
