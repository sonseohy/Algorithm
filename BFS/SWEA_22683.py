# 나무 베기
# 앞으로 이동, 왼쪽으로 90도 회전, 오른쪽으로 90도 회전이 가능한 RC카가 있는데, 출발지에서 목적지까지 최소의 조작으로 이동시킬 수 있다.
# 나무에 가로 막혀 RC카를 목적지까지 이동시킬 수 없어 나무를 베기로 결심
#  N x N 크기의 필드 정보와 벨 수 있는 최대 나무의 수가 주어졌을 때, RC카를 목적지까지 이동시키기 위한 최소 조작 횟수를 구하라.
# G : RC카가 이동가능한 땅, T : RC카가 이동이 불가능한 나무, X : 현재 RC카의 위치, Y : RC카를 이동시키려는 위치
# 항상 위를 바라보는 상태로 RC카의 조작을 시작하며, 목적지까지 RC카를 이동시킬 수 없다면 -1을 출력
from collections import deque

def rc_car(i, j, cut):
    queue = deque()
    queue.append([i, j])
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1

    # 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    k = 0   # RC카의 방향

    while queue:
        ti, tj = queue.popleft()

        if ti == endi and tj == endj:
            return visited[ti][tj] - 1
        
        # 전진
        ni, nj = ti+di[k], tj+dj[k]
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if FIELD[ni][nj] == 'T' and cut > 0:
                cut -= 1
                FIELD[ni][nj] = 'G'
            queue.append([ni, nj])
            visited[ni][nj] = visited[ti][tj] + 1

        # 오른쪽 회전
        k = (k+1) % 4
        ni, nj = ti+di[k], tj+dj[k]

        # 왼쪽 회전
        k = (k-1) % 4

    return -1

def find(n, p):
    for row in range(n):
        for col in range(n):
            if FIELD[row][col] == p:
                return row, col

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    FIELD = [list(input()) for _ in range(N)]

    sti, stj = find(N, 'X')
    endi, endj = find(N, 'Y')

    print(rc_car(sti, stj, K, FIELD))

