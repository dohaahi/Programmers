class Solution {
    public int solution(int a, int b) {
        if(a * b % 2 == 0) {
            if(a % 2 == 0 && b%2 ==0) {
                return Math.abs(a - b);
            } else {
                return 2*(a+b);
            }
        }
        return a * a + b * b;
    }
}