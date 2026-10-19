# SQL 코딩테스트 (MySQL 기준)

---

## 0. 핵심 한 줄 요약

| 키워드     | 핵심 한 줄                                                                  |
| ---------- | --------------------------------------------------------------------------- |
| `GROUP BY` | 같은 값끼리 행을 묶어서 그룹별로 집계(COUNT, SUM, AVG 등)할 수 있게 만든다. |
| `HAVING`   | 그룹화된 결과(집계 결과)에 조건을 걸어 원하는 그룹만 남긴다.                |
| `WHERE`    | 그룹화하기 전, 개별 행 단위로 조건을 걸어 거른다.                           |

**WHERE vs HAVING**

- `WHERE` → 그룹화 **전** 행 필터 → 집계함수 사용 불가
- `HAVING` → 그룹화 **후** 그룹 필터 → 집계함수 사용 가능

---

## 1. 실행 순서

```
작성: SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
실행: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

- `WHERE`는 `SELECT`보다 먼저 실행되므로 SELECT 별칭을 쓸 수 없다.
- MySQL에서 `HAVING`, `ORDER BY`는 SELECT 별칭 사용 가능.

---

## 2. GROUP BY + HAVING

```sql
SELECT FISH_TYPE, COUNT(*) AS CNT, AVG(LENGTH) AS AVG_LEN
FROM FISH_INFO
WHERE LENGTH IS NOT NULL      -- 행 단위 필터
GROUP BY FISH_TYPE
HAVING COUNT(*) >= 10         -- 그룹 단위 필터
ORDER BY CNT DESC;
```

**규칙:** `GROUP BY`를 쓰면 SELECT에는 ① 그룹 기준 컬럼 ② 집계함수만 올 수 있다.

---

## 3. 집계함수와 NULL

| 함수                    | NULL 처리            |
| ----------------------- | -------------------- |
| `COUNT(*)`              | NULL 포함 전체 행 수 |
| `COUNT(컬럼)`           | NULL 제외하고 셈     |
| `COUNT(DISTINCT 컬럼)`  | 중복·NULL 제외       |
| `SUM / AVG / MAX / MIN` | NULL 무시            |

> `AVG`가 NULL을 무시한다는 점이 문제 조건과 엮여 자주 함정이 된다.

---

## 4. NULL 다루기

```sql
WHERE LENGTH IS NULL          -- '= NULL'은 안 됨
WHERE LENGTH IS NOT NULL
IFNULL(LENGTH, 10)            -- NULL이면 10으로 대체 (MySQL)
COALESCE(A, B, 0)             -- 첫 번째 non-NULL 반환
```

---

## 5. 조건 분기: CASE WHEN

```sql
SELECT ID,
  CASE WHEN LENGTH <= 10 THEN 'LOW'
       WHEN LENGTH <= 20 THEN 'MID'
       ELSE 'HIGH' END AS GRADE
FROM FISH_INFO;
```

조건부 집계:

```sql
SUM(CASE WHEN LENGTH > 10 THEN 1 ELSE 0 END)
```

---

## 6. JOIN

```sql
-- INNER: 양쪽 다 있는 것만
FROM A JOIN B ON A.ID = B.ID

-- LEFT: A 전부 + 매칭되는 B (없으면 NULL)
FROM A LEFT JOIN B ON A.ID = B.ID
```

**"~가 없는 데이터 찾기" 패턴**

```sql
SELECT A.*
FROM A LEFT JOIN B ON A.ID = B.ID
WHERE B.ID IS NULL;
```

---

## 7. 서브쿼리

```sql
-- 평균보다 큰 것
SELECT * FROM FISH_INFO
WHERE LENGTH > (SELECT AVG(LENGTH) FROM FISH_INFO);

-- 존재 여부
WHERE ID IN (SELECT ID FROM OTHER_TABLE)
WHERE ID NOT IN (SELECT ID FROM OTHER_TABLE)
```

---

## 8. 날짜 함수 (MySQL)

```sql
YEAR(DATE)  MONTH(DATE)  DAY(DATE)
DATE_FORMAT(DATE, '%Y-%m-%d')    -- %Y 4자리연도, %y 2자리, %m 월, %d 일, %H 시
DATEDIFF(A, B)                   -- 일 수 차이
```

---

## 9. 문자열 함수

```sql
CONCAT(A, B)
SUBSTRING(S, 1, 3)
LENGTH(S)
UPPER(S)  LOWER(S)
TRIM(S)
REPLACE(S, 'a', 'b')

LIKE '%abc%'    -- % = 0글자 이상, _ = 정확히 1글자
```

---

## 10. 정렬과 제한

```sql
ORDER BY A DESC, B ASC    -- 다중 정렬
LIMIT 10                  -- 상위 10개
LIMIT 5, 10               -- 5개 건너뛰고 10개 (OFFSET)
```

---

## 11. 윈도우 함수 (MySQL 8.0+)

```sql
RANK()       OVER (PARTITION BY 그룹 ORDER BY 값 DESC)   -- 동점 같은 순위, 다음 순위 건너뜀
DENSE_RANK() OVER (...)                                  -- 동점 같은 순위, 건너뛰지 않음
ROW_NUMBER() OVER (...)                                  -- 동점이어도 고유 번호
```

그룹별 1등 찾기:

```sql
SELECT *
FROM (
  SELECT *, RANK() OVER (PARTITION BY FISH_TYPE ORDER BY LENGTH DESC) AS RK
  FROM FISH_INFO
) T
WHERE RK = 1;
```

---

## 12. 빈출 유형 & 풀이 패턴

| 유형                  | 핵심 패턴                                     |
| --------------------- | --------------------------------------------- |
| 가장 큰/작은 N개      | `ORDER BY 컬럼 DESC LIMIT N`                  |
| 최댓값/최솟값 행 찾기 | `WHERE 컬럼 = (SELECT MAX(컬럼) FROM 테이블)` |
| 그룹별 개수/합계      | `GROUP BY` + `COUNT/SUM`                      |
| N개 이상인 그룹만     | `GROUP BY` + `HAVING COUNT(*) >= N`           |
| 중복 제거             | `DISTINCT` 또는 `GROUP BY`                    |
| NULL 처리             | `IS NULL`, `IFNULL`, `COALESCE`               |
| 없는 데이터 찾기      | `LEFT JOIN ... WHERE B.ID IS NULL`            |
| 구간/등급 나누기      | `CASE WHEN`                                   |
| 월별/연도별 집계      | `GROUP BY MONTH(DATE)` 또는 `DATE_FORMAT`     |
| 그룹별 1등            | 윈도우 함수 `RANK() OVER (PARTITION BY ...)`  |
| 평균보다 큰/작은      | WHERE 절 서브쿼리                             |
| 문자열 포함 검색      | `LIKE '%키워드%'`                             |

---

## 13. 자주 하는 실수

- `WHERE`에 집계함수 쓰기 → `HAVING`으로 옮기기
- `= NULL` 비교 → `IS NULL` 사용
- `GROUP BY`에 없는 일반 컬럼을 SELECT에 쓰기
- `COUNT(*)`와 `COUNT(컬럼)` 혼동 (NULL 처리 차이)
- `NOT IN` 서브쿼리에 NULL이 섞여 결과가 비는 경우
- 동점 처리 기준(`ORDER BY` 2순위) 누락

---

## 14. 공부 순서 추천

1. `SELECT / WHERE / ORDER BY / LIMIT`
2. `GROUP BY / HAVING / 집계함수`
3. `IS NULL / IFNULL / CASE WHEN`
4. `JOIN`
5. 서브쿼리, 날짜·문자열 함수
6. 윈도우 함수
