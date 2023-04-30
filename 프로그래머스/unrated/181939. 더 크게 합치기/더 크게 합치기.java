class Solution {
    public int solution(int a, int b) {
        double new_a = a * (Math.pow(10, Integer.toString(b).split("").length));
        double new_b = b * (Math.pow(10, Integer.toString(a).split("").length));

        if(new_a +b >= new_b+a) {
            return (int)new_a + b;
        }
        return (int) new_b + a;
    }
}