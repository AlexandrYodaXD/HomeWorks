public class ToiletPaper extends HygieneItem {
    protected int numberOfLayers;

    public ToiletPaper(String title, Integer price, Integer count, String unit, int piecesPerPack, int numberOfLayers) {
        super(title, price, count, unit, piecesPerPack);
        this.numberOfLayers = numberOfLayers;
    }

    @Override
    public String toString() {
        return "Туалетная бумага '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", количество в упаковке: " + quantityInThePackage +
                ", слоев: " + numberOfLayers;
    }
}
