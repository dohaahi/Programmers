class Solution {
    public String solution(String rny_string) {
        String new_string = rny_string.replace("m", "rn");
        if(rny_string.length() == new_string.length()) {
            return rny_string;
        }
        return new_string;
    }
}