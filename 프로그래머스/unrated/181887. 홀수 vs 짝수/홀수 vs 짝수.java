class Solution {
    public int solution(int[] num_list) {
       int odd = 0;
        int sum = 0;

        // 1. 홀수 값들의 합 구하기
        for (int i = 0; i < num_list.length; i += 2) {
            odd += num_list[i];
        }

        // 2. 전체 합 - 홀수 합 = 짝수 합
        for (int i : num_list) {
            sum += i;
        }

        // 3. 1과 2를 비교하여 결과 출력
        return sum - odd <= odd ? odd : sum - odd;
    }
}