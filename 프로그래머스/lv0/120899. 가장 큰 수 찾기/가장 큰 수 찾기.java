import java.util.Arrays;

class Solution {
    public int[] solution(int[] array) {
        int[] answer = new int[2];
        int[] du_arr = array.clone();

                Arrays.sort(array);

        answer[0] = array[array.length - 1];

        for (int i = 0; i < array.length; i++) {
            if (du_arr[i] == answer[0]) {
                answer[1] = i;
            }
        }

        return answer;
    }
}