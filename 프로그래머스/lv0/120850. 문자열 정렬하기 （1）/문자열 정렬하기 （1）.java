import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        String str = "";

        // 1. 숫자만 뽑기
        char[] arr = my_string.toCharArray();
        for (char c : arr) {
            if (c < 'A') {
                str += c;
            }
        }

        // 2. string -> 숫자 배열
        int[] answer = new int[str.length()];
        String[] s_num = str.split("");
        for (int i = 0; i < answer.length; i++) {
            answer[i] = Integer.valueOf(s_num[i]);
        }

        Arrays.sort(answer);

        return answer;
    }
}