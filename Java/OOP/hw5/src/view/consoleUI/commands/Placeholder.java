package view.consoleUI.commands;

import view.consoleUI.menu.Menu;
import view.consoleUI.notifications.NoticeType;

public class Placeholder extends Command{
    @Override
    public void execute(Menu menu) {
        notifier.add("Неверная команда", NoticeType.ERROR);
    }

    @Override
    public String getDescription() {
        return null;
    }
}
