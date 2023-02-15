import java.io.IOException;
import java.util.Arrays;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

//2 . Реализуйте алгоритм сортировки пузырьком числового массива, результат после каждой итерации запишите в лог-файл.
public class Task_2 {
    private static Logger logger;
    public static void main(String[] args) {
        // создание и настройка логгера
        FileHandler fileHandler;
        try {
            fileHandler = new FileHandler("Task_2_log.log", true);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        SimpleFormatter sFormatter = new SimpleFormatter();
        fileHandler.setFormatter(sFormatter);
        logger = Logger.getLogger(Task_2.class.getName());
        logger.addHandler(fileHandler);
        // ОТКЛЮЧЕНИЕ ВЫВОДА СООБЩЕНИЙ ЛОГГИРОВАНИЯ В КОНСОЛЬ
        logger.setUseParentHandlers(false);

        // массив для сортировки
        int[] intArray = new int[]{4, 6, 2, 8, 3, 9, 11, 10, 5, 7, 1};
        System.out.println(Arrays.toString(intArray));

        // массив после сортировки
        bubbleSort(intArray);
        System.out.println(Arrays.toString(intArray));
    }

    public static void bubbleSort(int[] arr) {
//        Logger logger = getLogger();
        logger.info(String.format("""
                Новая сортировка.
                =====================================================================
                Исходный вид массива: %s
                =====================================================================""",
                Arrays.toString(arr)));
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
            logger.info(String.format("Массив после итерации № %d: %s", i + 1, Arrays.toString(arr)));
        }
        logger.info(String.format("""
                Сортировка завершена
                =====================================================================
                Окончательный вид массива: %s
                =====================================================================
                """, Arrays.toString(arr)));
    }
}
