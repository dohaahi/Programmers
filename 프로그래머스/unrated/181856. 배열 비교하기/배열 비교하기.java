class Solution {
    public int solution(int[] arr1, int[] arr2) {
        // 1. 배열 길이가 다를 때
        if (arr1.length != arr2.length) {
            return arr1.length > arr2.length ? 1 : -1;
        }

        // 2. 배열 길이가 같을 때
        int sum1 = 0;
        int sum2 = 0;

        for (int i = 0; i < arr1.length; i++) {
            sum1 += arr1[i];
            sum2 += arr2[i];
        }

        if (sum1 == sum2) {
            return 0;
        }

        return sum1 > sum2 ? 1 : -1;
    }
}