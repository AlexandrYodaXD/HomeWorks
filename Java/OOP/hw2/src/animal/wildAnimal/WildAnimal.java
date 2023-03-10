package animal.wildAnimal;

import animal.Animal;

import java.time.LocalDate;

public abstract class WildAnimal extends Animal {
    protected String habitat;
    protected LocalDate dateOfLocation;

    public WildAnimal(int growth, int weight, String eyeColor, String habitat, LocalDate dateOfLocation) {
        super(growth, weight, eyeColor);
        this.habitat = habitat;
        this.dateOfLocation = dateOfLocation;
    }
}
