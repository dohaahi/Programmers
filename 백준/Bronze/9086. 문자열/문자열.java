import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < num; i++) {
            String str = sc.nextLine();
            String[] arr = str.split("");
            System.out.println(arr[0] + arr[arr.length - 1]);
        }
    }
}