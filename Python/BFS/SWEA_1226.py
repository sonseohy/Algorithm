# 미로1
# 16*16 행렬의 형태로 만들어진 미로에서 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
# 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성

def bfs(sti, stj):
    visited = [[0]*16 for _ in range(16)]
    visited[sti][stj] = 1
    queue = []
    queue.append([sti, stj])

    while queue:
        ti, tj = queue.pop(0)

        if maze[ti][tj] == 3:
            return 1

        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                queue.append([ni, nj])
                visited[ni][nj] = 1
    return 0

T = 10
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    print(bfs(1, 1))