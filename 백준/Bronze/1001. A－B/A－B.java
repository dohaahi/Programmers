import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String aa = sc.next();
        String bb = sc.next();
        int a = Integer.parseInt(aa);
        int b = Integer.parseInt(bb);
        System.out.println(a - b);
    }
}