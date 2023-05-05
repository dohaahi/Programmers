class Solution {
    public int[] solution(int[] arr) {
        int len = 0;
        int sum = 0;

        for (int i : arr) {
            len += i;
        }

        int[] answer = new int[len];

        for (int i = 0; i < arr.length; i++) {
            if (i > 0) {
                sum += arr[i - 1];
            }

            for (int k = sum; k < sum + arr[i]; k++) {
                answer[k] = arr[i];
            }
        }

        return answer;
    }
}