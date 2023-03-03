/*
2.Пусть дан произвольный список целых чисел, удалить из него четные числа
*/

import java.util.ArrayList;
import java.util.Arrays;

public class Task_2 {
    public static void main(String[] args) {
        ArrayList<Integer> numList = new ArrayList<>(Arrays.asList(7, 8, 4, 6, 1, 9, 3, 2, 5));
        System.out.printf("Список до удаления четных чисел: %s\n", numList);
        numList.removeIf(x -> x % 2 == 0);
        System.out.printf("Список после удаления четных чисел: %s", numList);
    }
}
