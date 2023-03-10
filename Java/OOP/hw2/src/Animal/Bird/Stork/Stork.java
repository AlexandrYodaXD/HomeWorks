package Animal.Bird.Stork;

import Animal.Bird.Bird;

public class Stork extends Bird {
    public Stork(int growth, int weight, String eyeColor, int flightAltitude) {
        super(growth, weight, eyeColor, flightAltitude);
    }

    @Override
    public String getASound() {
        return "Иуиуиуиу!";
    }
}
