# 유기농 배추
# 배추들이 모여있는 곳에는 배추 흰 지렁이가 한 마리만 있으면 됨
# 0은 배추가 심어져 있지 않은 땅, 1은 배추가 심어져 있는 땅
# 출력 : 최소의 배추흰지렁이 마리 수
def cabbage(sti, stj):
    visited = [[0]*M for _ in range(N)]
    visited[sti][stj] = 1
    queue = []
    queue.append([sti, stj])

    while queue:
        ti, tj = queue.pop(0)

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and FARM[ni][nj] == 1:
                queue.append([ni,nj])
                visited[ni][nj] = 1
                FARM[ni][nj] = 0
        

T = int(input())

for test_case in range(T):
    M, N, K = map(int, input().split())     # M : 배추밭 가로, N : 배추밭 세로, K : 배추 심어진 위치
    FARM = [[0]*M for _ in range(N)]

    for _ in range(K):
        y, x = map(int, input().split())
        FARM[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if FARM[i][j] == 1:
                cabbage(i, j)
                cnt += 1
    print(cnt)