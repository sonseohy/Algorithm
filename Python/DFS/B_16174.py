# 점프왕 쩰리
# 쩰리가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
# 쩰리의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸 (0, 0)
# 쩰리가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
# 쩰리가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료
# 쩰리가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.
# 쩰리를 도와 주어진 게임 구역에서 끝 점(오른쪽 맨 아래 칸)까지 도달할 수 있는지를 알아보자!
# 게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여있다.
# ‘쩰리’가 끝 점에 도달할 수 있으면 HaruHaru, 도달할 수 없으면 Hing을 한 줄에 출력
from collections import deque
def dfs(sti, stj, k):
    stack = deque()
    stack.append((sti, stj, k))
    visited = [[0]*N for _ in range(N)]
    visited[sti][stj] = 1

    move = [(0, 1), (1, 0)]     # 오른쪽, 아래 방향

    while stack:
        ti, tj, jump = stack.pop()

        if MAP[ti][tj] == -1:
            return 'HaruHaru'   # -1에 도착 가능할 때

        for di, dj in move:
            ni, nj = di*jump + ti, dj*jump + tj     # di, dj에 점프 가능한 칸 수를 곱해 ni, nj 생성
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                stack.append([ni, nj, MAP[ni][nj]])
                visited[ni][nj] = 1
    return 'Hing'   # -1에 도착하지 못할 때

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

print(dfs(0, 0, MAP[0][0])) # 시작지점 i,j와 점프 가능한 거리