package view.consoleUI.commands;

import model.Note;
import view.consoleUI.menu.Menu;
import view.consoleUI.notifications.NoticeType;

public class OpenNote extends Command{
    Note note;

    public OpenNote(int index) {
        this.note = presenter.getAllNotes().get(index);
    }

    @Override
    public void execute(Menu menu) {
        if (note != null){
            notifier.add(note.getContent(), NoticeType.OK); // для теста
        } else {
            notifier.add("Эта ошибка не должна была произойти. Ошибка в при открыть запись.", NoticeType.ERROR);
        }
    }

    @Override
    public String getDescription() {
        String noteContent = note.getContent();
        if (noteContent.length() > 25) {
            return noteContent.substring(0, 25) + "<...>";
        }
        return noteContent;
    }
}
