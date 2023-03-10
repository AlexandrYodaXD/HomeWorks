package animal.wildAnimal.wolf;

import animal.wildAnimal.wildAnimal;

import java.time.LocalDate;

public class Wolf extends wildAnimal {
    private boolean packLeader;

    public Wolf(int growth, int weight, String eyeColor, String habitat, LocalDate dateOfLocation, boolean packLeader) {
        super(growth, weight, eyeColor, habitat, dateOfLocation);
        this.packLeader = packLeader;
    }

    @Override
    public String getASound() {
        return "Ауф!";
    }

    public boolean isPackLeader() {
        return packLeader;
    }
}
