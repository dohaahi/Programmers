import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        // 같은 눈 3개
        if(a == b  && b == c) {
            System.out.println(10000 + a*1000);
        // 모두 다른 눈
        } else if (a == b || a == c) {
            System.out.println(1000 + a * 100);
        } else if(b == c) {
            System.out.println(1000 + b * 100);
        } else {
            if(a > b && a > c) {
                System.out.println(a * 100);
            } else if(b > c && b > a) {
                System.out.println(b * 100);
            }else if (c > a && c > b){
                System.out.println(c * 100);
            }
        }

    }}