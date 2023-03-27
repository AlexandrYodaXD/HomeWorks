package view.consoleUI.commands;

import model.Note;
import view.consoleUI.menu.Menu;
import view.consoleUI.notifications.NoticeType;

import java.io.IOException;

public class RemoveNote extends Command {
    Note note;

    public RemoveNote(Note note) {
        this.note = note;
    }

    @Override
    public void execute(Menu menu) {
        try {
            presenter.removeNote(note);
        } catch (IOException e) {
            notifier.add(e.getMessage(), NoticeType.ERROR);
        }
    }

    @Override
    public String getDescription() {
        return "Удалить запись";
    }
}
