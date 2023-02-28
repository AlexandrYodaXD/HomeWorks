import java.util.ArrayList;
import java.util.Arrays;

/*
 *Реализовать алгоритм пирамидальной сортировки (HeapSort)
 */
public class Task_3 {
    public static void main(String[] args) {
//        Integer[] arr = new Integer[]{5, 7, 9, 4, 3, 8, 3, 1, 0, 3};
        Integer[] arr = new Integer[]{14, 333, 123, 4, 34, 8, 3, 1, 0, 3, 42, 332, 12, 1, 88, 1312};
        heapSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    static void heapSort(Integer[] originArray) {
        ArrayList<Integer> heapList = new ArrayList<>(Arrays.asList(originArray));
        heapList.add(0, 0);
//        System.out.println("Первичная куча: " + heapList);

        for (int i = 0; i < originArray.length; i++) {
            // пересобираем кучу, наименьший элемент вспылвет в 1 индекс
            rebuildHeap(heapList);
            originArray[i] = heapList.remove(1);
//            System.out.println("Добавлен отстортированный элемент");
        }
    }

    static void rebuildHeap(ArrayList<Integer> arrayList) {
        boolean wasChanged = true;
        // пересобираем кучу пока после при пересборке есть изменения
        while (wasChanged) {
            wasChanged = false;
            for (int i = 1; i < arrayList.size(); i++) {
                if (i > 1) {
                    int kid = i / 2;
                    if (arrayList.get(i) < arrayList.get(kid)) {
                        // меняем местами потомка и родителя
                        int temp = arrayList.remove(i);
                        arrayList.add(i, arrayList.get(kid));
                        arrayList.remove(kid);
                        arrayList.add(kid, temp);
                        // флаг, сообщающий об изменениях в куче переводится в true
                        wasChanged = true;
                    }
                }
            }
//            if (wasChanged) System.out.println("Куча отправляется на пересборку " + arrayList);
//            else System.out.println("Куча не нуждается в пересборке  " + arrayList);
        }
    }
}
