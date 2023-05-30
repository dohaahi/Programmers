class Solution {
    public int solution(int a, int b, int c) {
        // 1. 세 숫자가 다 다른 경우
        if (a != b && b != c && c != a) {
            return a + b + c;
        }
        // 2. 세 숫자가 모든 같은 경우
        else if (a == b && a == c) {
            double f = Math.round((a + b + c) * (Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2)) * (Math.pow(a, 3) + Math.pow(b, 3) + Math.pow(c, 3)));
            return Integer.parseInt(String.valueOf(Math.round(f)));
        }
        // 3. 세 숫자 중 두개가 같은 경우
        double k = Math.round((a + b + c) * (Math.pow(a, 2) + Math.pow(b, 2) + Math.pow(c, 2)));

        return Integer.parseInt(String.valueOf(Math.round(k)));
    }
}