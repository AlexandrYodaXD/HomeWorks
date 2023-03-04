public class ChildrensProducts extends Product {
    protected int minimalAge;
    protected boolean hypoallergenic;

    public ChildrensProducts(String title, Integer price, Integer count, String unit, int minimalAge, boolean hypoallergenic) {
        super(title, price, count, unit);
        this.minimalAge = minimalAge;
        this.hypoallergenic = hypoallergenic;
    }

    @Override
    public String toString() {
        return "Детский товар '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", минимальный возраст: " + minimalAge + " г" +
                ", гипоаллергенность: " + (hypoallergenic ? "нет" : "да");
    }
}
