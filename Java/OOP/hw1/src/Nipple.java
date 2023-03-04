public class Nipple extends ChildrensProducts {
    public Nipple(String title, Integer price, Integer count, String unit, int minimalAge, boolean hypoallergenic) {
        super(title, price, count, unit, minimalAge, hypoallergenic);
    }

    @Override
    public String toString() {
        return "Соска '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", минимальный возраст: " + minimalAge + " год/лет" +
                ", гипоаллергенность: " + (hypoallergenic ? "нет" : "да");
    }
}
