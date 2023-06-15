import java.util.Arrays;

class Solution {
    public int solution(String before, String after) {
        int count = 0;

        char[] str1 = before.toCharArray();
        char[] str2 = after.toCharArray();

        Arrays.sort(str1);
        Arrays.sort(str2);

        for (int i = 0; i < str1.length; i++) {
            if (str1[i] == str2[i]) {
                count++;
            }
        }
        
        return count>=before.length() ? 1 : 0;
    }
}