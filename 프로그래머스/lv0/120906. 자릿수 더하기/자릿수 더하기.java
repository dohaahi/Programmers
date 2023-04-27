class Solution {
    public int solution(int n) {
        String[] array = Integer.toString(n).split("");
        int answer = 0;
        for(String num : array) {
            answer += Integer.valueOf(num);
        }
        return answer;
    }
}