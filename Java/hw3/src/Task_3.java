/*
3.Задан целочисленный список ArrayList. Найти минимальное, максимальное и среднее арифметическое этого списка.
*/

import java.util.ArrayList;
import java.util.Arrays;

public class Task_3 {
    public static void main(String[] args) {
        ArrayList<Integer> numList = new ArrayList<>(Arrays.asList(7, 8, 4, 6, 1, 1, 9, 3, 2, 5));
        System.out.printf("Список чисел: %s\n", numList);
        System.out.printf("Минимальный элемент: %d\n", getMin(numList));
        System.out.printf("Максимальный элемент: %d\n", getMax(numList));
        System.out.printf("Среднее арифметическое списка: %f\n", getAverage(numList));
    }

    public static int getMin(ArrayList<Integer> numList) {
        int min = Integer.MAX_VALUE;
        for (Integer integer : numList) {
            min = Math.min(integer, min);
        }
        return min;
    }

    public static int getMax(ArrayList<Integer> numList) {
        int max = Integer.MIN_VALUE;
        for (Integer integer : numList) {
            max = Math.max(integer, max);
        }
        return max;
    }
    public static double getAverage(ArrayList<Integer> numList){
        int sum = 0;
        for (Integer integer : numList){
            sum += integer;
        }
    return (double) sum / numList.size();
    }
}
