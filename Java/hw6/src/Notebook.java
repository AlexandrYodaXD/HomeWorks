
public class Notebook {
    String title;
    Double size;
    Integer[] resolution;
    Integer ram;
    Integer ssd;
    Integer price;

    public Notebook(String title, Double size, Integer[] resolution, Integer ram, Integer ssd, Integer price) {
        this.title = title;
        this.size = size;
        this.resolution = resolution;
        this.ram = ram;
        this.ssd = ssd;
        this.price = price;
    }

    /**
     * Метод для формирования и возврата всех характеристик ноутбука в виде строки,
     * например, "Название: 'MSI Katana G76'; Размер экрана: 17,3"; Разрешение: 1920x1080; RAM: 8 GB; SSD: 512 GB; Цена: 78900 ₽."
     * Если характеристика равна null, то при помощи тернарного оператора она будет равна "N/A".
     *
     * @return Возвращает строку с характеристиками ноутбука.
     */
    @Override
    public String toString() {
        String title = "Название: " +
                (this.title == null ? "N/A" : String.format("'%s'", this.title));
        String size = "; Размер экрана: " +
                (this.size == null ? "N/A" : String.format("%.1f", this.size) + '"');
        String resolution = "; Разрешение: " +
                (this.resolution[0] == null || this.resolution[1] == null ? "N/A" :
                        String.format("%dx%d", this.resolution[0], this.resolution[1]));
        String ram = "; RAM: " +
                (this.ram == null ? "N/A" : this.ram + " GB");
        String ssd = "; SSD: " +
                (this.ssd == null ? "N/A" : this.ssd + " GB");
        String price = "; Цена: " +
                (this.price == null ? "N/A" : this.price + " ₽");

        return title + size + resolution + ram + ssd + price;
    }

    /**
     * Метод для сравнения настоящего объекта Ноутбука с другим.
     * Характеристики сравниваются только в том случае, если в обоих объектах они не равны null.
     *
     * @param other Объект Ноутбука, с которым сравнивается настоящим.
     * @return Если в настоящем объекте какая-либо из характеристик хуже, чем в сравниваемом, то возвращается false,
     * иначе если все if пройдены, то возвращается true.
     */
    public boolean compareTo(Notebook other) {
        if (this.title != null && other.title != null &&
                !this.title.toLowerCase().contains(other.title.toLowerCase())) return false;
        if (this.size != null && other.size != null &&
                other.size > this.size) return false;
        if (this.resolution[0] != null && this.resolution[1] != null &&
                other.resolution[0] != null && other.resolution[1] != null &&
                (this.resolution[0] * this.resolution[1]) < (other.resolution[0] * other.resolution[1])) return false;
        if (this.ram != null && other.ram != null &&
                this.ram < other.ram) return false;
        if (this.ssd != null && other.ssd != null &&
                other.ssd > this.ssd) return false;
        if (this.price != null && other.price != null &&
                this.price < other.price) return false;
        return true;
    }
}
