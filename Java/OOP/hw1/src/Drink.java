public class Drink extends Product {
    protected double volume;

    public Drink(String title, Integer price, Integer count, String unit, double volume) {
        super(title, price, count, unit);
        this.volume = volume;
    }


    @Override
    public String toString() {
        return "Напиток '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", объем: " + volume + "л";
    }
}
