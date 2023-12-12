import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {
        int[] answer = new int[emergency.length];

        int[] sortedArray = Arrays.stream(emergency)
                .sorted()
                .toArray();

        for (int i = 0; i < emergency.length; i++) {
            for (int j = 0; j < sortedArray.length; j++) {
                if (emergency[i] == sortedArray[j]) {
                    answer[i] = emergency.length - j;
                }
            }
        }

        return answer;
    }
}