class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for (int[] query : queries) {
            int first = query[0];
            int second = query[1];

            int a = arr[second];
            int b = arr[first];

            arr[first] = a;
            arr[second] = b;
        }

        return arr;
    }
}