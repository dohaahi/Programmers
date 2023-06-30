import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;

class Solution {
    public String[] solution(String myString) {
        String[] arr = myString.split("x");

        ArrayList<String> list = new ArrayList<>();

        for (String s : arr) {
            if (!Objects.equals(s, "")) {
                list.add(s);
            }
        }

        String[] answer = new String[list.size()];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }

        Arrays.sort(answer);

        return answer;
    }
}