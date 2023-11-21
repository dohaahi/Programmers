import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public String solution(String my_string, int[] indices) {
       List<String> stringList = Arrays.stream(my_string.split(""))
                .collect(Collectors.toList());

        Arrays.stream(indices)
                .forEach(i -> {
                    stringList.set(i, "");
                });

        return String.join("", stringList);
    }
}