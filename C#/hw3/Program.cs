/*
// Задача 19. Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
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
        Console.WriteLine($"Результат после {globalCount} итерации: {firstDigit}_{num}_{lastDigit}.");
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

// Вариант решения 2 (строго для пятизначных чисел).

void IsThisPalindromeNumberSecond(int num)
{
    if (num < 10000 ^ num > 99999)
    {
        Console.WriteLine($"ОШИБКА: введено не пятизначное число.");
    }
    else
    {
        int firstDigit = num / 10000;
        int lastDigit = num % 10;

        if (firstDigit == lastDigit)
        {
            int newNum = num % 10000 / 10;
            firstDigit = newNum / 100;
            lastDigit = newNum % 10;
            if (firstDigit == lastDigit)
                Console.WriteLine($"Число {num} является палиндромом.");
            else
                Console.WriteLine($"Число {num} НЕ является палиндромом.");
        }
        else
            Console.WriteLine($"Число {num} НЕ является палиндромом.");
    
    }
}

Console.Write("Введите число, которое будем проверять на палиндром: ");
int number = Convert.ToInt32(Console.ReadLine());

// для проверки варианта 1А или варианта 1B раскомментировать одну из двух строк ниже
// bool palindromeNumber = IsThisPalindromeNumberFirstA(number); // для проверки варианта 1А
// bool palindromeNumber = IsThisPalindromeNumberFirstB(number); // для проверки варианта 1B

//  для проверки варианта 1А или варианта 1B раскомментировать ветвление ниже
// if (palindromeNumber)
//     Console.WriteLine($"Число {number} является палиндромом.");
// else
//     Console.WriteLine($"Число {number} НЕ является палиндромом.");
//

// для проверки варианта 2 раскоментировать строку ниже
//  IsThisPalindromeNumberSecond(number);
*/



/*
// Задача 21. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
double FindDistance(double ax, double ay, double az, double bx, double by, double bz)
{
    return Math.Sqrt(Math.Pow(ax - bx, 2) + Math.Pow(ay - by, 2) + Math.Pow(az - bz, 2));
}

Console.Write("Введите коордитану X точки A: ");
double ax = Convert.ToDouble(Console.ReadLine());

Console.Write("Введите коордитану Y точки A: ");
double ay = Convert.ToDouble(Console.ReadLine());

Console.Write("Введите коордитану Z точки A: ");
double az = Convert.ToDouble(Console.ReadLine());

Console.WriteLine($"Точка A будет иметь координаты ({ax}, {ay}, {az}).");

Console.Write("Введите коордитану X точки B: ");
double bx = Convert.ToDouble(Console.ReadLine());

Console.Write("Введите коордитану Y точки B: ");
double by = Convert.ToDouble(Console.ReadLine());

Console.Write("Введите коордитану Z точки B: ");
double bz = Convert.ToDouble(Console.ReadLine());

Console.WriteLine($"Точка B будет иметь координаты ({bx}, {by}, {bz}).");

Console.WriteLine($"Расстояние между точкой A({ax}, {ay}, {az}) и точкой B({bx}, {by}, {bz}) примерно равно равно {Math.Round(FindDistance(ax, ay, az, bx, by, bz), 2)}.");
*/



/*
// Задача 23. Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
// Вариант решения 1 (вывод в виде строки).
void QuartsOfNumbersA(int n)
{
    int count = 1;
    while (count <= n)
    {
        Console.Write($"{Math.Pow(count, 3)}");
        if (count < n) Console.Write(", "); // чтобы запятая не ставилась после последнего числа
        count++;
    }
}

// Вариант решения 2 (вывод в виде таблицы).
void QuartsOfNumbersB(int n)
{
    int count = 1;
    int tableSide = Convert.ToInt32(Math.Sqrt(n)); // размер стороны квадратной таблицы, чем больше n, тем больше сторона

    while (count <= n)
    {
        Console.Write($"{Math.Pow(count, 3)} ");
        // if (count < n) Console.Write(", "); // чтобы запятая не ставилась после последнего числа
        if (count % tableSide == 0) Console.WriteLine(); // переносим строку, когда count достигет края таблицы
        count++;
    }
}


Console.Write("Введите число N: ");
int n = Convert.ToInt32(Console.ReadLine());
// QuartsOfNumbersA(n); // в виде строки
QuartsOfNumbersB(n); // в виде таблицы
*/