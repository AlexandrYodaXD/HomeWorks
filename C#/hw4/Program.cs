void LaunchMenu()
{   Console.Clear();

    string[] tasksArray = {"Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.",
        "Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.",
        "Задача 29: Напишите программу, которая задаёт массив из m элементов и выводит их на экран.",
        "Дополнительное задание. Заполнение массива пользовательскими целыми числами."
    };

    Console.WriteLine("Вас приветствует Мастер выбора задачи для запуска.");
    for (int i = 0; i < tasksArray.Length; i++)
        Console.WriteLine($"    {i+1}. {tasksArray[i]}");

    Console.Write("Введите номер задачи для запуска >: ");
    int choise = Convert.ToInt32(Console.ReadLine());

    while (choise < 0 ^ choise > tasksArray.Length)
    {
        Console.WriteLine("ОШИБКА. Введен недопустимый номер задачи.");
        Console.Write("Введите номер задачи для запуска >: ");
        choise = Convert.ToInt32(Console.ReadLine());
    }
    Console.WriteLine("=============================================");
    Console.WriteLine(tasksArray[choise-1]);
    if (choise == 1) CallAPowB();
    else if (choise == 2) CallSumOfDigits();
    else if (choise == 3) CallMakeIntArray();
    else if (choise == 4) PrintIntArray(MakeUserArray());

}

LaunchMenu();


// Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
double APowB(int a, int b)
{
    return Math.Pow(a, b);
}

void CallAPowB() // вспомогательный метод с запросом данных и выводом в терминал.
{
    Console.Write("Введите первое число >: ");
    int numberA = Convert.ToInt32(Console.ReadLine());
    Console.Write("Введите второе число >: ");
    int numberB = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine($"{numberA}^{numberB} = {APowB(numberA, numberB)}");
}


// Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
int SumOfDigits(int num) // принимает целое число, возвращает сумму цифр введенного числа
{
    int res = 0;
    if (num < 0) num *= -1;

    while (num > 0)
    {
        res += num % 10;
        num /= 10;
    }

    return res;
}

void CallSumOfDigits() // вспомогательный метод с запросом данных и выводом в терминал.
{
    Console.Write("Введите число >: ");
    int number = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine($"Сумма цифр числа {number} равна {SumOfDigits(number)}.");
}


// Задача 29: Напишите программу, которая задаёт массив из m элементов и выводит их на экран.
int[] MakeIntArray(int size, int minValue, int maxValue) // принимает целое число в качестве размера массива, верхнюю и нижнюю границу для генерации чисел, возвращает массив заданного размера, заполненный случайными числами от нижней до верхней границы чисел включительно.
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

void CallMakeIntArray() // вспомогательный метод с запросом данных и выводом в терминал.
{
    Console.Write("Введите размер массива >: ");
    int arrSize = Convert.ToInt32(Console.ReadLine());
    while (arrSize < 0)
    {
        Console.WriteLine("ОШИБКА! Размер массива не может быть отрицательным!");
        Console.Write("Введите размер массива (неотрицательное число) >: ");
        arrSize = Convert.ToInt32(Console.ReadLine());
    }

    Console.Write("Введите нижнюю границу для генерации чисел >: ");
    int minValue = Convert.ToInt32(Console.ReadLine());

    Console.Write("Введите верхнюю границу для генерации чисел >: ");
    int maxValue = Convert.ToInt32(Console.ReadLine());

    PrintIntArray(MakeIntArray(arrSize, minValue, maxValue));
}


// Дополнительное задание.
int[] MakeUserArray() // заполнение массива пользовательскими целыми числами
{
    Console.Write("Введите размер массива >: ");
    int size = Convert.ToInt32(Console.ReadLine());

    while (size < 0)
    {
        Console.WriteLine("ОШИБКА! Размер массива не может быть отрицательным!");
        Console.Write("Введите размер массива (неотрицательное число) >: ");
        size = Convert.ToInt32(Console.ReadLine());
    }

    int[] array = new int[size];

    if (size == 0)
        Console.WriteLine("Размер массива равен нулю, возвращаю пустой массив.");
    else
    {
        Console.WriteLine($"Создан массив с размером {size}. Давайте его заполним!");
        for (int i = 0; i < size; i++)
        {
            Console.Write($"Введите элемент массива ({i+1}/{size}) >: ");
            array[i] = Convert.ToInt32(Console.ReadLine());
        }
        Console.WriteLine($"Массив из {size} элемента(-ов) заполнен, возвращаю массив.");
        
    }

    return array;
}
