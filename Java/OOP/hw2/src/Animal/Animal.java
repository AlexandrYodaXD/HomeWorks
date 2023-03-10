package Animal;

public abstract class Animal {
    protected int growth;
    protected int weight;
    protected String eyeColor;

    public Animal(int growth, int weight, String eyeColor) {
        this.growth = growth;
        this.weight = weight;
        this.eyeColor = eyeColor;
    }

    @Override
    public String toString() {
        return "Вид: " + this.getClass().getSimpleName() +
                ", рост: " + growth +
                ", вес: " + weight +
                ", цвет глаз: '" + eyeColor + '\'';
    }

    public abstract String getASound();
}
