class Solution {
    public int solution(int a, int b) {
        int plus = Integer.valueOf(Integer.toString(a) + b);

        return plus > 2 * a * b ? plus : 2 * a * b;
    }
}