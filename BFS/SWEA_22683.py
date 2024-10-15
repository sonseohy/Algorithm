# 나무 베기 (이해 50%..?)
# 앞으로 이동, 왼쪽으로 90도 회전, 오른쪽으로 90도 회전이 가능한 RC카가 있는데, 출발지에서 목적지까지 최소의 조작으로 이동시킬 수 있다.
# 나무에 가로 막혀 RC카를 목적지까지 이동시킬 수 없어 나무를 베기로 결심
#  N x N 크기의 필드 정보와 벨 수 있는 최대 나무의 수가 주어졌을 때, RC카를 목적지까지 이동시키기 위한 최소 조작 횟수를 구하라.
# G : RC카가 이동가능한 땅, T : RC카가 이동이 불가능한 나무, X : 현재 RC카의 위치, Y : RC카를 이동시키려는 위치
# 항상 위를 바라보는 상태로 RC카의 조작을 시작하며, 목적지까지 RC카를 이동시킬 수 없다면 -1을 출력

from collections import deque

def rc_car(i, j, cut):
    queue = deque()
    queue.append([i, j, 0, cut, 0])     # 시작점 좌표 i, j, rc카 방향, 벨 수 있는 횟수, 총 조작 횟수
    # 필드와 같은 크기의 2차원 배열을 만든 후 각 칸에 방향별로 나무를 벨 수 있는 횟수 저장
    visited = [[[-1] * 4 for _ in range(N)] for _ in range(N)]  # 방문 여부와 나무를 벨 수 있는 횟수가 0일 때를 구분하기 위해 -1로 초기값 설정
    visited[i][j][0] = cut  # 처음 시작점의 칸(i, j)에 0번(방향 k가 위 일때) 인덱스 값을 벨 수 있는 횟수 cut으로 저장

    # 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    while queue:
        ti, tj, k, tc, cnt = queue.popleft()    # k : rc카 방향, tc : 나무 벨 수 있는 횟수, cnt : 조작횟수

        if FIELD[ti][tj] == 'Y':    # 도착지점 'Y'에 도착 했을때
            return cnt


        # 오른쪽 회전
        turn_r = (k + 1) % 4
        # visited에 저장된 벨 수 있는 횟수보다 현재 벨 수 있는 횟수 tc가 클때만 회전
        # why? 현재 벨 수 있는 홧수가 더 많다면 다른 최소경로를 더 찾을 수 있다는 의미 (나무를 더 벨 수 있으므로)
        # 이미 visited의 벨 수 있는 횟수가 더 크다면 이미 최소경로를 다 봤다는 의미
        if visited[ti][tj][turn_r] < tc:
            visited[ti][tj][turn_r] = tc
            queue.append([ti, tj, turn_r, tc, cnt + 1])     # 회전을 할 때도 조작횟수 cnt + 1

        # 왼쪽 회전
        turn_l = (k - 1) % 4
        # 마찬가지로 visited에 저장된 벨 수 있는 횟수보다 현재 벨 수 있는 횟수 tc가 클때만 회전
        if visited[ti][tj][turn_l] < tc:
            visited[ti][tj][turn_l] = tc
            queue.append([ti, tj, turn_l, tc, cnt + 1])

        # 전진
        ni, nj = ti + di[k], tj + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if FIELD[ni][nj] == 'T':    # 전진할 곳에 나무가 있다면
                if tc > 0 and (visited[ni][nj][k] < tc - 1):    # 나무를 벨 수 있고(tc>0), visited의 cut 횟수보다 나무가 있는 칸을 이동 후 벨 수 있는 횟수(tc - 1)가 클 때
                    # 나무를 베고 이동
                    tc -= 1
                    queue.append([ni, nj, k, tc, cnt + 1])
                    visited[ni][nj][k] = tc     # 해당 칸의 방향 인덱스에 가능한 cut횟수 저장
            else:   # 전진할 곳이 나무가 없을 때('G', 'Y')
                if visited[ni][nj][k] < tc:     # visited의 cut 횟수보다 벨 수 있는 횟수가 클 때
                    queue.append([ni, nj, k, tc, cnt + 1])
                    visited[ni][nj][k] = tc     # 해당 칸의 방향 인덱스에 가능한 cut횟수 저장

    return -1   # RC카가 도착지점까지 이동할 수 없는 경우

def find(n): # 시작지점 찾기
    for row in range(n):
        for col in range(n):
            if FIELD[row][col] == 'X':
                return row, col

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    FIELD = [list(input()) for _ in range(N)]

    sti, stj = find(N)

    print(f'#{test_case}', rc_car(sti, stj, K))


# # 시도1 : 뭔가 이상한 내 코드
# from collections import deque

# def rc_car(i, j, cut):
#     queue = deque()
#     queue.append([i, j, 0, cut, 0])
#     visited = [[[False]*4 for _ in range(N)] for _ in range(N)]
#     visited[i][j][0] = cut

#     # 상 우 하 좌
#     di = [-1, 0, 1, 0]
#     dj = [0, 1, 0, -1]

#     while queue:
#         ti, tj, k, tc, cnt = queue.popleft()

#         if FIELD[ti][tj] == 'Y':
#             return cnt

#         visited[ti][tj][k] = tc

#         # 오른쪽 회전
#         turn_r = (k+1) % 4
#         visited[ti][tj][turn_r] = tc
#         queue.append([ti, tj, turn_r, tc, cnt+1])

#         # 왼쪽 회전
#         turn_l = (k-1) % 4
#         visited[ti][tj][turn_l] = tc
#         queue.append([ti, tj, turn_l, tc, cnt+1])

#         # 전진
#         ni, nj = ti+di[k], tj+dj[k]
#         if 0 <= ni < N and 0 <= nj < N:
#             if FIELD[ni][nj] == 'T' and tc > 0 and (visited[ni][nj][k] == False or visited[ni][nj][k] < tc-1):    # 전진할 곳이 나무일 때
#                 # 나무를 자르고 해당 칸에 방문했을 때 그 칸에서의 남은 벨 수 있는 횟수보다 지금이 크면 갈 수 있는 경로가 더 생길 수 있음을 의미
#                 tc -= 1
#                 queue.append([ni, nj, k, tc, cnt+1])
#             else:
#                 if visited[ni][nj][k] == False and visited[ni][nj][k] < tc:
#                     queue.append([ni, nj, k, tc, cnt+1])

#     return -1

# def find(n, p):
#     for row in range(n):
#         for col in range(n):
#             if FIELD[row][col] == p:
#                 return row, col

# T = int(input())
# 4
# for test_case in range(1, T+1):
#     N, K = map(int, input().split())
#     FIELD = [list(input()) for _ in range(N)]

#     sti, stj = find(N, 'X')
#     endi, endj = find(N, 'Y')

#     print(f'#{test_case}', rc_car(sti, stj, K))