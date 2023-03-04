public class Milk extends Drink {
    protected double percentageOfFatContent;
    protected int expirationDateInDays;

    public Milk(String title, Integer price, Integer count, String unit, double volume, double percentageOfFatContent, int expirationDateInDays) {
        super(title, price, count, unit, volume);
        this.percentageOfFatContent = percentageOfFatContent;
        this.expirationDateInDays = expirationDateInDays;
    }

    @Override
    public String toString() {
        return "Молоко '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", объем: " + volume + " л" +
                ", процент жира: " + String.format("%.1f",percentageOfFatContent) + " %" +
                ", срок годности: " + expirationDateInDays + " д";
    }
}
