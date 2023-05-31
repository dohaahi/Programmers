class Solution {
    public String[] solution(String[] strArr) {
        String answer = "";
        for (String s : strArr) {
            if (!s.contains("ad")) {
                answer += s + " ";
            }
        }

        String[] result = answer.split(" ");
        return result;
    }
}