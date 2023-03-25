package view.consoleUI.commands;

import view.consoleUI.menu.CreationFileMenu;
import view.consoleUI.menu.Menu;

public class CreateFileCreationMenu extends Command {
    @Override
    public String getDescription() {
        return "Создать файл";
    }

    @Override
    public void execute(Menu menu) {
        CreationFileMenu creationFileMenu = new CreationFileMenu("Меню создания файла", false);
        creationFileMenu.run();
        menu.stop();
    }
}
