class Solution {
    public int solution(String num_str) {
        int answer = 0;
        String[] arr = num_str.split("");
        for(String num : arr) {
            answer += (int) Integer.parseInt(num);
        }
        return answer;
    }
}