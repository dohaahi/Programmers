class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] arr = my_string.split("");
        for (String s : arr) {
            if (s.toUpperCase() == s) {
                answer += s.toLowerCase();
            } else {
                answer += s.toUpperCase();
            }
        }
        return answer;
    }
}