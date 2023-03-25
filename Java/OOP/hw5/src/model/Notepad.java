package model;

import model.fileUtils.FileUtils;
import model.fileUtils.FileWorker;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Notepad {
    private List<Note> notes;
    private boolean unsavedChanges = false;
    private FileWorker fileWorker;

    public List<String> getAllTXTFilesNames(String folderPath) {
        return FileUtils.getAllFilesNames(folderPath, ".txt");
    }

    public void open(String folderPath, String fileName) throws IOException {
        if (!unsavedChanges) {
            if (!fileName.endsWith(".txt")) {
                fileName = fileName + ".txt";
            }
            this.fileWorker = new FileWorker(folderPath, fileName);
            List<String> data = fileWorker.read();
            notes = new ArrayList<>();

            for (String noteText : data) {
                notes.add(new Note(noteText));
            }
        } else {
            throw new IllegalStateException("ОШИБКА: Нельзя открыть новый файл, в текущем файле есть несохраненные изменения.");
        }
    }

    public boolean isOpened() {
        return (notes != null);
    }

    public void create(String folderPath, String fileName) throws IOException {
        if (!unsavedChanges) {
            if (!fileName.endsWith(".txt")) {
                fileName = fileName + ".txt";
            }
            this.fileWorker = new FileWorker(folderPath, fileName);

            fileWorker.create(folderPath, fileName);
        } else {
            throw new IllegalStateException("ОШИБКА: Нельзя создать новый файл, в текущем файле есть несохраненные изменения.");
        }
    }


    public String getFileName() throws IOException {
        if (isOpened()) return fileWorker.getFileName();
        else throw new IOException("ОШИБКА: невозможно получить имя файла, файл не открыт.");
    }

    public List<String> getAllTxtFilesNames() throws IOException{
        return fileWorker.getAllFilesNames(".txt");
    }

    public void save() throws IOException {
        List<String> buffer = new ArrayList<>();

        for (Note note : notes) {
            buffer.add(note.getContent());
        }

        fileWorker.write(buffer);
        unsavedChanges = false;
    }

    public void add(String text) throws IOException {
        if (!isOpened()) throw new IOException("ОШИБКА: Невозможно добавить запись, записная книга не открыта.");
        else {
            notes.add(new Note(text));
            unsavedChanges = true;
        }
    }

    public void remove(int index) throws IOException {
        if (!isOpened()) throw new IOException("ОШИБКА: Невозможно удалить запись, записная книга не открыта.");
        else {
            notes.remove(index);
            this.unsavedChanges = true;
        }
    }

    public void replace(int index, String text) throws IOException {

        if (!isOpened()) throw new IOException("ОШИБКА: Невозможно заменить запись, записная книга не открыта.");
        else {
            notes.get(index).setContent(text);
            this.unsavedChanges = true;
        }
    }

    public String getNote(int index){
        return notes.get(index).getContent();
    }

    public List<Note> getAllNotes() throws NullPointerException {
        if (notes != null){
            return new ArrayList<>(notes);
        } else {
            throw new NullPointerException("ОШИБКА: нельзя получить все записи, файл не открыт.");
        }
    }

    public boolean isUnsaved() {
        return unsavedChanges;
    }
}
