package view.consoleUI.commands;

import model.Note;
import view.consoleUI.menu.ChangeNoteMenu;
import view.consoleUI.menu.Menu;

public class ChangeNote extends Command {
    Note note;

    public ChangeNote(Note note) {
        this.note = note;
    }

    @Override
    public void execute(Menu menu) {
        ChangeNoteMenu changeNoteMenu = new ChangeNoteMenu("Меню изменения записи", false, note);
        changeNoteMenu.run();
    }

    @Override
    public String getDescription() {
        return "Изменить запись";
    }
}
