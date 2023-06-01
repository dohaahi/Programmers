class Solution {
    public int[] solution(String myString) {
         String[] str = myString.split("x");
        String[] arr = myString.split("");

        // 마지막 문자가 x일 경우
        if (arr[arr.length - 1].equals("x")) {
            int[] answer = new int[str.length + 1];

            for (int i = 0; i < answer.length - 1; i++) {
                answer[i] = str[i].length();
            }

            answer[answer.length - 1] = 0;
            return answer;
        }

        int[] answer = new int[str.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = str[i].length();
        }
        return answer;
    }
}