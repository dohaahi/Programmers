import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String answer = "";

        String[] arr = my_string.split("");
        for (int i = 0; i < arr.length; i++) {
            // 대문자 -> 소문자
            if (arr[i].charAt(0) < 'a') {
                arr[i] = arr[i].toLowerCase();
            }
        }

        Arrays.sort(arr);
        for (String s : arr) {
            answer += s;
        }
        return answer;
    }
}