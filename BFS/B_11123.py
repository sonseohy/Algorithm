# 양 한마리... 양 두 마리...
# 양을 #으로 나타내고 .으로 풀을 표현
# 서로 다른 # 두 개 이상이 붙어있다면 한 무리의 양들이 있는 것
# 그리드 위에 양무리가 몇개 있었는지 출력
def count_sheep(sti, stj):
    visited = [[False]*W for _ in range(H)]
    visited[sti][stj] = True
    queue = []
    queue.append([sti, stj])

    while queue:
        ti, tj = queue.pop(0)

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == False and GRID[ni][nj] == '#':
                queue.append([ni, nj])
                visited[ni][nj] = True
                GRID[ni][nj] = '.'

T = int(input())

for test_case in range(T):
    H, W = map(int, input().split())
    GRID = [list(input()) for _ in range(H)]

    cnt = 0
    for r in range(H):
        for c in range(W):
            if GRID[r][c] == '#':
                count_sheep(r, c)
                cnt += 1

    print(cnt)