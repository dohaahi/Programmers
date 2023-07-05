class Solution {
    public int solution(String s) {
        int answer = 0;

        String[] arr = s.split(" ");
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].charAt(0) == 'Z') {
                arr[i - 1] = "";
                arr[i] = "";
            }
        }

        for (String d : arr) {
            if (d == "") continue;
            answer += Integer.parseInt(d);
        }

        return answer;
    }
}