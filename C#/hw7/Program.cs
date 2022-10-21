Console.Clear();

void Print2DDoubleArray(double[,] array) // печать массива, состоящего из double элементов
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (var j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j]);
            if (j < array.GetLength(1) - 1) // если это не последний элемент в строке, то ставим запятую после элемента. 
                Console.Write(", ");
        }
        if (i < array.GetLength(0) - 1) // если это не последняя строка, то ставим запятую в конце строки, иначе точку.
                Console.WriteLine(",");
        else Console.WriteLine(".");
    }
}

void PrintDoubleArray(double[] array) // печать массива, состоящего из double элементов
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write(array[i]);
        if (i < array.Length - 1) // ставим запятую после элемента, если это не последний элемент
            Console.Write(", ");
    }
}

// /*
// Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
// m = 3, n = 4.
// 0,5 7 -2 -0,2
// 1 -3,3 8 -9,9
// 8 7,8 -7,1 9

double[,] Create2DRandomDoubleArray(int rows, int columns, int minValue, int maxValue, int roundValue)
{
    
    double[,] array = new double[rows, columns];

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            double integerPart = new Random().Next(minValue, maxValue); // генерация целой части числа.
            double fractionalPart = new Random().NextDouble(); // генерация дробной части числа.
            array[i, j] = Math.Round(integerPart + fractionalPart, roundValue); // складываем целую и дробную части, округляем до roundValue знаков после запятой.
        }
    }
    return array;
}

Console.Write("Введите количество строк >: ");
int m = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов >: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите минимальное возможное значение >: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите максимальное возможное значение >: ");
int max = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите до скольки знаков после запятой округлять >: ");
int round = Convert.ToInt32(Console.ReadLine());

double[,] resTask1 = Create2DRandomDoubleArray(rows: m, columns: n, minValue: min, maxValue: max, roundValue: round);

Print2DDoubleArray(resTask1);
// */


// /*
// Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4

// 1 7 -> числа с такими индексами в массиве нет

double[,] task2Array =
{
    {1, 4, 7, 2},
    {5, 9, 2, 3},
    {8, 4, 2, 4}
};

double? GetElemByIndex(double[,] array, int fRow, int fColumn) // если индекс элемента массива не выходит за рамки массива, то возвращается значение элемента массива по этому индексу, иначе возвращается null.
{
    if(fRow < array.GetLength(0) && fColumn < array.GetLength(1)) return array[fRow, fColumn];
    return null;
}

Print2DDoubleArray(task2Array); // печатаем массив
Console.WriteLine();

Console.Write("Введите индекс строки элемента >: ");
int idxI = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите индекс столбца элемента >: ");
int idxJ = Convert.ToInt32(Console.ReadLine());

double? resTask2 = GetElemByIndex(task2Array, idxI, idxJ); // при помощи "?" создаем переменную, которая может хранить значение null.

if(resTask2 == null)
    Console.WriteLine($"Элемент массива с индексом [{idxI}, {idxJ}] отсутствует.");
else
    Console.WriteLine($"Элемент массива с индексом [{idxI}, {idxJ}] имеет значение {task2Array[idxI, idxJ]}.");
// */

// /*
// Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4

// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.

double[,] task3Array =
{
    {1, 4, 7, 2},
    {5, 9, 2, 3},
    {8, 4, 2, 4}
};

double[] AverageOfColumns(double[,] array)
{
    double[] result = new double[array.GetLength(1)];
    for (var j = 0; j < array.GetLength(1); j++)
    {
        double sum = 0;
        for (var i = 0; i < array.GetLength(0); i++)
            sum += array[i,j];
        result[j] = Math.Round(sum / array.GetLength(0), 2);
    }
    return result;
}

Print2DDoubleArray(task3Array);
Console.WriteLine();
double[] resTask3 = AverageOfColumns(task3Array);
PrintDoubleArray(resTask3);
// */