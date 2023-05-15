class Solution {
    public String solution(String n_str) {
       String[] arr = n_str.split("");
        String answer = "";
        int index = 0;

        // 1. for 문을 돌며 0이 아닌 수의 index를 반환
        for (int i = 0; i < n_str.length(); i++) {
            if (Integer.valueOf(arr[i]) != 0) {
                index = i;
                break;
            }
        }

        // 2. 반환 받은 index 이후의 수를 answer에 추가
        for (int i = index; i < n_str.length(); i++) {
            answer += arr[i];
        }

        return answer;
    }
}