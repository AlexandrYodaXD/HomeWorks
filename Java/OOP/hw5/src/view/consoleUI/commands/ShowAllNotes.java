package view.consoleUI.commands;

import model.Note;
import view.consoleUI.menu.FlipMenu;
import view.consoleUI.menu.Menu;
import view.consoleUI.menu.OpeningNoteMenu;
import view.consoleUI.notifications.NoticeType;

import java.util.ArrayList;


public class ShowAllNotes extends Command{
    @Override
    public void execute(Menu menu) {
        try {
            ArrayList<Note> notes = presenter.getAllNotes();

            if (notes.isEmpty()) {
                notifier.add("Список записей пуст.\n", NoticeType.INFO);
                menu.stop();
            } else {
                FlipMenu openingNoteMenu = new OpeningNoteMenu("Все записи", false);
                openingNoteMenu.setList(notes);
                openingNoteMenu.run();
            }

        } catch (Exception e) {
            notifier.add(e.getMessage(), NoticeType.ERROR);
        }
    }

    @Override
    public String getDescription() {
        return "Показать все записи";
    }
}
