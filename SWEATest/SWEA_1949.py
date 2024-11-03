# [모의 SW 역량테스트] 등산로 조성
# 등산로를 만들기 위한 부지는 N * N 크기를 가지고 있으며, 이곳에 최대한 긴 등산로를 만들 계획
# 각 숫자는 지형의 높이를 나타내며, 등산로를 만드는 규칙은 다음과 같다.
# 1. 등산로는 가장 높은 봉우리에서 시작해야 한다.
# 2. 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
# 즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.
# 3. 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.
# N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다. 이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성
# 오답 point!
# 주의! 최대 K 깊이만큼 깎을 수 있음, 즉 1~K까지 깎을 수 있다는 의미, 무조건 K 값을 깎는 것 X
# -> 가장 긴 등산로를 만드려면 가장 적게 깎아야함 -> 높이가 같은 경우 1만큼만 깎고 다른 경우 두 높이 차에서 +1 만큼 깎기
# 주의! 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.
def trail(i, j, point, length, visited):  # 시작 지점 인덱스 i, j, 공사 가능 횟수 point, 등산로 길이 length, 간 경로 저장할 visited
    global result
    result = max(length, result)    # 등산로의 길이 최댓값 갱신

    # 가장 높은 곳에서 갈 수 있는 낮은 지형들을 찾아감
    for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
            if MAP[ni][nj] >= MAP[i][j] and point and MAP[ni][nj] - K < MAP[i][j]:  # 다음 위치가 현재 위치 높이보다 높지만 공사가 가능한 경우
                visited.append((ni, nj))
                if MAP[ni][nj] == MAP[i][j]:    # 가장 적게 깎아 긴 등산로를 만들기 위해 두 높이가 같은 경우 1만큼만 깎음
                    MAP[ni][nj] -= 1
                    trail(ni, nj, 0, length+1, visited)
                    MAP[ni][nj] += 1
                else:
                    cut = MAP[ni][nj] - MAP[i][j] + 1   # 다음 위치가 더 높은 경우 두 높이 차에서 +1 만큼만 깎음
                    MAP[ni][nj] -= cut
                    trail(ni, nj, 0, length+1, visited)
                    MAP[ni][nj] += cut
                visited.pop()
            if MAP[ni][nj] < MAP[i][j]:     # 다음 위치가 현재 위치보다 낮은 경우 (깎지 않고 갈 수 있는 경우)
                visited.append((ni, nj))
                trail(ni, nj, point, length+1, visited)
                visited.pop()


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # 1. 시작지점인 최대 높이 찾기
    max_v = 0   # 최대 높이 찾기 위한 변수
    for h in range(N):
        max_v = max(max_v, max(MAP[h]))
    
    # 2. 시작 지점들의 인덱스 찾기
    start = []  # 시작 지점인 가장 높은 봉우리들을 담을 리스트
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == max_v:
                start.append((r, c))

    result = 0  # 최대 등산로 저장할 변수
    for i, j in start:  # 시작 지점을 하나씩 trail 함수에 넘겨줌
        trail(i, j, 1, 1, [(i, j)])

    print(f'#{tc} {result}')


# 시도1. BFS : 실패 (visited 갱신이 안됨)
"""
def trail(sti, stj, high, p):
    queue = []
    queue.append((sti, stj, high, p))
    visited = [[0]*N for _ in range(N)]
    visited[sti][stj] = 1
    trail_len = 0

    while queue:
        ti, tj, h, point = queue.pop(0)

        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if MAP[ni][nj] >= h and point and MAP[ni][nj] - K < h:
                    queue.append((ni, nj, MAP[ni][nj] - K, 0))
                    visited[ni][nj] = visited[ti][tj] + 1
                if MAP[ni][nj] < h:
                    queue.append((ni, nj, MAP[ni][nj], 1))
                    visited[ni][nj] = visited[ti][tj] + 1
            # 방문을 했지만 이전의 등산로 경로보다 더 길다면 visited 갱신
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] and visited[ni][nj] != 1:
                if MAP[ni][nj] < h and visited[ni][nj] < visited[ti][tj] + 1:
                    visited[ni][nj] = visited[ti][tj] + 1
                    queue.append((ni, nj, MAP[ni][nj], point))
                if MAP[ni][nj] >= h and point and MAP[ni][nj] - K < h and visited[ni][nj] < visited[ti][tj] + 1:
                    queue.append((ni, nj, MAP[ni][nj] - K, 0))
                    visited[ni][nj] = visited[ti][tj] + 1

    print('------------------')
    for k in range(N):
        print(*visited[k])

    for i in range(N):
        trail_len = max(trail_len, (max(visited[i])))

    return trail_len

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    # 1. 시작지점인 최대 높이 찾기
    max_v = 0   # 최대 높이 찾기 위한 변수
    for h in range(N):
        max_v = max(max_v, max(MAP[h]))
    
    # 2. 시작 지점들의 인덱스 찾기
    start = []  # 시작 지점들을 담을 리스트
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == max_v:
                start.append((r, c))

    result = 0
    for i, j in start:
        tmp = trail(i, j, MAP[i][j], 1)
        result = max(result, tmp)


    print(f'#{tc} {result}')
"""

# 다른 코드 (유정언니)
"""
def climb(i, j, one):
    global result
    result = max(result, visited[i][j])  # 최댓값 갱신

    # 4방향 탐색
    for k in [(0,1), (1,0), (0,-1), (-1,0)]:
        ni, nj = i + k[0], j + k[1]
        # 범위 내에 있고, 방문하지 않은 경우
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if maps[i][j] > maps[ni][nj]:  # 지형이 낮다면
                visited[ni][nj] = visited[i][j] + 1  # 방문 표시
                climb(ni, nj, one)
                visited[ni][nj] = 0 # 방문 해제

            # 공사 기회가 있고, 공사할 경우 지형이 낮다면
            elif one and maps[i][j] > maps[ni][nj] - K:
                visited[ni][nj] = visited[i][j] + 1   # 방문 표시
                temp = maps[ni][nj]
                maps[ni][nj] = maps[i][j] - 1   # 가장 긴 경로를 찾아야 하므로 이전 지형에서 -1 깎기
                climb(ni, nj, one-1)
                visited[ni][nj] = 0   # 방문 해제
                maps[ni][nj] = temp   # 원래 값 되돌리기


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 배열크기, 공사가능 깊이
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 최대 높이 찾기
    top = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > top:
                top = maps[i][j]

    # 등산로 찾기
    result = 0  # 최대 등산로 길이
    for i in range(N):
        for j in range(N):
            if maps[i][j] == top:
                visited[i][j] = 1
                climb(i, j, 1)
                visited[i][j] = 0

    print(f'#{test_case} {result}')
"""