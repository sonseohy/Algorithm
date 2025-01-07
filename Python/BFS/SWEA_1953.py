# 탈주범 검거
# 탈주범은 시간당 1의 거리를 움직일 수 있고, 지하 터널은 총 7 종류의 구조물로 구성되어 있다.
# 지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산하는 프로그램을 작성
# 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 탈출 후 소요된 시간 L
from collections import deque

def move_tunnel(sti, stj):
    queue = deque()
    queue.append([sti, stj])
    visited = [[0]*M for _ in range(N)]
    visited[sti][stj] = 1
    cnt = 0

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    unconnected = [[0, 2, 4, 5], [0, 3, 5, 6], [0, 2, 6, 7], [0, 3, 4, 7]]  # 파이프의 방향별로 연결되지 않은 파이프 종류를 저장

    while queue:
        ti, tj = queue.popleft()

        if visited[ti][tj] == L:    # 시간이 모두 소요되면 이동 종료
            break
        
        for k in tunnel_type[t_map[ti][tj]]:
            ni, nj = ti+di[k], tj+dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and t_map[ni][nj] not in unconnected[k]:    # 방문하지 않았고, 다음 파이프가 연결되어 있을때만
                queue.append([ni, nj])
                visited[ni][nj] = visited[ti][tj] + 1   # visited에 이동한 시간 저장

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:  # 방문한 지점들을 카운트
                cnt += 1

    return cnt


T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    t_map = [list(map(int, input().split())) for _ in range(N)]

    tunnel_type = [[], [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [0, 1], [1, 2], [2, 3]]    # 터널 유형별로 갈 수 있는 방향 K를 저장
    print(f'#{test_case}', move_tunnel(R, C))

