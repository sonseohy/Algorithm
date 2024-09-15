# 적록색약
# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못함
# N X N에 R, G, B 색칠된 그림이 있고, 구역은 같은 색으로 이루어짐
# 같은 색이 상하좌우 인접해 있는 경우 두 글자는 같은 구역
# 출력 : 적록색약이 본 구역의 수, 적록색약 아닌 사람이 본 구역의 수
from collections import deque

def count_area(sti, stj, rg):
    global visited, rg_o, rg_x
    dq = deque()
    dq.append([sti, stj])
    # 스타트 지점 방문체크
    if rg:
        visited_rg[sti][stj] = 1
    else:
        visited[sti][stj] = 1

    while dq:
        ti, tj = dq.popleft()

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < N and visited_rg[ni][nj] == 0 and rg:   # 적록색약인 경우
                if PAINT[sti][stj] == 'B' and PAINT[ni][nj] == 'B':
                    dq.append([ni, nj])
                    visited_rg[ni][nj] = 1
                elif PAINT[sti][stj] != 'B' and PAINT[ni][nj] != 'B':
                    dq.append([ni, nj])
                    visited_rg[ni][nj] = 1

            elif 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and not rg:   # 적록색약이 아닌 경우
                if PAINT[sti][stj] == PAINT[ni][nj]:
                    dq.append([ni, nj])
                    visited[ni][nj] = 1
    if rg:
        rg_o += 1
    else:
        rg_x += 1
      

N = int(input())
PAINT = [list(input()) for _ in range(N)]

rg_o = 0  # 적록색약
rg_x = 0    # 적록색약 x
visited_rg = [[0]*N for _ in range(N)]  # 적록색약 구역 방문 체크
visited = [[0]*N for _ in range(N)]     # 적록색약 아닌 사람이 본 구역 방문 체크
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            count_area(i, j, False)    # 적록색약인 경우
        if visited_rg[i][j] == 0:
            count_area(i, j, True)     # 적록색약이 아닌 경우

print(rg_x, rg_o)

