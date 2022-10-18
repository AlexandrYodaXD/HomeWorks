// Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.

void NumbersGreaterThanZero()
{
    int count = 0;
    Console.Write("Сколько чисел будем вводить? >: ");
    int m = Convert.ToInt32(Console.ReadLine());
    for (var i = 0; i < m; i++)
    {
        Console.Write($"({i+1}/{m}) Введите число >: ");
        if (Convert.ToInt32(Console.ReadLine()) > 0) count++;
    }
    Console.WriteLine($"Колличество введенных чисел больше нуля: {count}.");
}

NumbersGreaterThanZero();

// Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.

void IntersectionPoint(double b1, double k1, double b2, double k2)
{
    double x = (b1 - b2) / (k2 - k1);
    double y = Math.Round(k2 * x + b2, 2);
    Console.WriteLine($"Координаты точки пересечения прямых: x: {x}, y: {y}.");
}

// Task_2(2, 5, 4, 9);