class Solution {
    public String solution(String my_string, int[] index_list) {
        String answer = "";
        String[] arr = my_string.split("");

        for (int i : index_list) {
            answer += arr[i];
        }
        return answer;
    }
}