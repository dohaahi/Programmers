class Solution {
    public String solution(int age) {
        // 1. age를 배열로 만들기
        String[] arr = (Integer.toString(age)).split("");

        String answer = "";

        // 2. 소문자 a의 char에 age만큼 더한 문자열 출력
        for (String s : arr) {
            answer += Character.toString(97 + Integer.valueOf(s));
        }

        return answer;
    }
}