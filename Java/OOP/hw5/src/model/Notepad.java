package model;

import java.io.*;
import java.util.ArrayList;

public class Notepad {
    File file;
    ArrayList<String> cash;
    boolean unsavedChanges = false;
    private final String FOLDERPATH = "src/notepads";

    public ArrayList<String> getAllFilesNames() {
        ArrayList<String> txtFiles = new ArrayList<>();
        File folder = new File(FOLDERPATH);

        File[] files = folder.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isFile() && file.getName().endsWith(".txt")) {
                    txtFiles.add(file.getName());
                }
            }
        }
        return txtFiles;
    }

    public void open(String fileName) throws IOException {
        if (!fileName.endsWith(".txt")) {
            fileName = fileName + ".txt";
        }
        // Создаем объект файла с заданным именем
        this.file = new File(FOLDERPATH + "/" + fileName);

        // Проверяем существует ли файл
        if (!file.exists()) {
            throw new IOException("ОШИБКА: Файл с таким именем не существует.");
        }
    }

    public void read() throws IOException {
        if (this.isOpened()) {
            ArrayList<String> content = new ArrayList<>();
            FileReader reader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(reader);
            String line;

            while ((line = bufferedReader.readLine()) != null) {
                content.add(line);
            }
            if (cash == null){
                cash = content;
            } else if (cash.equals(content)){
                throw new IOException("ОШИБКА: Попытка считать файл по-новой без сохранения изменений.");
            }
        } else {
            throw new IOException("ОШИБКА: Файл не открыт.");
        }
    }

    public ArrayList<String> getCash() throws IOException {
        if (cash != null){
            return cash;
        } else {
            throw new IOException("Файл не был прочтен.");
        }
    }

    public void createFile(String fileName) throws IOException {
        // Удаляем из названия файла .txt, если пользователь при вводе имени указал его
        if (fileName.endsWith(".txt")) {
            fileName = fileName.substring(0, fileName.length() - 4);
        }

        // Создаем папку с блокнотами
        File notepadsDir = new File(FOLDERPATH);

        // Проверяем, была ли создана папка с блокнотами
        if (!notepadsDir.exists()) {
            if (!notepadsDir.mkdirs()) {
                throw new IOException("ОШИБКА: Не удалось создать папку с блокнотами.");
            }
        }

        // Создаем объект файла с заданным именем
        File file = new File(FOLDERPATH + "/" + fileName + ".txt");


        // Проверяем, существует ли файл
        if (file.exists()) {
            throw new IOException("ОШИБКА: Файл с таким именем уже существует.");
        }

        // Создаем новый файл
        boolean created = file.createNewFile();

        // Проверяем, был ли файл успешно создан
        if (!created) {
            throw new IOException("ОШИБКА: Не удалось создать файл.");
        }
    }

    public boolean isOpened() {
        if (this.file == null) return false;
        return this.file.exists();
    }

    public String getFileName() throws IOException {
        if (this.isOpened()) return file.getName();
        else throw new IOException("ОШИБКА: невозможно получить имя файла, файл не открыт.");
    }

    public void replace(int index, String text) {
        this.cash.set(index, text);
        this.unsavedChanges = true;
    }

    public boolean isUnsaved(){
        return unsavedChanges;
    }

    public void remove(int index) {
        this.cash.remove(index);
        this.unsavedChanges = true;
    }

    public void save() throws IOException {
        FileWriter fileWriter = new FileWriter(FOLDERPATH + "/" + file.getName());
        BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
        for (String note : cash) {
            bufferedWriter.write(note);
            bufferedWriter.newLine();
        }
        bufferedWriter.close();
        this.unsavedChanges = false;
    }

    public void add(String text) {
        cash.add(text);
        this.unsavedChanges = true;
    }
}
