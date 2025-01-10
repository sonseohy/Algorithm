package If;

import java.util.Scanner;

// 알람 시계
// "45분 일찍 알람 설정하기"
// 현재 상근이가 설정한 알람 시각이 주어졌을 때, 알람을 45분 앞서는 시간으로 바꾸려면 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
public class B_2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int m = sc.nextInt();

        if (m < 45) {
            if (h == 0) {
                System.out.printf("%d %d", 23, 60 - (45 - m));
            } else {
                System.out.printf("%d %d", h - 1, 60 - (45 - m));
            }
        } else if (m == 45) {
            System.out.printf("%d %d", h, 0);
        } else {
            System.out.printf("%d %d", h, m - 45);
        }

        sc.close();
    }
}

// 오답 : 23시 45분일 경우