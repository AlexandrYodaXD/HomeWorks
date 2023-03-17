import java.util.Arrays;

public class DynamicArray<T> {
    private T[] array;
    private int size;

    /**
     * Конструктор по-умолчанию.
     */
    public DynamicArray() {
        this.array = (T[]) new Object[0];
        this.size = 0;
    }

    /**
     * Конструктор, создающий DynamicArray из массива.
     *
     * @param arr массив, на основании которого будет создан DynamicArray.
     */
    public DynamicArray(T[] arr) {
        this.array = Arrays.copyOf(arr, arr.length);
        this.size = arr.length;
    }

    /**
     * Метод для вставки объектов в конец массива.
     *
     * @param item объект для вставки в массив.
     */
    public void add(T item) {
        this.array = Arrays.copyOf(this.array, this.array.length + 1);
        array[size++] = item;
    }

    /**
     * Метод удаления элемента по индексу.
     * Если индекс выходит за пределы индексов массива, выбрасывается исключение.
     * Иначе элементы после удаляемого "сдвигаются" влево на его место, размер массива декрементируется,
     * данные в последнем элементе массива уже не нужны и заменяются на null.
     *
     * @param index индекс удаляемого элемента.
     */
    public void remove(int index) {
        if (index < 0 || index >= size) {
            throw new RuntimeException("Индекс " + index + " выходит за рамки!");
        } else {
            System.arraycopy(array, index + 1, array, index, size - index - 1);
            array[--size] = null;
        }
    }

    /**
     * Метод для удаления всех элементов, равных указанному.
     * В ходе работы метода элементы, которые не равны удаляемому, "сдвигаются" влево, так как в ходе "удаления"
     * образуются пустые места в массиве. Затем лишние элементы заменяются на null, после чего устанавливается новый size.
     *
     * @param value удаляемый элемент.
     */
    public void removeAll(T value) {
        int curIndex = 0;
        for (int i = 0; i < size; i++) {
            if (!array[i].equals(value)) {
                array[curIndex++] = array[i];
            }
        }
        for (int i = curIndex; i < size; i++) {
            array[i] = null;
        }

        size = curIndex;
    }

    /**
     * Метод, возвращающий минимальное значение в массиве.
     * Если массив пустой, то выбрасывает исключение.
     * Если в классе элементов массива не реализован интерфейс Comparable, то выбрасывается исключение.
     *
     * @return минимальное значение в массиве.
     */
    public T getMin() {
        if (size == 0) {
            throw new RuntimeException("Нельзя найти минимальный элемент в DynamicArray!");
        }

        T min = array[0];
        for (int i = 1; i < size; i++) {
            if (array[i] instanceof Comparable) {
                if (((Comparable) array[i]).compareTo(min) < 0) {
                    min = array[i];
                }
            } else {
                throw new RuntimeException("Нельзя найти минимальный элемент, в классе элементов не реализован интерфейс" +
                        "Comparable.");
            }
        }

        return min;
    }

    /**
     * Метод, возвращающий максимальное значение в массиве.
     * Если массив пустой, то выбрасывает исключение.
     * Если в классе элементов массива не реализован интерфейс Comparable, то выбрасывается исключение.
     *
     * @return максимальное значение в массиве.
     */
    public T getMax() {
        if (size == 0) {
            throw new RuntimeException("Нельзя найти максимальный элемент в DynamicArray!");
        }

        T max = array[0];
        for (int i = 1; i < size; i++) {
            if (array[i] instanceof Comparable) {
                if (((Comparable) array[i]).compareTo(max) > 0) {
                    max = array[i];
                }
            } else {
                throw new RuntimeException("Нельзя найти максимальный элемент, в классе элементов не реализован интерфейс" +
                        "Comparable.");
            }
        }

        return max;
    }

    /**
     * Метод для получения суммы элементов массива.
     * Если массив пустой (size == 0), то выбрасывается исключение.
     * Если массив состоит не из чисел, то выбрасывается исключение.
     *
     * @return сумма элементов массива, скастованная к типу массива.
     */
    public <T extends Number> T getSum() {
        if (size == 0) {
            throw new RuntimeException("Нельзя найти сумму элементов в пустом DynamicArray!");
        }

        double sum = 0.0;

        for (int i = 0; i < size; i++) {
            if (array[i] instanceof Number) {
                sum += ((Number) array[i]).doubleValue();
            }
        }

        if (array[0] instanceof Integer) {
            return (T) Integer.valueOf((int) sum);
        } else if (array[0] instanceof Double) {
            return (T) Double.valueOf(sum);
        } else if (array[0] instanceof Float) {
            return (T) Float.valueOf((float) sum);
        } else if (array[0] instanceof Long) {
            return (T) Long.valueOf((long) sum);
        } else {
            throw new RuntimeException("getSum может посчитать сумму только для чисел!");
        }
    }

    /**
     * Метод для получения произведения элементов массива.
     * Если массив пустой (size == 0), то выбрасывается исключение.
     * Если массив состоит не из чисел, то выбрасывается исключение.
     *
     * @return произведение элементов массива, скастованное к типу массива.
     */
    public <T extends Number> T getProduct() {
        if (size == 0) {
            throw new RuntimeException("Нельзя найти произведение элементов в пустом DynamicArray!");
        } else if (!(array[0] instanceof Number)) {
            throw new RuntimeException("getSum может посчитать произведение только для чисел!");
        }

        double product = 1.0;

        for (int i = 0; i < size; i++) {
            if (array[i] instanceof Number) {
                product *= ((Number) array[i]).doubleValue();
            }
        }

        if (array[0] instanceof Integer) {
            return (T) Integer.valueOf((int) product);
        } else if (array[0] instanceof Double) {
            return (T) Double.valueOf(product);
        } else if (array[0] instanceof Float) {
            return (T) Float.valueOf((float) product);
        } else if (array[0] instanceof Long) {
            return (T) Long.valueOf((long) product);
        } else {
            throw new RuntimeException("getSum может посчитать произведение только для чисел!");
        }
    }

    /**
     * Метод возвращает индекс первого вхождения искомого элемента.
     *
     * @param value искомый элемент.
     * @return индекс искомого элемента.
     */
    public int indexOf(T value) {
        for (int i = 0; i < size; i++) {
            if (array[i].equals(value)) {
                return i;
            }
        }

        return -1;
    }

    /**
     * Метод,  Проверка наличия элемента в массиве.
     *
     * @param value искомый элемент.
     * @return true, если элемент в массиве есть, false – нет.
     */
    public boolean contains(T value) {
        return indexOf(value) != -1;
    }

    /**
     * Метод пузырьковой сортировки.
     */
    public void bubbleSort() {
        if (size == 0) return;
        if (!(array[0] instanceof Comparable)) {
            throw new RuntimeException("Нельзя отсортировать массив, у класса объектов, содержащихся в DynamicArray, " +
                    "не реализован интерфейс Comparable.");
        }

        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < size - i - 1; j++) {
                if (((Comparable) array[j]).compareTo(array[j + 1]) > 0) {
                    T temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    /**
     * Метод сортировки простыми вставками.
     */
    public void insertionSort() {
        if (size == 0) return;
        if (!(array[0] instanceof Comparable)) {
            throw new RuntimeException("Нельзя отсортировать массив, у класса объектов, содержащихся в DynamicArray, " +
                    "не реализован интерфейс Comparable.");
        }

        for (int i = 1; i < size; i++) {
            T key = array[i];
            int j = i - 1;
            while (j >= 0 && ((Comparable) array[j]).compareTo(key) > 0) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
    }

    /**
     * Метод сортировки простым выбором.
     */
    public void selectionSort() {
        if (size == 0) return;
        if (!(array[0] instanceof Comparable)) {
            throw new RuntimeException("Нельзя отсортировать массив, у класса объектов, содержащихся в DynamicArray, " +
                    "не реализован интерфейс Comparable.");
        }

        for (int i = 0; i < size - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < size; j++) {
                if (((Comparable) array[j]).compareTo(array[minIndex]) < 0) {
                    minIndex = j;
                }
            }
            T temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }

    /**
     * Метод для получения объекта массива по индексу.
     *
     * @param index индекс элемента.
     * @return элемент массива.
     */
    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Индекс " + index + " выходит за рамки!");
        }
        return array[index];
    }

    /**
     * Метод для установки значения для элемента массива.
     *
     * @param index   индекс элемента.
     * @param element элемент для вставки.
     */
    public void set(int index, T element) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Индекс " + index + " выходит за рамки!");
        }
        array[index] = element;
    }

    /**
     * Метод для печати массива в консоль.
     */
    public void print() {
        System.out.println(Arrays.toString(Arrays.copyOf(array, size)));
    }

    /**
     * Метод для получения размера массива.
     *
     * @return размер массива.
     */
    public int length() {
        return size;
    }
}
