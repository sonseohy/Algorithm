# 데스 나이트
# 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
# 크기 N X N인 체스판에서 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수 구하기
def chess(sti, stj):
    visited = [[0]*N for _ in range(N)]
    visited[sti][stj] = 1
    queue = []
    queue.append([sti, stj])

    while queue:
        ti, tj = queue.pop(0)

        if ti == r2 and tj == c2:
            return visited[ti][tj] - 1
        
        for di, dj in [[-2, -1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                queue.append([ni,nj])
                visited[ni][nj] = visited[ti][tj] + 1
    return -1


N = int(input())
r1, c1, r2, c2 = map(int, input().split())

print(chess(r1, c1))