package Animal.wildAnimal.Tiger;

import Animal.wildAnimal.wildAnimal;

import java.time.LocalDate;

public class Tiger extends wildAnimal {
    public Tiger(int growth, int weight, String eyeColor, String habitat, LocalDate dateOfLocation) {
        super(growth, weight, eyeColor, habitat, dateOfLocation);
    }

    @Override
    public String getASound() {
        return "Р-р-р!";
    }
}
