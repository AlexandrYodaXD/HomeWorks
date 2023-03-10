package zoo;

import animal.Animal;

import java.util.ArrayList;

public class Zoo {
    private ArrayList<Animal> zooList;

    public Zoo() {
        this.zooList = new ArrayList<Animal>();
    }

    public void add(Animal animal) {
        zooList.add(animal);
    }

    public void remove(int i) {
        zooList.remove(i);
    }

    public void show(int i) {
        for (String property :
                zooList.get(i).toString().split(", ")) {
            System.out.printf("\t%S\n", property);
        }
        ;
    }

    public void showAll() {
        for (int i = 0; i < zooList.size(); i++) {
            System.out.printf("\t%d. %s\n", i + 1, zooList.get(i).toString());
        }
    }

    public void makeSound(int i) {
        Animal animal = zooList.get(i);
        System.out.printf("\t%s говорит \"%s\"\n", animal.getClass().getSimpleName(), animal.getASound());
    }

    public void makeSoundAll() {
        for (Animal animal : zooList) {
            System.out.printf("\t%s говорит \"%s\"\n", animal.getClass().getSimpleName(), animal.getASound());
        }
    }

    public Animal getAnimal(int i){
        return zooList.get(i);
    }
    public ArrayList<Animal> getAll(){
        return zooList;
    }
}
