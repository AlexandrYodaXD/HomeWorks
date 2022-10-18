// Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.

int NumbersGreaterThanZeroV1(int totalIterations)
{
    int count = 0;
    
    for (var iterationCounter = 0; iterationCounter < totalIterations; iterationCounter++)
    {
        Console.Write($"({iterationCounter+1}/{totalIterations}) Введите число >: ");
        if (Convert.ToInt32(Console.ReadLine()) > 0) count++;
    }
    return count;
}

int NumbersGreaterThanZeroV2(int totalIterations)
{
    int iterationCounter = 0;
    int count = 0;
    do
    {
        Console.Write($"({iterationCounter+1}/{totalIterations}) Введите число: ");
        int num = Convert.ToInt32(Console.ReadLine());
        if (num > 0) count++;
        iterationCounter++;
    }
    while (iterationCounter < totalIterations);
    return count;
}

int NumbersGreaterThanZeroV3()
{
    int iterationCounter = 0;
    int count = 0;
    do
    {
        Console.Write($"{iterationCounter+1}. Введите число: ");
        int num;
        string str = Console.ReadLine();
        if (int.TryParse(str, out num))
        {
            if (num > 0) count++;
            iterationCounter++;
        }
        else
        {
            Console.WriteLine($"'{str}' - это не число, ввод окончен.");
            break;
        }
    }
    while (true);
    return count;
}

void Task_1_Launcher()
{
    bool loopFlag = true;
    while (loopFlag)
    {
        Console.WriteLine("    1. Метод с использованием цикла for.");
        Console.WriteLine("    2. Метод с использованием цикла do-while.");
        Console.WriteLine("    3. Метод с использованием цикла do-while и неограниченным вводом.");
        Console.Write("Какой метод будем использовать? >: ");
        string choise = Console.ReadLine();
        loopFlag = false;
        switch (choise)
            {
                case "1":
                    Console.Write("Сколько чисел будем вводить? >: ");
                    int m1 = Convert.ToInt32(Console.ReadLine());
                    Console.WriteLine($"Колличество введенных чисел больше нуля: {NumbersGreaterThanZeroV1(m1)}.");
                    break;
                case "2":
                    Console.Write("Сколько чисел будем вводить? >: ");
                    int m2 = Convert.ToInt32(Console.ReadLine());
                    Console.WriteLine($"Колличество введенных чисел больше нуля: {NumbersGreaterThanZeroV2(m2)}.");
                    break;
                case "3":
                    Console.WriteLine("Для прекращения ввода введите что-либо отличное от числа.");
                    Console.WriteLine($"Колличество введенных чисел больше нуля: {NumbersGreaterThanZeroV3()}.");
                    break;
                default:
                    Console.WriteLine("ОШИБКА. Введен недопустимый номер.");
                    loopFlag = true;
                    break;
            }
    }
}

Task_1_Launcher();


// Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.

void IntersectionPoint(double b1, double k1, double b2, double k2)
{
    double x = (b1 - b2) / (k2 - k1);
    double y = Math.Round(k2 * x + b2, 2);
    Console.WriteLine($"Координаты точки пересечения прямых: x: {x}, y: {y}.");
}

// IntersectionPoint(2, 5, 4, 9);
