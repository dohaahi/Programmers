class Solution {
    public int solution(String binomial) {
        String[] str = binomial.split(" ");
        if (str[1].equals("+")) {
            return Integer.parseInt(str[0]) + Integer.valueOf(str[2]);
        } else if (str[1].equals("-")) {
            return Integer.parseInt(str[0]) - Integer.valueOf(str[2]);
        }
        return Integer.parseInt(str[0]) * Integer.valueOf(str[2]);
    }
}