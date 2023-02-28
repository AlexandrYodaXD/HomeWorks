import java.util.ArrayList;
import java.util.Arrays;

/*
 *Реализовать алгоритм пирамидальной сортировки (HeapSort)
 */
public class Task_3 {
    public static void main(String[] args) {
        int[] arr = new int[]{5, 7, 9, 4, 3, 8, 3, 1, 0, 3};
        heapSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    static void heapSort(int[] originArray) {
        int size = originArray.length;
        ArrayList<Integer> heapList = new ArrayList<>();
        heapList.add(0, 0);
        for (int i = 1; i < size + 1; i++) {
            heapList.add(i, originArray[size - i]);

            if (i > 1){
                int kid = i / 2;
                if (heapList.get(i) < heapList.get(kid)){
                    System.out.println(String.format("До замены: %s", heapList.toString()));
                    int temp = heapList.remove(i);
                    heapList.add(i, heapList.get(kid));
                    heapList.remove(kid);
                    heapList.add(kid, temp);
                    System.out.println(String.format("После замены: %s", heapList.toString()));
                }
            }
        }

        for (int i = 0; i < originArray.length; i++) {
            rebuildHeap(heapList);
            originArray[i] = heapList.remove(1);
        }
    }

    static void rebuildHeap(ArrayList<Integer> arrayList){
        for (int i = 1; i < arrayList.size(); i++) {

            if (i > 1){
                int kid = i / 2;
                if (arrayList.get(i) < arrayList.get(kid)){
//                    System.out.println(String.format("До замены: %s", arrayList.toString()));
                    int temp = arrayList.remove(i);
                    arrayList.add(i, arrayList.get(kid));
                    arrayList.remove(kid);
                    arrayList.add(kid, temp);
//                    System.out.println(String.format("После замены: %s", arrayList.toString()));
                }
            }
        }
        System.out.println("Новая куча: " + arrayList);
    }
}
