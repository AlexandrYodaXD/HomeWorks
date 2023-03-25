package view.consoleUI.menu;

import view.consoleUI.ConsoleUI;
import view.consoleUI.notifications.NoticeType;

public class InlineInputMenu extends Menu {
    private String description;

    public InlineInputMenu(String title, boolean oneTimeLoop) {
        super(title, oneTimeLoop);
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public void run() {
        do {
            System.out.print(description + " (для отмены введите 0) >: ");
            String fileName = scanner.nextLine();

            if (fileName.equals("0")) {
                stop();
            } else {
                try {
                    presenter.createFile("src/notepads", fileName);
                    ConsoleUI.notifier.add(String.format("Файл \"%s.txt\" успешно создан!\n", fileName), NoticeType.OK);
                    ConsoleUI.presenter.openFile("src/notepads", fileName);
                    stop();
                } catch (Exception e) {
                    ConsoleUI.notifier.add(e.getMessage(), NoticeType.ERROR);
                }
            }
        } while (running);
    }
}
