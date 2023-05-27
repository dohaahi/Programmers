class Solution {
   public static String solution(String my_string) {
        String[] vowel = {"a", "e", "i", "o", "u"};
        String answer = "";

        for (String s : my_string.split("")) {
            if (s.contains("a") || s.contains("e") || s.contains("i") || s.contains("o") || s.contains("u")) {
                continue;
            }
            answer += s;
        }

        return answer;
    }
}