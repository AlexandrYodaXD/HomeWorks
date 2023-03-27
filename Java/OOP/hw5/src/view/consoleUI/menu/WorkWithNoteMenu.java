package view.consoleUI.menu;

import model.Note;

public class WorkWithNoteMenu extends SimpleMenu {
    private final Note note;

    public WorkWithNoteMenu(String title, boolean oneTimeLoop, Note note) {
        super(title, oneTimeLoop);
        this.note = note;
    }

//    @Override
//    public void run() {
//        clearConsole();
//        notifier.showNotices();
//        printTitle();
//
//        printCommands();
//
//    }
}
