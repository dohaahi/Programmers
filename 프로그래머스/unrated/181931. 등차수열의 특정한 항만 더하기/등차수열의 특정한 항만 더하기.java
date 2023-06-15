import java.util.ArrayList;

class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int num = a;

        ArrayList<Integer> list = new ArrayList<>();
        list.add(a);

        for (int i = 1; i < included.length; i++) {
            num += d;
            list.add(num);
        }

        for (int i = 0; i < list.size(); i++) {
            if (included[i]) {
                answer += list.get(i);
            }
        }
        return answer;
    }
}