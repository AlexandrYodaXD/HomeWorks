/*
// Задача 10: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа
int ShowSecondDigitOfNumber(int num)
{
    int result = num / 10 % 10;
    return result;
}

Console.Write("Input number: ");
int numberA = Convert.ToInt32(Console.ReadLine());
int secondDigit = ShowSecondDigitOfNumber(numberA);
Console.WriteLine($"Second digit of {numberA} is {secondDigit}.");
*/

/*
// Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
int ShowThirdDigitOfNumber(int num)
{
    int result;

    if (num <= 99)
        result = -1;
    else
    {
        while (num > 999)
            num = num / 10;
        result = num % 10;
    }
    
    return result;
}

Console.Write("Input number: ");
int numberB = Convert.ToInt32(Console.ReadLine());

int thirdDigit = ShowThirdDigitOfNumber(numberB);

if (thirdDigit > -1)
    Console.WriteLine($"Third digit of {numberB} is {thirdDigit}.");
else
    Console.WriteLine($"No third digit.");
*/

/*
// Задача 15: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
bool IsDayAHoliday(int day)
{
    bool result;

    if (day == 6 ^ day == 7)
        result = true;
    else
        result = false;
    
    return result;
}

Console.Write("Input a number of the day of the week: ");
int dayNumber = Convert.ToInt32(Console.ReadLine());
bool isDayAHoliday = IsDayAHoliday(dayNumber);

if (isDayAHoliday)
    Console.WriteLine($"Yes, the {dayNumber} day of the week is a holiday! :)");
else
    Console.WriteLine($"No, the {dayNumber} day of the week is not a holiday! :(");
*/