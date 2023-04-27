class Solution {
    public int solution(int[] num_list) {
        int mul = 1;
        int sum = 0;
        for(int num : num_list) {
            mul *= num;
            sum += num;
        }
        sum *= sum;
        if(mul<= sum) {
            return 1;
        }
        return 0;
    }
}