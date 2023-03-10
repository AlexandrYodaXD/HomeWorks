package animal.petAnimal.Cat;

import animal.petAnimal.Pet;

import java.time.LocalDate;

public class Cat extends Pet{
    private boolean presenceOfWool;

    public Cat(int growth, int weight, String eyeColor, String name, String breed, boolean vaccinated,
               String coatColor, LocalDate dateOfBirth, boolean presenceOfWool) {
        super(growth, weight, eyeColor, name, breed, vaccinated, coatColor, dateOfBirth);
        this.presenceOfWool = presenceOfWool;
    }

    public boolean isPresenceOfWool() {
        return presenceOfWool;
    }

    @Override
    public String getASound() {
        return "Мяу!";
    }

    @Override
    public String toString() {
        return super.toString() +
                ", наличие шерсти: " + (presenceOfWool ? "есть" : "нет");
    }

    @Override
    public String showAffection() {
        return "проявлять ласку, мурлыкая";
    }
}
