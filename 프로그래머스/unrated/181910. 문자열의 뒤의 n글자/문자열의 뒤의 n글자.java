class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        String[] array = my_string.split("");
        for(int i=array.length -n; i<array.length;i++) {
            answer += array[i];
        }
        return answer;
    }
}