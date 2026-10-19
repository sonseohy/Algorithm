/*
 * 문제: 가장 큰 물고기 10마리 구하기
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298517
 * DB: MySQL
 *
 * [문제 요약]
 * FISH_INFO 테이블에서 가장 큰 물고기 10마리의 ID와 길이(LENGTH)를 조회한다.
 * 길이 기준 내림차순으로 정렬해서 출력한다.
 *
 * [핵심 포인트]
 * 1. ORDER BY의 기본 정렬은 ASC(오름차순)이다.
 *    -> "가장 큰" 걸 찾으려면 반드시 DESC를 명시해야 한다.
 * 2. LIMIT은 실행 순서상 맨 마지막이다. (FROM -> SELECT -> ORDER BY -> LIMIT)
 *    -> 정렬이 끝난 뒤 위에서 N개를 자르므로, 정렬 방향이 틀리면 "가장 작은 10마리"가 나온다.
 * 3. 동점 처리를 위해 2순위 정렬(ID ASC)을 추가해 결과를 항상 같은 순서로 고정한다.
 * 4. MySQL은 DESC 정렬 시 NULL을 맨 뒤로 보내므로, LENGTH가 NULL인 행은 상위 10개에 들어오지 않는다.
 *    (Oracle은 DESC 시 NULL이 맨 앞이라 NULLS LAST가 필요함. DB마다 다르니 주의)
 */

SELECT ID, LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID ASC -- 1순위: 길이 큰 순 / 2순위: 길이가 같으면 ID 작은 순
LIMIT 10;                   -- 정렬된 결과에서 상위 10개만 가져옴