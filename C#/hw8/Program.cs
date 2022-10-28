void Print2DArrayInt(int[,] array)
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

// временные методы для отладки
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
    Console.WriteLine(" }");
}

// Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// В итоге получается вот такой массив:
// 7 4 2 1
// 9 5 3 2
// 8 4 4 2

void Sort1DArrayInt(int[] array)
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

void Sort2DArrayInt(int[,] array)
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

// int[,] task1Array = Create2DArrayRandomInt(4, 4, 10, 99);
// Print2DArrayInt(task1Array);
// Console.WriteLine();
// Sort2DArrayInt(task1Array);
// Console.WriteLine();
// Print2DArrayInt(task1Array);



// Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

// Например, задан массив:

// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 5 2 6 7

// Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей суммой элементов: 1 строка

int FindRowWithMinSum(int[,] array)
{
    int res = 0;
    int? minSum = null;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        int sum = 0;
        for (int j = 0; j < array.GetLength(1); j++)
            sum += array[i, j];
        if (minSum == null) minSum = sum; // задаем minSum первоначальное значение (т. е. сумму первой строки);
                                          //      if (i == 0) minSum = sum; делает то же самое, но в этом случае при инициализации minSum можно было присвоить 0;
        Console.WriteLine($"Сумма {i + 1} строки равна {sum}."); // для наглядности;
        if (sum < minSum) res = i;
    }
    return res;
}

// int[,] task2Array = Create2DArrayRandomInt(4, 4, 1, 9);
// Print2DArrayInt(task2Array);
// Console.WriteLine();
// int task2res = FindRowWithMinSum(task2Array);
// Console.WriteLine();
// Console.WriteLine($"Наименьшая сумма элементов в {task2res + 1} строке.");


// Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
// Например, даны 2 матрицы:
// 2 4 | 3 4
// 3 2 | 3 3
// Результирующая матрица будет:
// 18 20
// 15 18
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

// int[,] task3Array1 = Create2DArrayRandomInt(2, 2, 1, 9);
// Print2DArrayInt(task3Array1);
// Console.WriteLine();
// int[,] task3Array2 = Create2DArrayRandomInt(2, 2, 1, 9);
// Print2DArrayInt(task3Array2);
// Console.WriteLine();
// int[,] task3ProductArray = MatrixProduct(task3Array1, task3Array2);
// if (task3ProductArray != null) Print2DArrayInt(task3ProductArray);


// Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
// Массив размером 2 x 2 x 2
// 66(0,0,0) 25(0,1,0)
// 34(1,0,0) 41(1,1,0)
// 27(0,0,1) 90(0,1,1)
// 26(1,0,1) 55(1,1,1)

int[] CreateNumbersSeriesArray(int minValue, int maxValue) // создает массив из ряда чисел, maxValue не будет включен;
{
    int[] numberSeries = new int[(maxValue) - minValue];
    for (int i = minValue; i < maxValue; i++)
    {
        numberSeries[i - minValue] = i;
    }
    return numberSeries;
}

void ShuffleArray(int[] array, int shuffleTimes = 1) // перемешивает массив, необязательный аргумент shuffleTimes отвечает за количество перемешиваний
{
    for (int i = 0; i < (shuffleTimes * array.Length); i++)
    {
        int index = i % array.Length; // так мы не выйдем за границы индексов массива;
        int temp = array[index];
        int randomIndex = new Random().Next(0, array.Length);
        array[index] = array[randomIndex];
        array[randomIndex] = temp;
    }
}

int[] CreateAnArrayOfNonRepeatingNumbers(int size, int minValue, int maxValue, int shuffleTimes = 1) // создает массив из случайных неповторяющихся чисел
{
    int[] resultArray = new int[size];
    int[] numbersSeriesArray = CreateNumbersSeriesArray(minValue, maxValue);
    ShuffleArray(numbersSeriesArray, shuffleTimes);
    for (int i = 0; i < size; i++)
    {
        resultArray[i] = numbersSeriesArray[i];
    }
    return resultArray;
}

int[,,] Fill3DArrayByNumberSeriesArray(int[] numberSeriesArray) // создание массива 2х2х2 из 8 неповторяющихся двузначных чисел;
{
    int[,,] resultArray = new int[2, 2, 2];
    int index = 0;
    for (int i = 0; i < resultArray.GetLength(0); i++)
        for (int j = 0; j < resultArray.GetLength(1); j++)
            for (int k = 0; k < resultArray.GetLength(2); k++)
            {
                resultArray[i, j, k] = numberSeriesArray[index];
                index++;
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

// int[] numSeriesArr = CreateAnArrayOfNonRepeatingNumbers(size: 8, minValue: 10, maxValue: 100); // массив из 8 неповторяющихся двузначных чисел;
// PrintIntArray(numSeriesArr);
// Console.WriteLine();
// int[,,] task3Array = Fill3DArrayByNumberSeriesArray(numSeriesArr);
// Print3DArrayIntWithIndex(task3Array);


// Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
// Например, на выходе получается вот такой массив:
// 01 02 03 04
// 12 13 14 05
// 11 16 15 06
// 10 09 08 07

int[,] CreateSpiralArray(int size)
{
    int[,] array = new int[size, size];
    int current = 1;
    for (int x = 0; x < (size / 2 + size % 2); x++)
    {
        for (int i = x, j = x; j < size - x; j++) // заполнение слева направо
        {
            array[i, j] = current;
            current++;
        }
        for (int i = x + 1, j = size - x - 1; i < size - x; i++) // заполнение сверху вниз
        {
            array[i, j] = current;
            current++;
        }
        for (int i = size - x - 1, j = size - x - 2; j >= x; j--) // заполнение справа налево
        {
            array[i, j] = current;
            current++;
        }
        for (int i = size - x - 2, j = 0 + x; i >= x + 1; i--) // заполнение снизу вверх
        {
            array[i, j] = current;
            current++;
        }
        // Console.WriteLine($"Проход №{x+1}. Последнее заполненное число {current-1}.");
    }
    return array;
}

void PrettyPrint2DArrayInt(int[,] array, int fillToSigns = 2)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (var j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i, j].ToString($"D{fillToSigns}") + " ");
        Console.WriteLine();
    }
}

PrettyPrint2DArrayInt(CreateSpiralArray(9));