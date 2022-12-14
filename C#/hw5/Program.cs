int[] MakeRandomIntArray(int size, int minValue, int maxValue) // принимает целое число в качестве размера массива, верхнюю и нижнюю границу для генерации чисел, возвращает массив заданного размера, заполненный случайными числами от нижней до верхней границы чисел включительно.
{
    int[] array = new int[size];

    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(minValue, maxValue + 1);
    }
    return array;
}

double[] MakeRandomDoubleArray(int size, int maxDigitsBeforeDecimal, int digitsAfterDecimal) // принимает целое число в качестве размера массива, число upperLimitDigitsBeforDecimal, указывающее на максимальное кол-во знаков перед запятой и число digitsAfterDecimal, указывающее на кол-во знаков после запятой. Будут сгенерированы числа от 0 до +- upperLimitDigitsBeforDecimal + 0.(9)).
{
    double[] array = new double[size];

    for (int i = 0; i < array.Length; i++)
    {
        double newRnd = new Random().NextDouble(); // создает случайное число в диапазоне от 0.0 до 0.(9)
        newRnd = newRnd * Math.Pow(10, new Random().Next(0, maxDigitsBeforeDecimal + 1)); // Умножаем наше рандомное число на 10 в рандомно выбранной степени (вплоть до upperLimitDigitsBeforDecimal) чтобы увеличить кол-во знаков перед запятой.
        newRnd = Math.Round(newRnd, digitsAfterDecimal); // округляем наше число до digitsAfterDecimal знаков.
        newRnd = newRnd * (Math.Pow(-1, new Random().Next(0, 2))); // с вероятностью 50% меняем знак числа на "-".
        array[i] =  newRnd;
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

void PrintDoubleArray(double[] array) // печать массива, состоящего из double элементов
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

int GetNotANegativeNumber(string msg) // в качестве аргумента принимает строку, которая будет выводиться в консоль (приглашение для ввода информации), метод возвращает целое не отрицательное число
{
    Console.Write(msg + " >: ");
    int number = Convert.ToInt32(Console.ReadLine());
    while (number < 0)
    {
        Console.WriteLine("ОШИБКА! Данный параметр не должен быть отрицательным!");
        Console.Write(msg + " >: ");
        number = Convert.ToInt32(Console.ReadLine());
    }
    return number;
}

// Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.
int CountOfEvenNumbers(int[] arr) // считает кол-во четных чисел в массиве.
{
    int count = 0;

    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] % 2 == 0) count ++;
    }

    return count;
}

void Task_1()
{
    int arrSize = GetNotANegativeNumber("Введите размер массива");
    
    int[] arrTask1 = MakeRandomIntArray(arrSize, 100, 999);
    Console.WriteLine($"Создан массив из {arrSize} элемента(ов) из случайно сгенерированных целых чисел в диапазоне [100, 999].");
    PrintIntArray(arrTask1);
    Console.WriteLine($"В массиве {CountOfEvenNumbers(arrTask1)} четных элемента(ов).");
}

// Task_1(); // вызов задачи

// Задача 36: Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
int SumOfNumsWithOddIdx(int[] array)
{
    int sum = 0;
    for (int i = 1; i < array.Length; i += 2)
    {
        sum += array[i];
    }
    return sum;
}

void Task_2()
{
    int arrSize = GetNotANegativeNumber("Введите размер массива");

    Console.Write("Введите нижнюю границу для генерации чисел >: ");
    int minValue = Convert.ToInt32(Console.ReadLine());

    Console.Write("Введите верхнюю границу для генерации чисел >: ");
    int maxValue = Convert.ToInt32(Console.ReadLine());

    int[] arrTask2 = MakeRandomIntArray(arrSize, minValue, maxValue);
    Console.WriteLine($"Создан массив из {arrSize} элемента(ов) из случайно сгенерированных целых чисел в диапазоне [{minValue}, {maxValue}].");
    PrintIntArray(arrTask2);

    Console.WriteLine($"Сумма элементов массива с нечетными индексами равна {SumOfNumsWithOddIdx(arrTask2)}.");
}

// Task_2(); // вызов задачи

// Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
double DifMinMax(double[] arr) // нахождение разницы между максимальным и минимальным элементов массива
{
    double min = arr[0];
    double max = arr[0];

    for (int i = 1; i < arr.Length; i++)
    {
        if (arr[i] > max) max = arr[i];
        else if (arr[i] < min) min = arr[i];
    }
    return max - min;
}

void Task_3()
{
    int arrSize = GetNotANegativeNumber("Введите размер массива");
    int maxDigitsBeforeDecimal = GetNotANegativeNumber("Введите максимальное количество знаков до запятой");
    int digitsAfterDecimal = GetNotANegativeNumber("Введите количество знаков после запятой");
    
    double[] arrayTask3 = MakeRandomDoubleArray(arrSize, maxDigitsBeforeDecimal, digitsAfterDecimal);
    Console.WriteLine($"Создан массив из {arrSize} элемента(ов) из случайно сгенерированных вещественных чисел в диапазоне ({-Math.Pow(10,digitsAfterDecimal)}, {Math.Pow(10,digitsAfterDecimal)}) с точностью в {digitsAfterDecimal} знака(ов) после запятой.");
    PrintDoubleArray(arrayTask3);
    Console.WriteLine($"Разница между самым большим и самым малым элементами массива равна {DifMinMax(arrayTask3)}.");
}

// Task_3(); // вызов задачи

// Дополнительное задание: Найдите произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Результат запишите в новом массиве.

int[]  MultOfPairs(int[] arr) // метод принимает массив и возвращает новый массив, состоящий из пар чисел исходного массива.
{
    int[] resArr = new int[arr.Length / 2 + arr.Length % 2]; // если исходный массив имеет четное кол-во эл-ов, то новый будет размером в половину от исходного, если исходный содержит нечетное кол-во эл-ов, то новый будет размером в половину + 1. Делается это для того чтобы в нечетном массиве добавить центральный элемент, для которого нет пары.
    for (int i = 0; i < arr.Length / 2 + arr.Length % 2; i++)
    {
        if (i != arr.Length - i - 1) resArr[i] = arr[i] * arr[arr.Length - i - 1]; // проверка на то находимся ли мы на центральном элементе нечетного массива.
        else resArr[i] = arr[i];
    }
    return resArr;
}

void Task_4()
{
    int arrSize = GetNotANegativeNumber("Введите размер массива");
    
    int[] arrTask4 = MakeRandomIntArray(arrSize, 10, 99);
    Console.WriteLine($"Создан массив из {arrSize} элемента(ов) из случайно сгенерированных целых чисел в диапазоне [100, 999].");
    PrintIntArray(arrTask4);
    int[] resArrTask4 = MultOfPairs(arrTask4);
    Console.WriteLine("Массив, содержащий суммы парных элементов исходного массива:");
    PrintIntArray(resArrTask4);
}

// Task_4(); // вызов задачи