class Solution {
    public int solution(String myString, String pat) {
        String result = "";

        String[] arr = myString.split("");
        for (String s : arr) {
            if (s.equals("A")) {
                result += "B";
            } else {
                result += "A";
            }
        }

        if (result.contains(pat)) {
            return 1;
        }
        return 0;
    }
}