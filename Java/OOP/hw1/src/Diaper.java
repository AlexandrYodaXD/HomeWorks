public class Diaper extends ChildrensProducts {
    protected String size;
    protected int minimalWeight;
    protected int maximalWeight;
    protected String type;

    public Diaper(String title, Integer price, Integer count, String unit, int minimalAge, boolean hypoallergenic,
                  String size, int minimalWeight, int maximalWeight, String type) {
        super(title, price, count, unit, minimalAge, hypoallergenic);
        this.size = size;
        this.minimalWeight = minimalWeight;
        this.maximalWeight = maximalWeight;
        this.type = type;
    }

    @Override
    public String toString() {
        return "Подгузник '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", минимальный возраст: " + minimalAge + " г" +
                ", гипоаллергенность: " + (hypoallergenic ? "нет" : "да") +
                ", размер: " + size +
                ", минимальный вес: " + minimalWeight + " кг" +
                ", максимальный вес: " + maximalWeight + " кг" +
                ", тип: " + type;
    }
}
