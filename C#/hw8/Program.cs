/*
Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
В итоге получается вот такой массив:
7 4 2 1
9 5 3 2
8 4 4 2
*/

void Sort2DIntArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            int max = j;
            for (int k = j + 1; k < array.GetLength(1); k++)
            {
                if (array[i, k] > array[i, max])
                {
                    max = k;
                }
            }
            if (max != j)
            {
                int temp = array[i, j];
                array[i, j] = array[i, max];
                array[i, max] = temp;
            }
        }
    }
}

void Task54()
{
    int[,] task1Array = Create2DArrayRandomInt(4, 4, 10, 99);
    System.Console.WriteLine("Изначальный массив:");
    Print2DIntArray(task1Array);
    Sort2DIntArray(task1Array);
    System.Console.WriteLine("Отсортированный массив массив:");
    Print2DIntArray(task1Array);
}
// Task54();


/*
Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

Например, задан массив:

1 4 7 2
5 9 2 3
8 4 2 4
5 2 6 7

Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка
*/

int FindRowWithMinSum(int[,] array)
{
    int res = 0;
    int? minSum = null;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        int sum = 0;
        for (int j = 0; j < array.GetLength(1); j++)
        {
            sum += array[i, j];
        }
        if (minSum == null) minSum = sum; // задаем minSum первоначальное значение (сумму первой строки);
        Console.WriteLine($"Сумма {i + 1} строки равна {sum}.");
        if (sum < minSum) res = i;
    }
    return res;
}

void Task56()
{
    int[,] task2Array = Create2DArrayRandomInt(4, 4, 1, 9);
    Print2DIntArray(task2Array);
    int task2res = FindRowWithMinSum(task2Array);
    Console.WriteLine();
    Console.WriteLine($"Наименьшая сумма элементов в {task2res + 1} строке.");
}
// Task56();

/*
Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Например, даны 2 матрицы:
2 4 | 3 4
3 2 | 3 3
Результирующая матрица будет:
18 20
15 18
*/

int[,] MatrixProduct(int[,] array1, int[,] array2)
{
    if (array1.GetLength(0) != array2.GetLength(1))
    {
        Console.WriteLine("Матрицы не совместимы.");
        return null;
    }
    int size = array1.GetLength(0);
    int[,] res = new int[size, size];
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            for (int k = 0; k < size; k++)
                res[i, j] += array1[i, k] * array2[k, j];
        }
    }
    return res;
}

void Task58()
{
    System.Console.WriteLine("Первая матрица:");
    int[,] task3Array1 = Create2DArrayRandomInt(2, 2, 1, 9);
    Print2DIntArray(task3Array1);
    System.Console.WriteLine("Вторая матрица:");
    int[,] task3Array2 = Create2DArrayRandomInt(2, 2, 1, 9);
    Print2DIntArray(task3Array2);
    int[,] task3ProductArray = MatrixProduct(task3Array1, task3Array2);

    if (task3ProductArray != null)
    {
        System.Console.WriteLine("Результат произведения матриц:");
        Print2DIntArray(task3ProductArray);
    }
}
// Task58();


/*
Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
Массив размером 2 x 2 x 2
66(0,0,0) 25(0,1,0)
34(1,0,0) 41(1,1,0)
27(0,0,1) 90(0,1,1)
26(1,0,1) 55(1,1,1)
*/

/* ShuffleArray перемешивает массив, необязательный аргумент shuffleCount отвечает за количество перемешиваний.
С логической точки зрения хватит одного перемешивания/прохода по массиву,
но почему-то хочется добавить возможность перемешивать "сильнее" (человеческий фактор?) */
void ShuffleArray(int[] array, int shuffleCount = 1) 
{
    Random randomNumber = new Random();
    for (int i = 0; i < array.Length * shuffleCount; i++)
    {
        int index = i % array.Length; // так мы не выйдем за границы индексов массива;
        int randomIndex = randomNumber.Next(0, array.Length);
        
        do randomIndex = randomNumber.Next(0, array.Length);
        while (index == randomIndex);

        int temp = array[index];
        array[index] = array[randomIndex];
        array[randomIndex] = temp;
    }
}

/* Второй вариант метода для перемешивания массива.
За идею с проходом до половины массива спасибо Елене :)
По тестам работает быстрее первого способа, но "хуже перемешивает",
т. к. оба индекса массива выбираются случайно и участок массива
с последовательными элементами, например, [...13, 14, 15...] может не попасть под перемешивание */
void ShuffleArray2(int[] array, int shuffleCount = 1)
{
    Random randomNumber = new Random();
    int halfLenght = array.Length / 2;

    for (int i = 0; i < halfLenght * shuffleCount; i++)
    {
        int firstIndex = randomNumber.Next(0, halfLenght);
        int secondIndex = randomNumber.Next(halfLenght, array.Length);
        int temp = array[firstIndex];
        array[firstIndex] = array[secondIndex];
        array[secondIndex] = temp;
    }
}

// метод создает срез массива
int[] ArraySlice(int[] array, int start, int amount)
{
    int[] resultArray = new int[amount];

    for (int i = 0, m = start; i < amount; i++, m++)
    {
        resultArray[i] = array[m];
    }
    return resultArray;
}

// метод заполняет создает новый массив размера NxNxN и заполняет его числами из массива из аргумента array.
int[,,] Fill3DArray(int[] array, int size = 3)
{
    int[,,] resultArray = new int[size, size, size];

    for (int i = 0, index = 0; i < resultArray.GetLength(0) && index < array.Length; i++)
    {
        for (int j = 0; j < resultArray.GetLength(1) && index < array.Length; j++)
        {
            for (int k = 0; k < resultArray.GetLength(2) && index < array.Length; k++, index++)
            {
                resultArray[i, j, k] = array[index];
            }
        }
    }

    return resultArray;
}

void Print3DArrayIntWithIndex(int[,,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(2); k++)
                Console.Write($"{array[i, j, k]}({i},{j},{k}) ");
            // Console.Write($"{array[j, k, i]}({j},{k},{i}) "); вывод как требуется в задаче
            Console.WriteLine();
        }
        Console.WriteLine();
    }
}

void Task60()
{
    int[] twoDigitsNumbers = Enumerable.Range(10, 90).ToArray(); // создается массив двузначных чисел
    ShuffleArray(twoDigitsNumbers);
    PrintIntArray(twoDigitsNumbers);
    int[] arraySlice = ArraySlice(twoDigitsNumbers, 0, 7); // создается срез массива twoDigitsNumbers с 0 по 7 индексы
                                                           // позже я доработал метод Fill3DArray таким образом,
                                                           // что в него можно передавать twoDigitsNumbers целиком,
                                                           // но т.к. ArraySlice уже написан, то пусть будет :)
    PrintIntArray(arraySlice);
    int[,,] task3Array = Fill3DArray(arraySlice);
    Print3DArrayIntWithIndex(task3Array);
}
// Task60();


/*
Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
Например, на выходе получается вот такой массив:
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07
*/

// метод создает спиральную матрицу размером NxM
int[,] CreateSpiralArray(int rows, int columns = -1)
{
    if (columns == -1) columns = rows; // если не передать значение columns в параметрах, то создастся квадратная матрица
    int[,] array = new int[rows, columns];

    for (int iteration = 0, current = 1; current <= rows * columns; iteration++)
    {
        for (int i = iteration, j = iteration; j < columns - iteration; j++, current++) // заполнение слева направо
            array[i, j] = current;

        if (current > rows * columns) break;
        for (int i = iteration + 1, j = columns - iteration - 1; i < rows - iteration; i++, current++) // заполнение сверху вниз
            array[i, j] = current;

        if (current > rows * columns) break;
        for (int i = rows - iteration - 1, j = columns - iteration - 2; j >= iteration; j--, current++) // заполнение справа налево
            array[i, j] = current;

        if (current > rows * columns) break;
        for (int i = rows - iteration - 2, j = 0 + iteration; i >= iteration + 1; i--, current++) // заполнение снизу вверх
            array[i, j] = current;
    }
    return array;
}

// Красивая печать матрицы с дополнением нулями до fillToSigns знаков и раскрашиванием чисел цветом.
// Как говорится, лучше один раз увидеть :)
void PrettyPrint2DArrayInt(int[,] array, int fillToSigns = 2)
{
    ConsoleColor[] colors = {ConsoleColor.Red, ConsoleColor.Yellow, ConsoleColor.Green,
                            ConsoleColor.Cyan, ConsoleColor.Blue, ConsoleColor.Magenta};
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.ForegroundColor = colors[(j + i) % 6]; // 6 в данном случае длина [] colors (GetLenght не работает)
            Console.Write(array[i, j].ToString($"D{fillToSigns}") + " ");
        }
        Console.WriteLine();
    }
    Console.ResetColor();
}

void Task62()
{
    int[,] task62Array = CreateSpiralArray(4, 4);
    PrettyPrint2DArrayInt(task62Array, 2);
}
Task62();


// общие методы
void Print2DIntArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (var j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j]);
            if (j < array.GetLength(1) - 1)
                Console.Write(", ");
        }
        if (i < array.GetLength(0) - 1)
            Console.WriteLine(",");
        else Console.WriteLine(".");
    }
    Console.WriteLine();
}
int[,] Create2DArrayRandomInt(int rows, int columns, int minValue, int maxValue)
{
    int[,] array = new int[rows, columns];
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            array[i, j] = new Random().Next(minValue, maxValue + 1);
        }
    }
    return array;
}
int[] MakeRandomIntArray(int size, int minValue, int maxValue) // принимает целое число в качестве размера массива, верхнюю и нижнюю границу для генерации чисел, возвращает массив заданного размера, заполненный случайными числами от нижней до верхней границы чисел включительно.
{
    int[] array = new int[size];

    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(minValue, maxValue + 1);
    }
    return array;
}
void PrintIntArray(int[] array) // печать массива, состоящего из int элементов
{
    Console.Write("{ ");
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i]);
        if (i < array.Length - 1) // ставим запятую после элемента, если это не последний элемент
            Console.Write(", ");
    }
    Console.WriteLine(" }\n");
}
void Sort1DIntArray(int[] array) // сортировка одномерного int массива
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        int max = i;
        for (int j = i + 1; j < array.GetLength(0); j++)
            if (array[j] > array[max])
                max = j;
        if (max != i)
        {
            int temp = array[i];
            array[i] = array[max];
            array[max] = temp;
        }
    }
}