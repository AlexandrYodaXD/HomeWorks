/*
3* . Дана json строка (можно сохранить в файл и читать из файла)
[{"фамилия":"Иванов","оценка":"5","предмет":"Математика"},
{"фамилия":"Петрова","оценка":"4","предмет":"Информатика"},
{"фамилия":"Краснов","оценка":"5","предмет":"Физика"}]

Написать метод(ы), который распарсит json и, используя StringBuilder,
создаст строки вида: Студент [фамилия] получил [оценка] по предмету [предмет].

Пример вывода:
Студент Иванов получил 5 по предмету Математика.
Студент Петрова получил 4 по предмету Информатика.
Студент Краснов получил 5 по предмету Физика.
*/

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Map;


public class Task_3 {
    public static void main(String[] args) {
        List<Map<String, Object>> data = jsonParser("Task_3_data.json");
        StringBuilder myString = buildString(data);
        System.out.println(myString);
    }

    public static List<Map<String, Object>> jsonParser(String path) {
        try {
            String content = Files.readString(Paths.get(path), StandardCharsets.UTF_8);
            ObjectMapper objectMapper = new ObjectMapper();
            return objectMapper.readValue(content, new TypeReference<>() {
            });
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static StringBuilder buildString(List<Map<String, Object>> data) {
        StringBuilder omegaString = new StringBuilder();
        for (Map<String, Object> datum : data) {
            omegaString.append(String.format("Студент %s получил %s по предмету %s.\n",
                    datum.get("фамилия"),
                    datum.get("оценка"),
                    datum.get("предмет")));
        }
        return omegaString;
    }
}

