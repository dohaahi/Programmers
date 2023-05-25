class Solution {
    public String solution(String myString) {
        String answer = "";

        char[] arr = myString.toCharArray();

        for (char c : arr) {
            if (c < 'l') {
                c = 'l';
            }
            answer += Character.toString(c);
        }

        return answer;
    }
}