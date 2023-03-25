package view.consoleUI.commands;

import presenter.Presenter;
import view.consoleUI.ConsoleUI;
import view.consoleUI.Notifier;
import view.consoleUI.menu.Menu;

import java.util.Scanner;

public abstract class Command {
    protected final Notifier notifier = ConsoleUI.notifier;
    protected final Scanner scanner = ConsoleUI.scanner;
    protected final Presenter presenter = ConsoleUI.presenter;

    public abstract void execute(Menu menu);
    public abstract String getDescription();
}
