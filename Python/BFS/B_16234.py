# 인구 이동
# N×N크기의 땅이 있고, 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
# 인접한 나라 사이에는 국경선이 존재하고, 오늘부터 인구 이동이 시작되는 날이다.
# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
# 1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 2. 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 4. 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 5. 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
from collections import deque

def move(i, j, check):
    dq = deque()
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    dq.append((i, j))
    union = False   # 연합 가능한 나라가 있는지 없는지 확인하는 변수

    while dq:
        ti, tj = dq.popleft()

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and L <= abs(population[ti][tj] - population[ni][nj]) <= R:
                dq.append((ni, nj))
                visited[ni][nj] = 1
                area[ni][nj] = check
                union = True
    if union:
        area[i][j] = check   # 연합이 가능한 나라가 있다면 bfs로 모두 찾은 후 마지막에 첫 지점 체크 (처음부터 체크하면 연합이 없는 경우에도 첫 지점이 체크됨)

def change(i, j):
    sum_v = 0
    idx = []
    cq = deque()
    cq.append((i, j))
    change_visited[i][j] = 1
    sum_v += population[i][j]
    idx.append((i, j))  # 헤맴 point : 첫 지점도 check인 지점을 메인에서 보내줬으므로 idx에 append 하고 시작해야함

    while cq:
        ti, tj = cq.popleft()

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = ti + di, tj + dj
            # 헤맴 point : L과 R 사이인지 한번 더 판단 (밑 주석 참고)
            if 0 <= ni < N and 0 <= nj < N and change_visited[ni][nj] == 0 and L <= abs(population[ti][tj] - population[ni][nj]) <= R:
                cq.append((ni, nj))
                change_visited[ni][nj] = 1
                idx.append((ni, nj))
                sum_v += population[ni][nj]

    for ci, cj in idx:
        population[ci][cj] = sum_v // len(idx)
    

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

area = [[0]*N for _ in range(N)]    # 국경선을 열 수 있어 연합이 가능한 나라 표시시
check = 1   # 하루별로 연합 가능한 나라를 구분하기 위해
result = 0

while True:
    for r in range(N):
        for c in range(N):
            if area[r][c] < check:
                move(r, c, check)   # 연합이 가능한 나라 찾기
    
    finish = False  # 인구 이동이 있었는지 확인하는 변수
    change_visited = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if change_visited[r][c] == 0 and area[r][c] == check:
                change(r, c)    # 연합 가능한 나라를 찾은 것을 기반으로 인구 이동동
                finish = True

    if finish:
        result += 1 # 인구 이동이 있었다면(finish == True) 인구 이동한 날 수 +1
        check += 1  # 다음 날의 연합 가능한 나라를 area에 표시하기 위해 area도 +1
    else:
        break   # 인구 이동이 없었다면 while문 끝냄

print(result)

# 헤맴 point : 38줄
# why? area에 붙어있는 지역이라고 해도 모든 칸이 연합 가능한 칸이 아닐 수 있음
# ex) 2 2 2 1
#     2 2 1 1
#     1 1 2 1
#     1 2 2 2
# 위 예제의 경우 위의 2 다섯칸이 모두 area로 연합 가능한 칸이지만 실제로 보면
# 30 66 66 50
# 30 66 50 50
# 50 50 62 50
# 50 62 62 62
# 위와 같이 1번, 5번 자리가 30으로 인구 이동이 가능하고, 2, 3, 6번 자리가 66으로 인구 이동이 가능한 경우이다.
# 따라서 area에서 연합 가능한 국가라고 와도 한번 더 인구 이동 bfs 할 때 L, R사이 값인지 검사해 계산해줘야 한다.
# 마지막 예제 참고 게시판 : https://www.acmicpc.net/board/view/50238

# 시간 줄일 수 있는 방법 있을듯? 아슬아슬하게 통과한 듯
