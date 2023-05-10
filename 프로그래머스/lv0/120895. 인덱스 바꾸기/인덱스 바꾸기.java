class Solution {
    public String solution(String my_string, int num1, int num2) {
        // 1. 기존 스트링을 배열로 변환
        String[] arr = my_string.split("");

        // 2. 새로운 배열 만들어서 기존 배열 복사
        String[] answer = my_string.split("");

        // 3. 바꾸고 싶은 문자열 새로운 배열에 넣기
        answer[num1] = arr[num2];
        answer[num2] = arr[num1];

        return String.join("", answer);
    }
}