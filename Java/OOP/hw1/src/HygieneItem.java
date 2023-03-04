public class HygieneItem extends Product {
    protected int quantityInThePackage;

    public HygieneItem(String title, Integer price, Integer count, String unit, int piecesPerPack) {
        super(title, price, count, unit);
        this.quantityInThePackage = piecesPerPack;
    }

    @Override
    public String toString() {
        return "Предмет гигиены '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", количество в упаковке: " + quantityInThePackage;
    }
}
