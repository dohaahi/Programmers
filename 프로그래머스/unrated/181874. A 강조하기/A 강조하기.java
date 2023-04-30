class Solution {
    public String solution(String myString) {
        String answer = "";
        String[] arr = myString.split("");

        for (String s : arr) {
            if (s.equals("a") || s.equals("A")) {
                answer += "A";
            } else {
                answer += s.toLowerCase();
            }
        }
        return answer;
    }
}