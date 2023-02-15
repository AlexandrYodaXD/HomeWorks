/*
1 . Дана строка sql-запроса "select * from students where ".
Сформируйте часть WHERE этого запроса, используя StringBuilder.
Данные для фильтрации приведены ниже в виде json строки.
Если значение null, то параметр не должен попадать в запрос.
Параметры для фильтрации: {"name":"Ivanov", "country":"Russia", "city":"Moscow", "age":"null"}
*/

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.util.Map;

public class Task_1 {
    public static void main(String[] args) {
        String prefix = "select * from students where ";
        String request = "{\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\":null}";
        Map<String, Object> data = jsonStringToMap(request);
        System.out.println(buildRequest(data));
        StringBuilder conditions = buildRequest(data);
        System.out.printf("Полная строка запроса выглядела бы так: %s;", prefix + conditions);
    }

    public static Map<String, Object> jsonStringToMap(String content) {
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            Map<String, Object> data;
            data = objectMapper.readValue(content, new TypeReference<>() {
            });
            return data;
        } catch (JsonProcessingException e) {
            throw new RuntimeException(e);
        }
    }

    public static StringBuilder buildRequest(Map<String, Object> data) {
        StringBuilder requestString = new StringBuilder();
        String[] keys = data.keySet().toArray(new String[0]);
        for (int i = 0; i < keys.length; i++) {
            String key = keys[i];
            Object value = data.get(key);
            if (value != null){
                if (i != 0) requestString.append(" and ");
                requestString.append(String.format("%s = \"%s\"", key,value));
            }
        }
        return requestString;
    }
}
