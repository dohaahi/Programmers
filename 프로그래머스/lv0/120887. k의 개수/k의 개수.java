class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;

        for (int l = i; l <= j; l++) {
            String[] arr = Integer.toString(l).split("");
            for (String s : arr) {
                if (s.contains(Integer.toString(k))) {
                    answer++;
                }
            }

        }
        return answer;
    }
}