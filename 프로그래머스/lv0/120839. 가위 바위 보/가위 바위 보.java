class Solution {
    public String solution(String rsp) {
        String[] answer = rsp.split("");
        String result = "";

        for (String s : answer) {
            switch (s) {
                case "5":
                    s = "2";
                    break;
                case "2" :
                    s = "0";
                    break;
                case "0" :
                    s = "5";
                    break;
            }
            result += s;
        }
        return result;
    }
}