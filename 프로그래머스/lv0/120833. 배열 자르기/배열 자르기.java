class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        // 1. num2 - num1 + 1 의 길이를 갖는 새로운 배열을 만들기
        int[] answer = new int [num2 - num1 + 1];

        // 2. 해당 index의 값을 새로운 배열에 넣기
        for(int i=0; i<answer.length; i++) {
            answer[i] = numbers[i + num1];
        }

        return answer;
    }
}