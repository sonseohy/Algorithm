# 펭귄의 하루 (미완)
# N X M의 펭귄마을, E:안전 구역, D: 위험 구역, F:먹이 구역
# 펭귄은 위험구역이 아닌 곳을 상하좌우로 이동, 마을 밖 이동 X
# 현재 위치에서 출발하여 물고기 서식지 중 최소한 한 곳을 들러 사냥을 마치고 집으로 돌아가려 함
# 물고기를 사냥해 최대한 빠르게 펭귄의 집에 도달하는 데 걸리는 시간 출력
# S:현재위치, H:펭귄 집
# 물고기 서식지는 공간에 1개 이상 1000개 이하로 존재
import sys
from collections import deque

def go(sti, stj):
    global visited
    dq = deque()
    dq.append([sti, stj])
    visited[sti][stj] = 1

    while dq:
        ti, tj = dq.popleft()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = di+ti, dj+tj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and MAP[ni][nj] != 'D':
                dq.append([ni, nj])
                visited[ni][nj] = visited[ti][tj] + 1

N, M = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline()) for _ in range(N)]

time = 0
result = 1e8
goal = [[] for _ in range(2)]
fish = []
visited = [[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if MAP[r][c] == 'S':
            goal[0] = [r,c]
        if MAP[r][c] == 'H':
            goal[1] = [r,c]
        if MAP[r][c] == 'F':
            fish.append([r,c])
go(goal[0][0], goal[0][1])    # start지점에서 각각 최소거리 계산
if visited[goal[1][0]][goal[1][1]]:
    for f in fish:
        time += visited[f[0]][f[1]] - 1
        visited = [[0]*M for _ in range(N)]
        go(f[0], f[1])
        if visited[goal[1][0]][goal[1][1]]:
            time += visited[goal[1][0]][goal[1][1]] - 1
            result = min(result, time)
        else:
            time = 0
            result = -1
else:
    result = -1

print(result)