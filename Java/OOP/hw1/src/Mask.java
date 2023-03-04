public class Mask extends HygieneItem {
    public Mask(String title, Integer price, Integer count, String unit, int piecesPerPack) {
        super(title, price, count, unit, piecesPerPack);
    }

    @Override
    public String toString() {
        return "Маска для лица '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", количество в упаковке: " + quantityInThePackage;
    }
}
