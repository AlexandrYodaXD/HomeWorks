package animal.bird;

import animal.Animal;

public abstract class Bird extends Animal implements Fly{
    protected int flightAltitude;

    public Bird(int growth, int weight, String eyeColor, int flightAltitude) {
        super(growth, weight, eyeColor);
        this.flightAltitude = flightAltitude;
    }

    protected void showFly(){
        System.out.printf("Я лечу на %s метрах.", flightAltitude);
    }
}
