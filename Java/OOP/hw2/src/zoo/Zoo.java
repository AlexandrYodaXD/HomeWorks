package zoo;

import animal.Animal;

import java.util.ArrayList;

public class Zoo {
    private ArrayList<Animal> zooList;

    public Zoo() {
        this.zooList = new ArrayList<Animal>();
    }

    public void add(Animal animal){
        zooList.add(animal);
    }

    public void remove(int i){
        zooList.remove(i);
    }

    public void show(int i){
        System.out.println(zooList.get(i).toString());
    }

    public void makeSound(int i){
        System.out.println(zooList.get(i).getASound());
    }

    public void showAll(){
        for (Animal animal : zooList) {
            System.out.println(animal.toString());
        }
    }

    public void makeSoundAll(){
        for (Animal animal : zooList) {
            System.out.printf("%s говорит \"%s\"\n", animal.getClass().getSimpleName(), animal.getASound());
        }
    }
}
