package If;

import java.util.Scanner;

// 주사위 세개
// 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
// 1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
// 2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
// 3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
// 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
public class B_2480 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();

        int money;

        if (n1 == n2 && n2 == n3) {
            money = 10000 + n1 * 1000;
        } else if (n1 == n2 || n2 == n3) {
            money = 1000 + n2 * 100;
        } else if (n1 == n3) {
            money = 1000 + n1 * 100;
        } else {
            if (n1 > n2 && n1 > n3) {
                money = n1 * 100;
            } else if (n1 < n2 && n2 > n3) {
                money = n2 * 100;
            } else {
                money = n3 * 100;
            }
        }

        System.out.println(money);
        sc.close();
    }
}
