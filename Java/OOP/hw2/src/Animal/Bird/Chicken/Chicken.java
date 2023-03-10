package Animal.Bird.Chicken;

import Animal.Bird.Bird;

public class Chicken extends Bird {
    public Chicken(int growth, int weight, String eyeColor, int flightAltitude) {
        super(growth, weight, eyeColor, flightAltitude);
    }

    @Override
    public String getASound() {
        return "Куд-кудах!";
    }
}
