public class Bread extends Food {
    protected String flourGrade;

    public Bread(String title, Integer price, Integer count, String unit, int expirationDateInDays, String flourGrade) {
        super(title, price, count, unit, expirationDateInDays);
        this.flourGrade = flourGrade;
    }

    @Override
    public String toString() {
        return "Хлеб '" + title + '\'' +
                ", цена: " + price + " ₽" +
                ", колличество: " + count + " " + unit +
                ", срок годности: " + expirationDateInDays + " д" +
                ", мука: " + flourGrade;
    }
}
