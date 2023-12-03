class Solution {
    public int solution(String myString, String pat) {
        String[] split = myString.split("");
        int answer = 0;

        for (int i = 0; i <= split.length - pat.length(); i++) {
            StringBuilder matchString = new StringBuilder();

            for (int j = i; j < pat.length() + i; j++) {
                matchString.append(split[j]);
            }

            if (matchString.toString().equals(pat)) {
                answer++;
            }
        }

        return answer;
    }
}