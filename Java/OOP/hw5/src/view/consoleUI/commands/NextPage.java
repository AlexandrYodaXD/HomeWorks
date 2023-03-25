package view.consoleUI.commands;

import view.consoleUI.menu.FlipMenu;
import view.consoleUI.menu.Menu;

public class NextPage extends Command{
    @Override
    public void execute(Menu menu) {
        ((FlipMenu) menu).incrementPage();
    }

    @Override
    public String getDescription() {
        return "Следующая страница";
    }
}
