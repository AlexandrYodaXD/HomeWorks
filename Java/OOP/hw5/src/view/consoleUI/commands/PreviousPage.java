package view.consoleUI.commands;

import view.consoleUI.menu.FlipMenu;
import view.consoleUI.menu.Menu;

public class PreviousPage extends Command{
    @Override
    public void execute(Menu menu) {
        ((FlipMenu) menu).decrementPage();
    }

    @Override
    public String getDescription() {
        return "Предыдущая страница";
    }
}
