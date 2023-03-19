package presenter;

import model.Notepad;
import view.View;

import java.io.IOException;
import java.util.ArrayList;

public class Presenter {
    private final Notepad notepad;

    public Presenter(View view, Notepad notepad) {
        this.notepad = notepad;
        view.setPresenter(this);
    }

    public void openFile(String fileName) throws IOException{
        notepad.open(fileName);
        notepad.read();
    }

    public void createFile(String fileName) throws IOException {
        notepad.createFile(fileName);
    }

    public ArrayList<String> getAllFilesNames() {
        return notepad.getAllFilesNames();
    }

    public ArrayList<String> getContent() throws Exception {
        try {
            return notepad.getCash();
        }catch (Exception e){
            throw new Exception("Cash пуст");
        }
    }

    public boolean isOpened() {
        return notepad.isOpened();
    }

    public String getFileName() throws IOException {
        return notepad.getFileName();
    }

    public void replaceNote(int index, String newNote) {
        notepad.replace(index, newNote);
    }

    public boolean isUnsaved(){
        return notepad.isUnsaved();
    }

    public void removeNote(int index) {
        notepad.remove(index);
    }

    public void saveChanges() throws IOException {
        notepad.save();
    }

    public void addNote(String newNote) {
        notepad.add(newNote);
    }
}
