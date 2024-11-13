# 빵집
def bakery(i, j):
    global cnt, finish
    visited[i][j] = 1

    if j == C-1:
        cnt += 1
        finish = True
        return

    for di, dj in [(-1, 1), (0, 1), (1, 1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < R and 0 < nj < C and visited[ni][nj] == 0 and MAP[ni][nj] != 'x':
            bakery(ni, nj)
            if finish:
                return

R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

cnt = 0
visited = [[0]*C for _ in range(R)]
for r in range(R):
    finish = False
    bakery(r, 0)

print(cnt)