package view.consoleUI;

import presenter.Presenter;
import view.View;
import view.consoleUI.commands.*;
import view.consoleUI.menu.SimpleMenu;

import java.util.Scanner;

public class ConsoleUI implements View {
    public static Scanner scanner;
    public static Presenter presenter;
    public static Notifier notifier;

    public ConsoleUI() {
        scanner = new Scanner(System.in);
        notifier = new Notifier();
    }

    public void setPresenter(Presenter presenter) {
        ConsoleUI.presenter = presenter;
    }

    public void start() {
        //noinspection InfiniteLoopStatement
        while (true) {

            // Цикл для создания стартового меню, когда файл не открыт
            while (!presenter.fileIsOpened()) {
                SimpleMenu startSimpleMenu = new SimpleMenu("Стартовое меню", true);
                startSimpleMenu.addCommand(new CreateFileCreationMenu());
                startSimpleMenu.addCommand(new CreateFileOpeningMenu());
                startSimpleMenu.addCommand(new Exit());
                startSimpleMenu.run();
            }

            // Цикл для создания стартового меню работы с файлом
            while (presenter.fileIsOpened()) {
                SimpleMenu fileWorkMenu = new SimpleMenu(String.format("\"Меню работы с файлом \"%s\"", presenter.getFileName()), true);
                fileWorkMenu.addCommand(new ShowAllNotes());
                fileWorkMenu.addCommand(new ShowLastNote());
//                fileWorkMenu.addCommand(new AddNewNote());
//                fileWorkMenu.addCommand(new CloseCurrentNotepad());
//                fileWorkMenu.addCommand(new Save());
                fileWorkMenu.addCommand(new Exit());
                fileWorkMenu.run();
            }
        }
    }
}
