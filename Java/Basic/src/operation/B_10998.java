package operation;

import java.util.Scanner;

// A x B
// 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
public class B_10998 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(a * b);
    }
}
