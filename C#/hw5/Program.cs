int[] MakeRandomIntArray(int size, int minValue, int maxValue) // принимает целое число в качестве размера массива, верхнюю и нижнюю границу для генерации чисел, возвращает массив заданного размера, заполненный случайными числами от нижней до верхней границы чисел включительно.
{
    int[] array = new int[size];

    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(minValue, maxValue + 1);
    }
    return array;
}

double[] MakeRandomDoubleArray(int size, int upperLimitDigitsBeforDecimal, int digitsAfterDecimal) // принимает целое число в качестве размера массива, верхнюю и нижнюю границу для генерации чисел, возвращает массив заданного размера, заполненный случайными числами от нижней до верхней границы чисел включительно.
{
    double[] array = new double[size];

    for (int i = 0; i < array.Length; i++)
    {
        double newRnd = new Random().NextDouble(); // создает случайное число в диапазоне от 0.0 до 0.(9)
        newRnd = newRnd * Math.Pow(10, new Random().Next(0, upperLimitDigitsBeforDecimal + 1)); // Умножаем наше рандомное число на 10 в рандомно выбранной степени (вплоть до upperLimitDigitsBeforDecimal) чтобы увеличить кол-во знаков перед запятой.
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

void PrintDoubleArray(double[] array) // печать массива, состоящего из int элементов
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

int DifMinMax(int[] arr)
{
    int min = arr[0];
    int max = arr[0];

    for (int i = 1; i < arr.Length; i++)
    {
        if (arr[i] > max) max = arr[i];
        else if (arr[i] < min) min = arr[i];
    }
    return max - min;
}

double[] newArr = MakeRandomDoubleArray(10, 2, 2);
PrintDoubleArray(newArr);
// Console.WriteLine(DifMinMax(newArr));


// Дополнительное задание. Найдите произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Результат запишите в новом массиве.
