class Solution {
    public String solution(String cipher, int code) {
        String[] answer = cipher.split("");
        String result = "";
        for (int i = code-1; i < answer.length; i += code) {
            result +=answer[i];
        }
        
        return result;
    }
}