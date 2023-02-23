/*
Найдите сумму всех элементов LinkedList, сохраняя все элементы в списке. Используйте итератор
 */

import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;

public class Task_3 {
    public static void main(String[] args) {
        LinkedList<Integer> myLL = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        Iterator<Integer> iterator = myLL.iterator();

        int sum = 0;
        while (iterator.hasNext()){
            sum += iterator.next();
        }

        System.out.println(sum); // 55
    }
}
