/*
 * 문제: 한 해에 잡은 물고기 수 구하기
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298516
 * DB: MySQL
 *
 * [문제 요약]
 * FISH_INFO 테이블에서 2021년도에 잡은 물고기 수를 구한다.
 * 컬럼명은 FISH_COUNT로 지정한다.
 *
 * [테이블 구조]
 * FISH_INFO (ID INTEGER, FISH_TYPE INTEGER, LENGTH FLOAT NULL허용, TIME DATE)
 * 단, 잡은 물고기의 길이가 10cm 이하이면 LENGTH가 NULL이다.
 *
 * [핵심 포인트]
 * 1. TIME 컬럼이 DATE 타입이므로 YEAR() 함수로 연도만 숫자로 꺼낼 수 있다.
 * 2. 행을 거르는 건 WHERE의 역할이다. (그룹화 전에 행 단위로 필터링)
 * 3. GROUP BY는 필요 없다. 2021년 전체를 하나의 숫자로 세는 문제이기 때문이다.
 * 4. 실행 순서: FROM -> WHERE -> SELECT
 *    -> 먼저 2021년 행만 남기고, 그 다음 개수를 센다.
 *
 * [주의: COUNT(LENGTH)를 쓰면 안 되는 이유]
 * - COUNT(컬럼)은 해당 컬럼이 NULL인 행을 세지 않는다.
 * - 이 문제는 10cm 이하 물고기의 LENGTH가 NULL이라, COUNT(LENGTH)를 쓰면
 *   작은 물고기가 전부 빠지고 틀린 답이 나온다.
 * - 예시 데이터에서 2021년 물고기는 ID 0(LENGTH 13.37), ID 5(LENGTH NULL) 2마리다.
 *   COUNT(LENGTH)는 ID 5가 빠져 1이 나오고, COUNT(*)는 정답인 2가 나온다.
 * - 정리: "행이 몇 개인지" 셀 때는 COUNT(*), "값이 있는 것만" 셀 때는 COUNT(컬럼)
 *
 * [주의: WHERE에는 집계함수를 못 쓰고, SELECT 별칭도 못 쓴다]
 * - WHERE는 SELECT보다 먼저 실행되므로 FISH_COUNT 같은 별칭을 WHERE에서 쓸 수 없다.
 */

-- [풀이 1] YEAR() 함수 사용 (가장 직관적, 코테에서 많이 사용)
SELECT COUNT(*) AS FISH_COUNT   -- NULL 여부와 상관없이 전체 행 수를 센다
FROM FISH_INFO                  -- 물고기 정보 테이블
WHERE YEAR(TIME) = 2021;        -- TIME에서 연도만 뽑아 2021인 행만 남긴다


/*
 * [풀이 2] 범위 비교 (BETWEEN)
 * 결과는 풀이 1과 같다.
 * 컬럼을 가공하지 않고 그대로 비교하기 때문에, TIME에 인덱스가 있으면 DB가 그 인덱스로 2021년 구간을 바로 찾을 수 있다.
 * (YEAR(TIME)처럼 컬럼에 함수를 씌우면 인덱스를 쓰지 못하고 전체 행을 읽는 경우가 많다. 실무에서 중요)
 * TIME이 DATE 타입이라 '2021-12-31'까지 포함해도 안전하다.
 * (DATETIME 타입이었다면 12월 31일 낮 시간대가 빠질 수 있어 주의)
 */

SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE TIME BETWEEN '2021-01-01' AND '2021-12-31';


/*
 * [풀이 3] DATE_FORMAT 사용
 * 연도를 문자열로 뽑아 비교한다. 결과는 같다.
 * 문자열 비교라서 '2021'처럼 따옴표를 붙여야 한다. (YEAR()는 숫자 비교)
 *
 * SELECT COUNT(*) AS FISH_COUNT
 * FROM FISH_INFO
 * WHERE DATE_FORMAT(TIME, '%Y') = '2021';
 */

/*
 * [자주 하는 실수]
 * - COUNT(LENGTH) 사용: 위에 설명한 NULL 함정.
 * - 컬럼명 누락: 문제에서 FISH_COUNT로 지정했으므로 AS FISH_COUNT를 꼭 붙인다.
 * - TIME은 MySQL 키워드이지만 예약어는 아니라서, 컬럼명으로 그대로 써도 에러가 나지 않는다.
 *   (예약어인 SELECT, ORDER 등을 컬럼명으로 쓸 때만 백틱으로 감싸야 한다)
 */