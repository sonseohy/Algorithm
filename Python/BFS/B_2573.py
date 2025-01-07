# 빙산
# 빙산 이외의 바다에 해당되는 칸에는 0이 저장
# 빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 빙산의 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
# 단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
# 2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다. 
# 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성
# 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력
from collections import deque

# 빙산 한 덩어리 탐색하는 함수
def count_ice(ci, cj):
    cq = deque()
    cq.append((ci, cj))
    cnt_visited[ci][cj] = 1

    while cq:
        ti, tj = cq.popleft()

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < M and cnt_visited[ni][nj] == 0 and iceberg[ni][nj] != 0:
                cq.append((ni, nj))
                cnt_visited[ni][nj] = 1

# 1년동안 빙산의 높이가 얼마나 녹는지 확인하는 함수
def melt_iceberg(i, j):
    q = deque()
    q.append((i, j))
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    cut_lst = []    # 녹는 빙산의 정보 저장하는 리스트 (녹는 빙산의 위치 i, j와 녹는 높이 cut 저장)

    while q:
        ti, tj = q.popleft()
        cnt = 0     # 빙산 주변의 바다 갯수 저장

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti+di, tj+dj
            # 현재 빙산 주변에 빙산이 있는 경우
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and iceberg[ni][nj] != 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
            # 현재 빙산 주변에 바다가 있는 경우
            if 0 <= ni < N and 0 <= nj < M and iceberg[ni][nj] == 0:
                cnt += 1
                # 오답 point: 바다를 확인하고 빙산을 바로 깎으면 다른 대륙에서 바다를 확인할 때 빙산이였던 곳이 바다로 판정되어 버리는 경우 발생
                # iceberg[ti][tj] -= 1
        
        # 한 빙산의 4곳을 모두 확인한 후(for문 이후), 바다가 접해있는 갯수 cnt가 0보다 커서 빙산이 녹아야 할 경우 cut_lst에 저장
        if cnt > 0 :
            cut_lst.append((ti, tj, cnt))

    # cut_lst를 확인하면서 빙산 높이 조정
    for cut_i, cut_j, cut in cut_lst:
        # 녹아야 하는 높이가 빙산 높이보다 크거나 같으면 해당 빙산 영역 0으로 (-가 되는 것을 막기 위해)
        if iceberg[cut_i][cut_j] <= cut:
            iceberg[cut_i][cut_j] = 0
        # 빙산 높이가 더 크면 cut만큼 빙산 깎기
        else:
            iceberg[cut_i][cut_j] -= cut

# 빙산의 시작 지점 찾는 함수
def find_ice():
    for r in range(N):
        for c in range(M):
            if iceberg[r][c] != 0:
                return r, c
    
    return False, False # 빙산이 없으면 False 반환

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
time = 0
piece = False

while True:
    # 빙산 녹음
    sti, stj = find_ice()
    melt_iceberg(sti, stj)

    # 빙산 조각 카운트
    cnt_visited = [[0]*M for _ in range(N)] # 빙산 덩어리를 세기 위한 visited
    ci, cj = find_ice()
    # 빙산이 전부 녹아버렸을 때
    if not ci :
        time = 0
        break
    # 빙산이 남아있을 때
    else:
        count_ice(ci, cj)
    
    # 빙산이 한번 녹은 후
    for n in range(N):
        for m in range(M):
            # 높이가 남아있는 빙산이 있고, 빙산 조각을 카운트 때 체크하지 않은 빙산이 있다면 두 덩어리 이상으로 분리된 것이므로 for문을 끝낸다.
            if iceberg[n][m] != 0 and cnt_visited[n][m] == 0:
                piece = True
                break
        if piece:
            break
    time += 1   # 1년동안의 과정이 끝나면 시간을 +1하고
    if piece:
        break   # piece가 True가 됐다면 조각이 두 개 이상이라는 뜻이므로 while문 끝냄

print(time)
    
