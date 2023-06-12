class Solution {
    public String solution(String letter) {
        String answer = "";

        String[] str = letter.split(" ");
        String[] morse = {".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};


        for (int i = 0; i < str.length; i++) {
            for (int j = 0; j < morse.length; j++) {
                if (str[i].equals(morse[j])) {
                    answer += Character.toString('a' + j);
                    break;
                }

            }
        }

        return answer;
    }
}