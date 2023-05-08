class Solution {
    public int solution(String my_string, String is_suffix) {
        String new_string = "";
        String[] arr = my_string.split("");
        
        // is_suffix 의 길이가 my_string 보다 길다면 0을 리턴 
        if (my_string.length() < is_suffix.length()) {
            return 0;
        }

        // is_suffix 길이만큼 my_string을 끝에서 부터 자름
        for (int i = is_suffix.length(); i > 0; i--) {
            new_string += arr[my_string.length() - i];
        }

        return new_string.equals(is_suffix) ? 1 : 0;
    }
}