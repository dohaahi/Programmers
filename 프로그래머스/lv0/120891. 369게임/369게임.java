class Solution {
    public int solution(int order) {
        String[] arr = Integer.toString(order).split("");
        int answer = 0;

        for (String s : arr) {
            if (Integer.valueOf(s) != 0 &&Integer.valueOf(s) % 3 == 0) {
                answer++;
            }
        }

        return answer;
    }
}