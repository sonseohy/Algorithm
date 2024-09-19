# 뱀
from collections import deque

def dummy(sti, stj):
    time = 1
    tail = deque()
    tail.append([sti, stj])
    visited = [[0] * N for _ in range(N)]
    visited[sti][stj] = 1
    
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0
	
    for r in range(N):
        for c in range(N):
            ni, nj = di[k] + r, dj[k] + c
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if board[ni][nj] == 'A':
                    visited[ni][nj] = 1
                    board[ni][nj] = 0
                    tail.append([ni, nj])
                else:
                    if visited[ni][nj] == 1:
                        visited[ni][nj] = 1
                        tail.popleft()
                    else:
                        visited[r][c] = 0
                        visited[ni][nj] = 1
                        tail.popleft()
                        tail.append([ni, nj])
                    
                time += 1
                if change_dict.get(str(time)) is not None:
                    if change_dict[str(time)] == 'D':
                        k = (k + 1) % 4
                    elif change_dict[str(time)] == 'L':
                        k = (k - 1) % 4
                r += di[k]
                c += dj[k]
            else:
                return time

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
