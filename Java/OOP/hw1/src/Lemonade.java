public class Lemonade extends Drink {
    public Lemonade(String title, Integer price, Integer count, String unit, double volume) {
        super(title, price, count, unit, volume);
    }

    @Override
    public String toString() {
        return "Лимонад '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", объем: " + volume + " л";
    }
}
