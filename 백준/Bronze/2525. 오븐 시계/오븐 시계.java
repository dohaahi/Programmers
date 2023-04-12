import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        // 분으로 변환
        int time = (a * 60 + b + c) % (60 * 24);

        System.out.println(time/60  + " " + time%60);
    }}