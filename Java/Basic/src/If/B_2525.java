package If;

import java.util.Scanner;

// 오븐 시계
// 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
public class B_2525 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int h, m;

        if (b + (c % 60) >= 60) {
            h = a + (c / 60) + 1;
            m = b + (c % 60) - 60;
        } else {
            h = a + (c / 60);
            m = b + (c % 60);
        }

        System.out.printf("%d %d", h % 24, m);
        sc.close();
    }
}
