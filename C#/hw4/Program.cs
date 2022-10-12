void Launcher()
{
    Console.Clear();
    Console.WriteLine("Вас приветствует мастер выбора задачи для запуска (v2).");

    string[] tasksArray = {
        "Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.",
        "Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.",
        "Задача 29: Напишите программу, которая задаёт массив из m элементов и выводит их на экран.",
        "Дополнительное задание. Заполнение массива пользовательскими целыми числами."
    };

    bool loopFlag = true;
    while (loopFlag)
    {
        loopFlag = false;

        for (int i = 0; i < tasksArray.Length; i++)
            Console.WriteLine($"    {i+1}. {tasksArray[i]}");

        Console.Write("Введите номер задачи для запуска >: ");
        var choise = Console.ReadLine();
        Console.WriteLine("=============================================");

        switch (choise)
        {
            case "1":
                CallAPowB();
                break;
            case "2":
                CallSumOfDigits();
                break;
            case "3":
                CallMakeIntArray();
                break;
            case "4":
                PrintIntArray(MakeUserArray());
                break;
            default:
                Console.WriteLine("ОШИБКА. Введен недопустимый номер задачи.");
                loopFlag = true;
                break;
        }

        if (loopFlag == false)
        {
            Console.Write("Запустить другую задачу? 'y' - да, любой иной символ - выход >: ");
            switch(Console.ReadLine())
            {
                case "y":
                case "Y":
                    loopFlag = true;
                    Console.WriteLine("=============================================");
                    break;
                default:
                    Console.WriteLine("ЗАВЕРШЕНИЕ ПРОГРАММЫ.");
                    break;
            }
        }
    }
}

Launcher();


// Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
int APowB(int a, int b)
{
    int res = 1;
    for (int i = 0; i < b; i++)
        res *= a;
    return res;
}

void CallAPowB() // вспомогательный метод с запросом данных и выводом в терминал.
{
    Console.WriteLine("Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.");
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
    Console.WriteLine("Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.");
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
    Console.WriteLine("Задача 29: Напишите программу, которая задаёт массив из m элементов и выводит их на экран.");
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
    Console.WriteLine("Дополнительное задание. Заполнение массива пользовательскими целыми числами.");
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
