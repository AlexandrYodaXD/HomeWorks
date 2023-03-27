package presenter;

import model.Note;
import model.Notepad;
import view.View;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Presenter {
    private final Notepad notepad;

    public Presenter(View view, Notepad notepad) {
        this.notepad = notepad;
        view.setPresenter(this);
    }

    public void openFile(String folderPath, String fileName) throws IOException{
        notepad.open(folderPath, fileName);
    }

    public void createFile(String folderPath, String fileName) throws IOException {
        notepad.create(folderPath, fileName);
    }

    public List<String> getAllFilesNames(String folderPath) {
        return notepad.getAllTXTFilesNames(folderPath);
    }

    public ArrayList<Note> getAllNotes() throws NullPointerException {
        return (ArrayList<Note>) notepad.getAllNotes();
    }

    public boolean fileIsOpened() {
        return notepad.isOpened();
    }

    public String getFileName() {
        try {
            return notepad.getFileName();
        } catch (Exception e){
            return "N/A";
        }
    }

    public void replaceNote(int index, String newNote) throws IOException {
        notepad.replace(index, newNote);
    }

    public boolean isUnsaved(){
        return notepad.isUnsaved();
    }

    public void removeNote(int index) throws IOException {
        notepad.remove(index);
    }
    public void removeNote(Note note) throws IOException {
        notepad.remove(note);
    }

    public void saveChanges() throws IOException {
        notepad.save();
    }

    public void addNote(String newNote) throws IOException {
        notepad.add(newNote);
    }
}
