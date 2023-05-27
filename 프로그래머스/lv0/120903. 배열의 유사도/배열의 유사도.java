class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;

        for (String s : s1) {
            for (String k : s2) {
                if (s.equals(k)) {
                    answer++;
                }
            }
        }
        return answer;
    }
}