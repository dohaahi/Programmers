import java.util.Arrays;

class Solution {
    public String[] solution(String my_string) {
       String[] answer = new String[my_string.length()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = "";
        }

        String[] arr = my_string.split("");

        for (int i = 0; i < answer.length; i++) {
            for (int j = i; j < answer.length; j++) {
                answer[i] += arr[j];
            }
        }

        Arrays.sort(answer);

        return answer;
    }
}