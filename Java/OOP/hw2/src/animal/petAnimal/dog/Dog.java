package animal.petAnimal.dog;

import animal.petAnimal.Pet;

import java.time.LocalDate;

public class Dog extends Pet {
    private boolean trained;

    public Dog(int growth, int weight, String eyeColor, String name, String breed, boolean vaccinated,
               String coatColor, LocalDate dateOfBirth, boolean trained) {
        super(growth, weight, eyeColor, name, breed, vaccinated, coatColor, dateOfBirth);
        this.trained = trained;
    }

    public boolean isTrained() {
        return trained;
    }

    @Override
    public String getASound() {
        return "Гав!";
    }

    @Override
    public String getAffection() {
        return "Виляет хвостом.";
    }

    @Override
    public String toString() {
        return super.toString() +
                ", наличие дрессировки: " + (trained ? "есть" : "нет");
    }

    public void train(){
        if (!trained){
            trained = true;
            System.out.printf("Теперь %s дрессированная пёс!", this.name);
        }
        else {
            System.out.printf("%s уже был дрессированным псом!", this.name);
        }
    }
}
