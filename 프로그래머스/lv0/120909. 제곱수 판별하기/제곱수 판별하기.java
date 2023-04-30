class Solution {
    public int solution(int n) {
       if ( (int)Math.pow((double)n, 0.5) == Math.sqrt(n)) {
            return 1;
        }
        return 2;
    }
}