class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String[] array = my_string.split("");
        for(String str : array) {
            for(int i=0; i<n;i++) {
                answer += str;
            }
        }
        return answer;
    }
}