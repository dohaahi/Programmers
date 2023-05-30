import java.util.ArrayList;

class Solution {
    public String[] solution(String my_string) {
        ArrayList<String> list = new ArrayList<>();

        // 1. 문자열만 뽑기
        String[] arr = my_string.split(" ");
        for (String s : arr) {
            if (!s.equals("")) {
                list.add(s);
            }
        }

        // 2. ArrayList -> static array
        String[] answer = new String[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}