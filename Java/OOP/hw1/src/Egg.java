public class Egg extends Product {
    protected int quantityInThePackage;

    public Egg(String title, Integer price, Integer count, String unit, int quantityInThePackage) {
        super(title, price, count, unit);
        this.quantityInThePackage = quantityInThePackage;
    }

    @Override
    public String toString() {
        return "Яйца '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", количество в упаковке: " + quantityInThePackage;
    }
}
