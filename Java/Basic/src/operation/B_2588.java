package operation;

import java.util.Scanner;

// 곱셈
// 세자리수 곱셈 과정의 수 들과 결과를 출력하시오.
public class B_2588 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        int ones = num2 % 10;
        int tens = ((num2 - ones) % 100) / 10;
        int hundreds = num2 / 100;

        System.out.println(num1 * ones);
        System.out.println(num1 * tens);
        System.out.println(num1 * hundreds);

        int result = (num1 * ones) + (num1 * tens * 10) + (num1 * hundreds * 100);
        System.out.println(result);

        sc.close();
    }
}
