import java.util.Arrays;
import java.util.LinkedList;

/*
Пусть дан LinkedList с несколькими элементами. Реализуйте метод, который вернет “перевернутый” список.
Постараться не обращаться к листу по индексам.
 */
public class Task_1 {
    public static void main(String[] args) {
        // с возвратом нового списка
        LinkedList<Integer> linkedList1 = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Original_1: " + linkedList1);
        LinkedList<Integer> reversedLinkedList = getReversedLinkedList(linkedList1);
        System.out.println("Reversed_1: " + reversedLinkedList);

        // изменение исходного списка
        LinkedList<Integer> linkedList2 = new LinkedList<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Original_2: " + linkedList2);
        reverseLinkedList(linkedList2);
        System.out.println("Reversed_2: " + linkedList2);
    }

    static LinkedList<Integer> getReversedLinkedList (LinkedList<Integer> linkedList){
        // возврат перевернутого списка
        LinkedList<Integer> reversedLinkedList = new LinkedList<>();
        while (linkedList.size() > 0){
            reversedLinkedList.add(linkedList.pollLast());
        }
        return reversedLinkedList;
    }

    static void reverseLinkedList (LinkedList<Integer> linkedList){
        // без возврата нового списка, изменение исходного списка
        LinkedList<Integer> buffer = new LinkedList<>();
        while (linkedList.size() > 0){
            buffer.add(linkedList.pollLast());
        }
        while (buffer.size() > 0){
            linkedList.add(buffer.pollFirst());
        }
    }
}
