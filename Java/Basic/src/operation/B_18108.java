package operation;

import java.util.Scanner;

// 1998년생인 내가 태국에서는 2541년생?!
// 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.
public class B_18108 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int year = sc.nextInt();

        System.out.println(year - 543);
        sc.close();
    }
}
