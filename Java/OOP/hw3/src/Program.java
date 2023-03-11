import figure.circle.Circle;
import figure.polygon.rectangle.Rectangle;
import figure.polygon.square.Square;
import figure.polygon.triangle.Triangle;

/*
Написать программу на языках Java, в которой идёт со следующими геометрическими фигурами:
1.Треугольник
2.Квадрат
3.Прямоугольник
4.Круг
В программе имеется массив фигур, с которым можно сделать следующие операции:
1.Добавить новую фигуру
2.Посчитать периметр у всех фигур
3.Посчитать площадь у всех фигур
Для фигуры использовать базовый абстрактный класс фигуры, у которого есть методы посчитать периметр и посчитать площадь
фигуры.
Создать класс-коллекцию фигур В классе-коллекции реализовать методы6
1. Вывода информации о всех периметах, площадях и длиннах окружности всех фигур, где это возможно,
2. добавления новой фигуры,
3. удаления фигуры,
4. изменения фигуры по ндексу,
5. сортировки по площади, вывод информации о всех фигурах.
При создании фигур необходимо осуществлять проверку входных данных на возможность создания данной фигуры и в случае
ошибки выдавать соответствующие сообщения. Перодумать собственную иерархию исключений
 */
public class Program {
    public static void main(String[] args) throws Exception {
        Figures figures = new Figures();
        figures.add(new Rectangle(44, 5));
        figures.add(new Square(5));
        figures.add(new Triangle(7, 14, 10));
        figures.add(new Circle(7));

        System.out.println("До сортировки:");
        figures.showAllInfo();

        System.out.println("\nПосле сортировки:");
        figures.sortByArea();
        figures.showAllInfo();

        System.out.println("\nПосле удаления третьей фигуры:");
        figures.remove(2);
        figures.showAllInfo();

        System.out.println("\nПосле замены третей фигуры на квадрат со стороной 10:");
        figures.set(2, new Square(10));
        figures.showAllInfo();

        System.out.println("\nПосле попытки добавить квадрат со стороной -5:");
        figures.set(2, new Square(-5)); // Exception in thread "main" java.lang.Exception: Многоугольник с такими сторонами не может существовать.
    }
}
