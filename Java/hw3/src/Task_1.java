/*
* 1.Реализовать алгоритм сортировки слиянием
*/

import java.util.Arrays;

public class Task_1 {
    public static void main(String[] args) {
        int[] arr = new int[]{7, 8, 4, 6, 1, 9, 3, 2, 5};
        mergeSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    public static void mergeSort(int[] arr) {
        // если массив состоит из одного элемента, то такой массив является отсортированным, выход из рекурсии
        if (arr.length <= 1) return;

        // середина массива
        int middle = arr.length / 2;

        // "срез" первой половины массива
        int[] left = Arrays.copyOfRange(arr, 0, middle);
        // рекурсивно вызываем функцию, "разрезая" массив на две части, пока не дойдем до базового случая
        mergeSort(left);

        // "срез" второй половины массива
        int[] right = Arrays.copyOfRange(arr, middle, arr.length);
        // рекурсивно вызываем функцию, "разрезая" массив на две части, пока не дойдем до базового случая
        mergeSort(right);

        // слияние массивов из левой и правой части в один отсортированный
        merge(left, right, arr);
    }

    private static void merge(int[] left, int[] right, int[] arr) {
        int leftIndex = 0; // указатель для левого массива
        int rightIndex = 0; // указатель для правого массива
        int targetIndex = 0; // указатель для целевого массива

        // цикл выполняется пока указатель одного из массивов не дойдет до конца массива
        while (leftIndex < left.length && rightIndex < right.length) {
            if (left[leftIndex] < right[rightIndex]) {
                arr[targetIndex++] = left[leftIndex++];
            } else {
                arr[targetIndex++] = right[rightIndex++];
            }
        }

        // т.к. благодаря циклу while один из указателей доходит до конца своего массива,
        // то лишь один из циклов while ниже будет выполнен

        // если указатель левого массива не дошел до конца, то докидываем в целевой массив всё что осталось
        while (leftIndex < left.length) {
            arr[targetIndex++] = left[leftIndex++];
        }
        // если указатель правого массива не дошел до конца, то докидываем в целевой массив всё что осталось
        while (rightIndex < right.length) {
            arr[targetIndex++] = right[rightIndex++];
        }
    }
}
