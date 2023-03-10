package animal.bird.chicken;

import animal.bird.Bird;

public class Chicken extends Bird {
    public Chicken(int growth, int weight, String eyeColor, int flightAltitude) {
        super(growth, weight, eyeColor, flightAltitude);
    }

    @Override
    public String getASound() {
        return "Куд-кудах!";
    }
}
