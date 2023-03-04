public class Product {
    protected String title;
    protected Integer price;
    protected Integer count;
    protected String unit;

    public Product(String title, Integer price, Integer count, String unit) {
        this.title = title;
        this.price = price;
        this.count = count;
        this.unit = unit;
    }

    @Override
    public String toString() {
        return "Продукт '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit;
    }
}
