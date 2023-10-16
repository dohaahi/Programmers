import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
       List<Integer> integerList = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            for (int d : delete_list) {
                if (arr[i] == d) {
                    arr[i] = 0;
                    break;
                }
            }
        }

        for (int i : arr) {
            if (i != 0) {
                integerList.add(i);
            }
        }

        int[] answer = new int[integerList.size()];
        for (int i = 0; i < integerList.size(); i++) {
            answer[i] = integerList.get(i);
        }


        return answer;
    }
}