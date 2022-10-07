﻿// Задача 19. Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
// Вариант решения #1A (с комментариями и вспомогательными выводами в консоль).
// Принимаются числа любой длинны, как с четным, так и с нечетным кол-вом цифр.
bool IsThisPalindromeNumberFirstA(int num)
{
    bool res = true; // задаем результирующей переменной значение по умолчанию true
    int globalCount = 1; // эта переменная просто для отображения порядкового номера итерации цикла

    // Основной цикл. В ходе него от числа num будут отсекаться первая и последняя цифры. Когда останется одна цифра (пусть даже 0), цикл прервется, в res останется true, так как если число состоит из одной цифры, то оно является палиндромом.
    while (num > 9)
    {
        Console.WriteLine($"{globalCount} итерация. num равен {num}."); // просто для наглядности показывает чему равен num на начало итерации с номером globalCount
        int lastDigit = num % 10; // переменная, хранящая последнюю цифру
        Console.WriteLine($"Последняя цифра числа {num} является {lastDigit}."); // просто для наглядности

        
        int firstDigit = num; // тут будет храниться первая цифра числа, для начала просто копируем в нее num
        int countOfDigits = 0; // счетчик количества разрядов числа, пригодится позже

        // цикл для нахождения первой цифры числа numCopy. Делим в цикле firstDigit на 10 пока не останется одна цифра.
        while (firstDigit >= 10)
        {
            countOfDigits++;
            firstDigit /= 10;
        }

        Console.WriteLine($"Первой цифрой числа {num} является {firstDigit}."); // для наглядности
        
        // если первая и последняя цифры различаются, то прерываем цикл, в res заносим false
        if (lastDigit != firstDigit)
        {
            res = false;
            Console.WriteLine($"Первая цифра {firstDigit} и последняя цифра {lastDigit} различаются, число не палиндром."); // для наглядности
            break; // прерывает ближайший цикл (while (num > 9))
        }

        // если всё ок и цикл не прервался, находим новое значение для num, без первой и последней цифры
        // Math.Pow(10, countOfDigits - 1) дает нам число, при делении по остатку на которое num даст нам первую цифру
        // по-идее, если я все правильно написал, то ситуцации где Math.Pow(10, countOfDigits - 1) будет равно нулю не должно возникать (но это не точно)
        num = num / 10 % (Convert.ToInt32(Math.Pow(10, countOfDigits - 1)));
        Console.WriteLine($"Результат после {globalCount} итерации: {firstDigit} + {num} + {lastDigit}.");
        globalCount++;
        Console.WriteLine($"================================="); // разделитель для наглядности
    }
    return res;
}

// Вариант решения #1B (без комментариев).
bool IsThisPalindromeNumberFirstB(int num)
{
    bool res = true;

    while (num > 9)
    {
        int lastDigit = num % 10;
        int firstDigit = num;
        int countOfDigits = 0;

        while (firstDigit >= 10)
        {
            countOfDigits++;
            firstDigit /= 10;
        }
        
        if (lastDigit != firstDigit)
        {
            res = false;
            break;
        }

        num = num / 10 % (Convert.ToInt32(Math.Pow(10, countOfDigits - 1)));
    }

    return res;
}

Console.Write("Введите число, которое будем проверять на палиндром: ");
int number = Convert.ToInt32(Console.ReadLine());

bool palindromeNumber = IsThisPalindromeNumberFirstA(number);
// bool palindromeNumber = IsThisPalindromeNumberFirstB(number);

if (palindromeNumber)
    Console.WriteLine($"Число {number} является палиндромом.");
else
    Console.WriteLine($"Число {number} НЕ является палиндромом.");


// Задача 21. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
// Задача 23. Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.