# 뱀
from collections import deque

def dummy(sti, stj):
    time = 0
    tail = deque()
    tail.append([sti, stj])
    visited = [[0] * N for _ in range(N)]
    visited[sti][stj] = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0
    r = c = 0

    while True:
        ni, nj = di[k] + r, dj[k] + c
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if board[ni][nj] == 'A':
                visited[ni][nj] = 1
                board[ni][nj] = 0
                tail.append([ni, nj])
            else:
                if len(tail) > 1:
                    ti, tj = tail.popleft()
                    tail.append([ni, nj])
                    visited[ti][tj] = 0
                    visited[ni][nj] = 1

                else:
                    tail.popleft()
                    tail.append([ni, nj])
                    visited[r][c] = 0
                    visited[ni][nj] = 1

            time += 1
            if change_dict.get(str(time)) is not None:
                if change_dict[str(time)] == 'D':
                    k = (k + 1) % 4
                elif change_dict[str(time)] == 'L':
                    k = (k - 1) % 4
            r = ni
            c = nj
        else:
            return time + 1


N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    board[R - 1][C - 1] = 'A'

L = int(input())
change_dict = {}
for _ in range(L):
    s, d = input().split()
    change_dict[s] = d

print(dummy(0, 0))


"""
# 뱀
from collections import deque

def dummy(sti, stj):
    time = 0
    tail = deque()
    tail.append([sti, stj])
    visited = [[0] * N for _ in range(N)]    # 뱀이 있는 자리를 표시
    visited[sti][stj] = 1
    
    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0        # 뱀의 이동 방향 결정
    r = c = 0    # 시작지점

    while True:
        ni, nj = di[k] + r, dj[k] + c
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if board[ni][nj] == 'A':    # 이동하려는 칸에 사과가 있을 때
                visited[ni][nj] = 1     # 다음 칸 방문체크
                board[ni][nj] = 0       # 사과 먹기 (사과자리에 0)
                tail.append([ni, nj])   # 뱀의 길이가 늘어나므로 tail에 다음 칸 append
            else:    # 사과가 없는 경우
                if len(tail) > 1:    # 뱀의 길이가 2 이상인 경우 : 뱀의 길이를 유지하며 이동해야함
                    ti, tj = tail.popleft()    # 뱀이 움직여야 하므로 뱀의 꼬리 인덱스를 pop
                    tail.append([ni, nj])      # 꼬리를 빼줬으므로 길이 유지를 위해 다음 칸(뱀의 머리에 해당)을 append
                    visited[ti][tj] = 0        # 꼬리를 빼줬으므로 해당 칸엔 뱀이 없기 때문에 visited를 0으로 바꿔줌
                    visited[ni][nj] = 1        # 뱀의 머리 위치 visited

                else:    # 뱀의 길이가 1 인 경우 : 한 칸씩 이동만 하면 되므로 이전 칸에서 다음 칸으로 이동
                    tail.popleft()           # 꼬리가 다음칸으로 이동해야하므로 pop 
                    tail.append([ni, nj])    # 새로 이동할 위치 append
                    visited[r][c] = 0        # 빠진 꼬리 인덱스 visited 0으로
                    visited[ni][nj] = 1      # 새로 뱀이 이동한 위치 visited 1로

            time += 1    # 뱀이 이동을 마치면 시간 +1
            
            # 만약 time이 뱀이 회전해야하는 시간이라면
            if change_dict.get(str(time)) is not None:
                if change_dict[str(time)] == 'D':
                    k = (k + 1) % 4    # 오른쪽으로 90도 (우, 하, 좌, 상 방향)
                elif change_dict[str(time)] == 'L':
                    k = (k - 1) % 4    # 왼쪽으로 90도 (우, 상, 좌, 하 방향)
            r = ni
            c = nj
        else:    # 뱀의 몸에 부딪히거나 벽에 부딪힐 때
            return time + 1


N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    board[R - 1][C - 1] = 'A'

L = int(input())
change_dict = {}    # 시간 초와 이동 방향 딕셔너리로 저장
for _ in range(L):
    s, d = input().split()
    change_dict[s] = d

print(dummy(0, 0))
"""