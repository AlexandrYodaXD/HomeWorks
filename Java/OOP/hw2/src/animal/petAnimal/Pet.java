package animal.petAnimal;

import animal.Animal;

import java.time.LocalDate;

public abstract class Pet extends Animal {

    protected String name;
    protected String breed;
    protected boolean vaccinated;
    protected String coatColor;
    protected LocalDate dateOfBirth;

    public Pet(int growth, int weight, String eyeColor,
               String name, String breed, boolean vaccinated, String coatColor, LocalDate dateOfBirth) {
        super(growth, weight, eyeColor);
        this.name = name;
        this.breed = breed;
        this.vaccinated = vaccinated;
        this.coatColor = coatColor;
        this.dateOfBirth = dateOfBirth;
    }

    public abstract String getAffection();

    @Override
    public String toString() {
        return super.toString() +
                ", кличка: '" + name + '\'' +
                ", порода: '" + breed + '\'' +
                ", наличие прививок: " + (vaccinated ? "есть": "нет") +
                ", цвет шерсти: '" + coatColor + '\'' +
                ", дата рождения: " + dateOfBirth;
    }
}
