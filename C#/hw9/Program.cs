/*
Задача 64: Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1. Выполнить с помощью рекурсии.
*/

void NumsRow(int n)
{
    Console.Write($"{n} ");
    if(n>1) NumsRow(n-1);
}
void Task64()
{
    int n = 10;
    NumsRow(n);
    Console.ReadKey();
}
// Task64();

/*
Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.

M = 1; N = 15 -> 120
M = 4; N = 8. -> 30
*/

int NumsRowSum(int m, int n)
{
    if(m < n) return NumsRowSum(m, n - 1) + n;
    if(m > n) return NumsRowSum(m - 1, n) + m;
    else return m;
}
void Task66()
{
    int m = 4;
    int n = 8;
    int res = NumsRowSum(m, n);
    Console.WriteLine(res);
    Console.ReadKey();
}
// Task66();

/*
Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
m = 2, n = 3 -> A(m,n) = 9
m = 3, n = 2 -> A(m,n) = 29
*/

int Akkerman(int m, int n)
{
    if (m == 0) return n + 1;
    else if (m > 0 && n == 0) return Akkerman(m - 1, 1);
    else if (m > 0 && n > 0) return Akkerman(m - 1, Akkerman(m, n - 1));
    else
    {
        Console.WriteLine("Этого не должно было случиться, но почему-то случилось... ");
        return 0;
    }
}
void Task68()
{
    int m = 4;
    int n = 4;
    int res = Akkerman(m, n);
    Console.WriteLine(res);
    Console.ReadKey();
}
// Task68();