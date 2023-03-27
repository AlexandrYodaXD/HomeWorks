package view.consoleUI.commands;

import model.Note;
import view.consoleUI.menu.*;
import view.consoleUI.notifications.NoticeType;

import java.util.ArrayList;
import java.util.List;

public class OpenNote extends Command{
    Note note;

    public OpenNote(int index) {
        this.note = presenter.getAllNotes().get(index);
    }

    @Override
    public void execute(Menu menu) {
        if (note != null){
            menu.stop();
//            SimpleMenu simpleMenu = new WorkWithNoteMenu(String.format("Меню работы с записью \"%s\"" ,getDescription()), false, note);
//            simpleMenu.addCommand(new ChangeNote(note));
//            simpleMenu.addCommand(new ShowFullContent(note));
//            simpleMenu.addCommand(new RemoveNote(note));
//            simpleMenu.addCommand(new Placeholder());
//            simpleMenu.addCommand(new Placeholder());
//            simpleMenu.addCommand(new Placeholder());
//            simpleMenu.addCommand(new Placeholder());
//            simpleMenu.addCommand(new Placeholder());
//            simpleMenu.addCommand(new Cancel());
//            simpleMenu.run();
            List<Command> commands = new ArrayList<>();
            commands.add(new ChangeNote(note));
            commands.add(new ShowFullContent(note));
            commands.add(new RemoveNote(note));
            FlipMenu flipMenu = new FlipMenu(String.format("Меню работы с записью \"%s\"" ,getDescription()), false) {
                @Override
                public void fillCommands() {
                    addCommand(new ChangeNote(note));
                    addCommand(new ShowFullContent(note));
                    addCommand(new RemoveNote(note));
                }
            };
            flipMenu.setList(new ArrayList<>());
            flipMenu.run();

            notifier.add(note.getContent(), NoticeType.OK); // для теста
        } else {
            notifier.add("Эта ошибка не должна была произойти. Ошибка в при открытии записи.", NoticeType.ERROR);
        }
    }

    @Override
    public String getDescription() {
        String noteContent = note.getContent();
        if (noteContent.length() > 25) {
            return noteContent.substring(0, 25) + "<...>";
        }
        return noteContent;
    }
}
