package animal.wildAnimal.tiger;

import animal.wildAnimal.WildAnimal;

import java.time.LocalDate;

public class Tiger extends WildAnimal {
    public Tiger(int growth, int weight, String eyeColor, String habitat, LocalDate dateOfLocation) {
        super(growth, weight, eyeColor, habitat, dateOfLocation);
    }

    @Override
    public String getASound() {
        return "Р-р-р!";
    }
}
