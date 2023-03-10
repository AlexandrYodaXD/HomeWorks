package animal.bird.stork;

import animal.bird.Bird;

public class Stork extends Bird {
    public Stork(int growth, int weight, String eyeColor, int flightAltitude) {
        super(growth, weight, eyeColor, flightAltitude);
    }

    @Override
    public String getASound() {
        return "Иииииууууу!";
    }

    @Override
    public String fly() {
        return "летать";
    }
}
