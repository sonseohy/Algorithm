package For;

import java.util.Scanner;

// 구구단
// N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.
// 출력형식과 같게 N*1부터 N*9까지 출력한다. ex) 2 * 1 = 2 ...
public class B_2739 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i = 1; i < 10; i++) {
            System.out.printf("%d * %d = %d\n", n, i, n * i);
        }
    }
}
