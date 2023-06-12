import java.util.ArrayList;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
       ArrayList<Integer> num_list = new ArrayList<>();

        // 1. intStrs 순회
        for (String intStr : intStrs) {
            String[] list = intStr.split("");
            String str = "";

            // 2. 배열에서 s부터 l에 해당하는 숫자 반환
            for (int i = s; i < s + l; i++) {
                str += list[i];
            }

            // 3. k와 반환한 숫자 비교
            if (Integer.parseInt(str) > k) {
                num_list.add(Integer.valueOf(str));
            }
        }

        int[] result = new int[num_list.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = num_list.get(i);
        }

        return result;
    }
}