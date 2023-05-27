class Solution {
    public int[] solution(int[] num_list, int n) {
        String arr = "";

        for (int i = 0; i < num_list.length; i += n ) {
            arr += Integer.toString(num_list[i]);
        }

        String[] str_arr = arr.split("");
        int[] answer = new int[str_arr.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = Integer.valueOf(str_arr[i]);
        }

        return answer;
    }
}