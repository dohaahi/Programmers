import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String count = sc.next();
        String value = sc.next();

        int answer = 0;
        String[] arr = value.split("");
        for (String s : arr) {
            answer += Integer.valueOf(s);

        }
        System.out.println(answer);
    }
}