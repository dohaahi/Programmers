import java.util.Arrays;

class Solution {
    public int solution(int[] array, int height) {
        return  (int) Arrays.stream(array)
                .filter(p -> p > height).count();
    }
}