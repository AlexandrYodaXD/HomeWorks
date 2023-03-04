public class Food extends Product {
    protected int expirationDateInDays;

    public Food(String title, Integer price, Integer count, String unit, int expirationDateInDays) {
        super(title, price, count, unit);
        this.expirationDateInDays = expirationDateInDays;
    }

     @Override
    public String toString() {
        return "Продукт питания '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", срок годности: " + expirationDateInDays + " д";
    }
}
