package view.consoleUI.commands;

import view.consoleUI.ConsoleUI;
import view.consoleUI.menu.FlipMenu;
import view.consoleUI.menu.Menu;
import view.consoleUI.menu.OpeningFileMenu;
import view.consoleUI.notifications.NoticeType;

public class CreateFileOpeningMenu extends Command {
    @Override
    public String getDescription() {
        return "Открыть файл";
    }

    @Override
    public void execute(Menu menu) {
        try {
            FlipMenu openingFileMenu = new OpeningFileMenu("Меню открытия файла", false);
            openingFileMenu.setList(presenter.getAllFilesNames("src/notepads"));
            openingFileMenu.run();
        } catch (Exception e) {
            notifier.add("Что-то пошло не так", NoticeType.ERROR);
            notifier.add(e.getMessage(), NoticeType.ERROR);
        }
    }

}
