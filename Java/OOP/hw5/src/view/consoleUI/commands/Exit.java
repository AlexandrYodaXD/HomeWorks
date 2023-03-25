package view.consoleUI.commands;

import view.consoleUI.menu.Menu;

public class Exit extends Command{
    @Override
    public String getDescription() {
        return "Выход";
    }

    @Override
    public void execute(Menu menu) {
        System.exit(0);
    }
}
