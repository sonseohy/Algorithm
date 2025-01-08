package operation;

import java.util.Scanner;

// A - B
// 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.
public class B_1001 {
    public static void main(String[] main) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(a - b);
    }
}
