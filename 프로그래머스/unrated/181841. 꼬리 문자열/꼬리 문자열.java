class Solution {
    public String solution(String[] str_list, String ex) {
        for (int i = 0; i < str_list.length; i++) {
            if (str_list[i].contains(ex)) {
                str_list[i] = "";
            }
        }

        return String.join("", str_list);
    }
}