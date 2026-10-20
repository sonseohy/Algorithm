/*
 * 문제: 최대 물고기의 길이 구하기
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298515
 * DB: MySQL
 *
 * [문제 요약]
 * FISH_INFO 테이블에서 가장 큰 물고기의 길이를 구하고,
 * 소수점 둘째 자리까지 맞춘 뒤 뒤에 'cm'를 붙여 MAX_LENGTH 컬럼으로 출력한다. (예: 50.00cm)
 *
 * [핵심 포인트]
 * 1. FORMAT(숫자, 2)
 *    -> 숫자를 소수점 둘째 자리까지 맞춘 "문자열"로 바꾼다. (50 -> '50.00')
 *    -> ROUND(숫자, 2)는 컬럼이 FLOAT이면 50으로만 나올 수 있어 .00이 보장되지 않는다.
 *    -> 1000 이상이면 천 단위 쉼표가 붙지만(1,000.00) 물고기 길이에는 해당되지 않는다.
 * 2. CONCAT(a, b, ...)
 *    -> 여러 값을 이어 붙여 하나의 문자열로 만든다. (CONCAT('50.00', 'cm') -> '50.00cm')
 *    -> 숫자는 자동으로 문자열로 변환되어 연결된다.
 *    -> 인자 중 하나라도 NULL이면 결과 전체가 NULL이 된다.
 */

SELECT CONCAT(FORMAT(MAX(LENGTH), 2), 'cm') AS MAX_LENGTH
FROM FISH_INFO;