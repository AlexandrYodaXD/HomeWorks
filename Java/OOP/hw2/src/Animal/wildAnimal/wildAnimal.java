package Animal.wildAnimal;

import Animal.Animal;

import java.time.LocalDate;

public abstract class wildAnimal extends Animal {
    public wildAnimal(int growth, int weight, String eyeColor, String habitat, LocalDate dateOfLocation) {
        super(growth, weight, eyeColor);
        Habitat = habitat;
        this.dateOfLocation = dateOfLocation;
    }

    protected String Habitat;
    protected LocalDate dateOfLocation;
}
