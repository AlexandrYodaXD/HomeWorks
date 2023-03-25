package view.consoleUI.commands;

import model.Note;
import view.consoleUI.menu.Menu;

import java.util.List;

public class ShowLastNote extends Command {
    Note note;

    public ShowLastNote() {
        List<Note> allNotes = presenter.getAllNotes();
        if (!presenter.getAllNotes().isEmpty()) {
            this.note = presenter.getAllNotes()
                    .get(allNotes.size() - 1);
        }
    }

    @Override
    public void execute(Menu menu) {
        if (note != null){
            System.out.println("TEST: " + note.getContent()); // для теста
        } else {
            System.out.println("Нуль при попытке показать последнюю запись");
        }
    }

    @Override
    public String getDescription() {
        return "Показать последнюю запись";
    }
}
