import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        String answer = "";

        for (int i = 0; i < num; i++) {
            String[] str = sc.nextLine().split(" ");

            String[] arr = str[1].split("");

            for (int k = 0; k < arr.length; k++) {
                answer += arr[k].repeat(Integer.valueOf(str[0]));
            }
            System.out.println(answer);
            answer = "";
        }

    }
}