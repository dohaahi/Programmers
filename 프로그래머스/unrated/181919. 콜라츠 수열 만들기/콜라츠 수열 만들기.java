import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> arr = new ArrayList<>();

        // 초기값 삽입
        arr.add(n);

        // n이 1이 될 때까지 반복
        while (n != 1) {
            // 짝수일 때
            if (n % 2 == 0) {
                n /= 2;
                arr.add(n);
                continue;
            }

            n = 3 * n + 1;
            arr.add(n);
        }

        int[] answer = new int[arr.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = arr.get(i);
        }

        return answer;
    }
}