class Solution {
    public int solution(String my_string, String is_prefix) {
        String[] new_arr = my_string.split("");
        String new_str = "";

        if (my_string.length() < is_prefix.length()) {
            return 0;
        }

        // is_prefix 의 길이만큼 my_string을 자르기
        for (int i = 0; i < is_prefix.length(); i++) {
            new_str += new_arr[i];
        }

        return new_str.equals(is_prefix) ? 1 : 0;
    }
}