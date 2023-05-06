import java.util.ArrayList;


class Solution {
    public int solution(int[] num_list) {
        // 1. 동적 배열 만들기
        ArrayList<String> evenList = new ArrayList<>();
        ArrayList<String> oddList = new ArrayList<>();

        // 2. 짝수, 홀수를 만들 문자열 만들기
        String even = "";
        String odd = "";

        // 3. for 문을 돌면서 짝수이면 even, 홀수이면 odd 배열에 값 추가
        for (int i : num_list) {
            if (i % 2 == 0) {
                evenList.add(Integer.toString(i));
            } else {
                oddList.add(Integer.toString(i));
            }
        }

        // 4. 배열을 돌면서 String으로 만들기
        for (String s : evenList) {
            even += s;
        }
        for (String s : oddList) {
            odd += s;
        }

        // 5. String 타입 -> int 타입으로 변경 후 두 값 더하기
        return Integer.valueOf(even) + Integer.valueOf(odd);
    }
}