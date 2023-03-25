package view.consoleUI.menu;

import view.consoleUI.commands.OpenFile;

public class OpeningFileMenu extends FlipMenu {
    public OpeningFileMenu(String title, boolean oneTimeLoop) {
        super(title, oneTimeLoop);
    }

    @Override
    protected void fillCommands() {
        // Добавляем по SIZE (7) комманд в список команд
        for (int i = currentPage * SIZE; i < (currentPage + 1) * SIZE && i < list.size(); i++) {
            this.addCommand(new OpenFile("src/notepads", (String) list.get(i)));
        }
    }
}
