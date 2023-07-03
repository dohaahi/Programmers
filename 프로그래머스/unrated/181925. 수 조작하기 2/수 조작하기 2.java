class Solution {
    public String solution(int[] numLog) {
        String answer = "";

        for (int i = 0; i < numLog.length - 1; i++) {
            int a = numLog[i];
            int b = numLog[i + 1];

            if (Math.abs(a - b) == 1) {
                if (b > a) {
                    answer += "w";
                } else {
                    answer += "s";
                }
            } else {
                if (b > a) {
                    answer += "d";
                } else {
                    answer += "a";
                }
            }
        }
        return answer;
    }
}