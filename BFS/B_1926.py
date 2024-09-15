# 그림
# 어떤 큰 도화지에 그림이 그려져 있을 때, 그림의 개수와 그림 중 넓이가 가장 넓은 것의 넓이 출력
# 그림은 1로 연결된 것을 한 그림이라고 정의
# 대각선으로 연결된 것은 떨어진 그림이며, 그림의 넓이란 그림에 포함된 1의 개수

# 오답 : queue = []로 사용해 시간초과, deque 사용하기 
from collections import deque   # queue = []를 쓰는 것보다 시간이 훨씬 빠름


def board(sti, stj):
    global max_w, visited
    w = 1
    dq =deque()
    dq.append([sti, stj])

    while dq:
        ti, tj = dq.popleft()

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == False and PAINT[ni][nj] == 1:
                dq.append([ni, nj])
                visited[ni][nj] = True
                PAINT[ni][nj] = 0
                w += 1

    max_w = max(max_w, w)

N, M = map(int, input().split())
PAINT = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
max_w = 0
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if PAINT[i][j] == 1:
            visited[i][j] = True
            board(i, j)
            cnt += 1
print(cnt)
print(max_w)
