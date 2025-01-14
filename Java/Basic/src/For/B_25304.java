package For;

import java.util.Scanner;

// 영수증
// 영수증에 적힌 구매한 각 물건의 가격과 개수, 구매한 물건들의 총 금액을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
// 첫째 줄에는 영수증에 적힌 총 금액 X가 주어지고, 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
// 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
public class B_25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int n = sc.nextInt();

        int sum = 0;

        for (int i = 0;i < n;i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            sum += a * b;
        }

        if (sum == x) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        sc.close();
    }
}
