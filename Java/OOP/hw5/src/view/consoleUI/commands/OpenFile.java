package view.consoleUI.commands;

import view.consoleUI.menu.Menu;
import view.consoleUI.notifications.NoticeType;

public class OpenFile extends Command {
    String fileName;
    String folderPath;

    public OpenFile(String folderPath, String fileName) {
        this.fileName = fileName;
        this.folderPath = folderPath;
    }

    @Override
    public String getDescription() {
        if (fileName.length() > 25) {
            return fileName.substring(0, 25) + "<...>" + fileName.substring(fileName.length() - 4);
        }
        return fileName;
    }

    @Override
    public void execute(Menu menu) {
        try {
            presenter.openFile(folderPath, fileName);
            menu.stop();
        } catch (Exception e) {
            notifier.add(e.getMessage(), NoticeType.ERROR);
        }
    }

}
