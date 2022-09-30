/*
// Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.

Console.Write("Input first number: ");
int firstNum = Convert.ToInt32(Console.ReadLine());

Console.Write("Input second number: ");
int secondNum = Convert.ToInt32(Console.ReadLine());

if (firstNum > secondNum)
{
    Console.WriteLine($"The first number {firstNum} is greater than the second number {secondNum}.");
}
else if (firstNum < secondNum)
{
    Console.WriteLine($"The second number {secondNum} is greater than the first number {firstNum}.");
}
else
{
    Console.WriteLine($"The first number {secondNum} and the second number {firstNum} are equal.");
}
*/

/*
// Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.

Console.Write("Input first number: ");
int firstNum = Convert.ToInt32(Console.ReadLine());

Console.Write("Input second number: ");
int secondNum = Convert.ToInt32(Console.ReadLine());

Console.Write("Input third number: ");
int thirdNum = Convert.ToInt32(Console.ReadLine());

int greater = firstNum;

if (secondNum > greater)
{
    greater = secondNum;
}

if (thirdNum > greater)
{
    greater = thirdNum;
}

Console.WriteLine($"Greater num is {greater}");
*/

/*
// Задача 6: Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).

Console.Write("Input number: ");
int num = Convert.ToInt32(Console.ReadLine());

if (num % 2 == 0)
{
    Console.WriteLine($"Number {num} is even.");
}
else
{
    Console.WriteLine($"Number {num} is odd (uneven).");
}
*/

/*
// Задача 8: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
// Добавил проверку на ввод отрицательного числа, либо 0.
// В случае ввода числа -5 получается последовательность 0 -2 -4, что соответствует условию задачи.

Console.Write("Input number: ");
int num = Convert.ToInt32(Console.ReadLine());

if (num > 0)
{
    int current = 2;
    while (current <= num)
    {
        Console.Write(current + " ");
        current += 2;
    }
}
else if (num <= 0)
{
    int current = 0;
    while (current >= num)
    {
        Console.Write(current + " ");
        current -= 2;
    }
}

*/