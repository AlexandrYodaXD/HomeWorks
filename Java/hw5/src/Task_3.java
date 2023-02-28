import java.util.ArrayList;
import java.util.Arrays;

/*
 *Реализовать алгоритм пирамидальной сортировки (HeapSort)
 */
public class Task_3 {
    public static void main(String[] args) {
//        ArrayList<Integer> arr = new ArrayList<>(Arrays.asList(33, 25, 66, 98, 13, 22, 88));
//        int[] arr = new int[]{33, 25, 88, 98, 13, 22, 66};
        int[] arr = new int[]{5, 7, 9, 4, 3, 8, 3, 1, 0, 3};
        makeHeap(arr);
    }

    static void makeHeap(int[] arr) {
        int size = arr.length;
        ArrayList<Integer> arrLst = new ArrayList<>();
        arrLst.add(0, 0);
        for (int i = 1; i < size + 1; i++) {
            arrLst.add(i, arr[i - 1]);

            if (i > 1){
                int kid = i / 2;
                if (arrLst.get(i) > arrLst.get(kid)){
                    System.out.println(String.format("До замены: %s", arrLst.toString()));
                    int temp = arrLst.remove(i);
                    arrLst.add(i, arrLst.get(kid));
                    arrLst.remove(kid);
                    arrLst.add(kid, temp);
                    System.out.println(String.format("После замены: %s", arrLst.toString()));
                }
            }
            System.out.println(arrLst);
        }
    }
}
