package Animal.Bird;

import Animal.Animal;

public abstract class Bird extends Animal {
    protected int flightAltitude;

    public Bird(int growth, int weight, String eyeColor, int flightAltitude) {
        super(growth, weight, eyeColor);
        this.flightAltitude = flightAltitude;
    }

    protected void fly(){
        System.out.printf("Я лечу на %s метрах.", flightAltitude);
    }
}
