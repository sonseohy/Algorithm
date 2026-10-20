/*
 * 문제: 잡은 물고기의 평균 길이 구하기
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/293259
 * DB: MySQL
 *
 * [문제 요약]
 * FISH_INFO 테이블에서 잡은 물고기의 평균 길이를 구해 AVERAGE_LENGTH 컬럼으로 출력한다.
 * 10cm 이하의 물고기는 LENGTH가 NULL이며, 이를 10cm로 취급해서 평균을 구한다.
 * 평균은 소수점 셋째 자리에서 반올림한다. (예: 26.666.. -> 26.67)
 *
 * [핵심 포인트]
 * 1. AVG는 NULL 행을 무시한다.
 *    -> 그냥 AVG(LENGTH)를 쓰면 10cm 이하 물고기가 평균에서 빠져 값이 실제보다 커진다.
 *    -> 예시 기준: 올바른 값 (30+50+40+20+10+10)/6 = 26.67, NULL 무시 시 (30+50+40+20)/4 = 35
 * 2. IFNULL(값, 대체값)
 *    -> 값이 NULL이면 대체값으로 바꾸고, NULL이 아니면 원래 값을 그대로 반환한다.
 *    -> IFNULL(LENGTH, 10)으로 NULL을 10으로 바꾼 뒤 AVG를 계산한다.
 *    -> COALESCE(LENGTH, 10)도 같은 결과이며, 표준 SQL이라 다른 DBMS에서도 쓸 수 있다.
 *    -> IS NULL은 NULL 여부를 판별하는 조건(WHERE용), ISNULL()은 0/1을 반환하는 함수라서 대체 용도로는 쓰지 않는다.
 * 3. "소수점 셋째 자리에서 반올림"은 둘째 자리까지 남긴다는 뜻이다.
 *    -> ROUND(값, 2)가 맞다. ROUND(값, 3)은 셋째 자리까지 남기므로 틀린다.
 */

SELECT ROUND(AVG(IFNULL(LENGTH, 10)), 2) AS AVERAGE_LENGTH
FROM FISH_INFO;