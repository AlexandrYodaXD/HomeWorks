package view.consoleUI.menu;

import view.consoleUI.commands.*;
import view.consoleUI.notifications.NoticeType;

import java.util.ArrayList;
import java.util.List;

abstract public class FlipMenu extends Menu {
    private final List<Command> commands = new ArrayList<>();
    int currentPage = 0;
    final int SIZE = 7;
    List<?> list;
    public FlipMenu(String title, boolean oneTimeLoop) {
        super(title, oneTimeLoop);
    }

    public void setList(List<?> list) {
        this.list = list;
    }

    @Override
    public void run() {
            do {
                clearConsole();
                notifier.showNotices();
                printTitle();

                clearCommands();
                fillCommands();

                // Дозаполняем список команд командами-пустышками, чтобы пункты меню Следующая страница,
                // Предыдущая страница и Отмена всегда были под цифрами 8, 9 и 0 соответственно.
                while (commands.size() < 7) {
                    commands.add(new Placeholder());
                }

                // Добавляем пункт меню "Предыдущая страница" если есть куда листать.
                if (currentPage > 0) {
                    this.addCommand(new PreviousPage());
                } else {
                    addCommand(new Placeholder());
                }

                // Добавляем пункт меню "Следующая страница" если есть куда листать.
                if (currentPage * SIZE + SIZE < list.size()) {
                    this.addCommand(new NextPage());
                } else {
                    addCommand(new Placeholder());
                }

                // Добавляем команду Отмена
                this.commands.add(new Cancel());

                printTenCommands();

                // Показываем номер текущей страницы и общее количество страниц, если есть куда листать.
                if (list.size() > SIZE) {
                    System.out.printf("[Страница %d/%d]\n", currentPage + 1, list.size() / SIZE + 1);
                }

                try {
                    System.out.print("Введите команду >: ");
                    String input = scanner.nextLine();
                    int commandNumber = Integer.parseInt(input);
                    commandNumber = (commandNumber == 0) ? 10 : commandNumber;
                    if (commandNumber < 1 || commandNumber > commands.size()) {
                        notifier.add("Неверная команда", NoticeType.ERROR);
                        continue;
                    }

                    Command command = commands.get(commandNumber - 1);
                    command.execute(this);
                } catch (NumberFormatException e) {
                    notifier.add("Неверная команда", NoticeType.ERROR);
                }
            } while (running);
    }

    public void incrementPage(){
        if (currentPage + SIZE < list.size()) currentPage += 1;
    }

    public void decrementPage(){
        if (currentPage > 0) currentPage -= 1;
    }

    public void addCommand(Command command) {
        commands.add(command);
    }

    abstract protected void fillCommands();

    public void clearCommands(){
        commands.clear();
    }

    protected void printTenCommands() {
        for (int i = 0; i < commands.size() && i < 10; i++) {
            int j = (i == 9) ? -10 : 0;
            String commandDescription = commands.get(i).getDescription();
            String text = (commandDescription != null) ? String.format("\t%d. %s%n", i + j + 1, commandDescription) : "";
            System.out.print(text);
        }
    }
}
