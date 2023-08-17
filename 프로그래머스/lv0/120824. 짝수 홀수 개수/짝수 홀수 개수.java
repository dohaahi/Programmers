import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];

        int even = Long.valueOf(Arrays.stream(num_list).filter(i -> i % 2 == 0).count()).intValue();
        answer[0] = even;
        answer[1] = num_list.length - even;

        return answer;
    }
}