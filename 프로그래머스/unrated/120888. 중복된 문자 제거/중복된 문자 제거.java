import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
       ArrayList<String> answer = new ArrayList<>();

        Arrays.stream(my_string.split(""))
                .distinct()
                .forEach(answer::add);

        return String.join("", answer);
    }
}