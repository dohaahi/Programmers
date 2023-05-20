import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. 입력 받은 수 공백을 기준으로 저장
        String[] num1 = sc.next().split("");
        String[] num2 = sc.next().split("");

        // 2. 배열의 원소를 for문으로 돌면서 숫자 뒤집기
        String newNum1 = "";
        String newNum2 = "";

        for (int i = 2; i >= 0; i--) {
            newNum1 += num1[i];
        }

        for (int i = 2; i >= 0; i--) {
            newNum2 += num2[i];
        }

        // 3.
        System.out.println(Integer.max(Integer.parseInt(newNum1), Integer.parseInt(newNum2)));
    }
}