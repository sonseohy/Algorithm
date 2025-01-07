# 감시
# 1번 CCTV는 한 쪽 방향만 감시
# 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다.
# 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.
# CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.
# CCTV는 CCTV를 통과할 수 있으며, CCTV가 감시할 수 없는 영역은 사각지대라고 한다.
# 0은 빈 칸, 6은 벽, 1~5는 CCTV, CCTV의 최대 개수는 8개를 넘지 않는다.
# 사무실의 가로, 세로 크기는 8을 넘지 않는다.
# 사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성

# cctv 감시구역 표시 함수
def check(i, j, num):
    sharp = 0   # #으로 변환한 개수 저장 후 반환 (향후 복구를 위해)
    ni = i + d[num][0]
    nj = j + d[num][1]

    if num == 0:  # 우
        while nj < M:
            if office[ni][nj] == 6:
                break
            if office[ni][nj] == 0:
                office[ni][nj] = '#'
                sharp += 1
                area.append((ni, nj))
            nj += 1
    elif num == 1:    # 하
        while ni < N:
            if office[ni][nj] == 6:
                break
            if office[ni][nj] == 0:
                office[ni][nj] = '#'
                sharp += 1
                area.append((ni, nj))
            ni += 1
    elif num == 2:    # 좌
        while nj >= 0:
            if office[ni][nj] == 6:
                break
            if office[ni][nj] == 0:
                office[ni][nj] = '#'
                sharp += 1
                area.append((ni, nj))
            nj -= 1
    elif num == 3:    # 상
        while ni >= 0:
            if office[ni][nj] == 6:
                break
            if office[ni][nj] == 0:
                office[ni][nj] = '#'
                sharp += 1
                area.append((ni, nj))
            ni -= 1
    
    return sharp
    
def blind_spot(idx):
    global result
    # print('--------')
    # for n in range(N):
    #     print(*office[n])

    if idx == len(cctv):
        cnt = 0
        # 사각지대 체크
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    cnt += 1
        # result 최소 사각지대 값으로 바꿔줌
        result = min(result, cnt)
        return
    
    ci, cj = cctv[idx]

    # 5번 cctv는 4방향 모두 감시 (회전 X)
    if office[ci][cj] == 5:
        change = 0
        # 4방향 모두 감시 중인 구역 체크 후
        for dt in range(4):
            change += check(ci, cj, dt)
        # 다음 cctv로 이동
        blind_spot(idx+1)
        # 이전에 표시한 cctv 감시구역 초기화
        for _ in range(change):
            pi, pj = area.pop()
            office[pi][pj] = 0
    
    # 2번 cctv는 가로, 세로 방향으로 감시 (회전 1번 가능 == 2개의 경우 존재)
    elif office[ci][cj] == 2:
        # dt가 0일 때는 가로 방향으로 감시(d 인덱스 0과 2가 좌우 방향), 1일 때는 세로 방향으로 감시(d 인덱스 1과 3이 상하 방향)
        for dt in range(2):
            change = 0
            change += check(ci, cj, dt)
            change += check(ci, cj, dt+2)
            blind_spot(idx+1)
            # 이전에 표시한 cctv 감시구역 초기화
            for _ in range(change):
                pi, pj = area.pop()
                office[pi][pj] = 0
    # (회전 3번 가능 == 4개의 경우 존재)
    else:
        for dt in range(4):
            # 1번 cctv는 한 방향 감시
            if office[ci][cj] == 1:
                change = check(ci, cj, dt)
                blind_spot(idx+1)
                # 이전에 표시한 cctv 감시구역 초기화
                for _ in range(change):
                    pi, pj = area.pop()
                    office[pi][pj] = 0
            # 3번 cctv는 직각으로 두 방향 감시
            elif office[ci][cj] == 3:
                change = 0
                change += check(ci, cj, dt)
                change += check(ci, cj, (dt+1)%4)
                blind_spot(idx+1)
                # change 횟수 만큼 반복하면서 이전에 표시한 cctv 감시구역 초기화
                for _ in range(change):
                    pi, pj = area.pop()
                    office[pi][pj] = 0
            # 4번 cctv는 세 방향 감시
            elif office[ci][cj] == 4:
                change = 0
                change += check(ci, cj, dt)
                change += check(ci, cj, (dt+1)%4)
                change += check(ci, cj, (dt+2)%4)
                blind_spot(idx+1)
                # change 횟수 만큼 반복하면서 이전에 표시한 cctv 감시구역 초기화
                for _ in range(change):
                    pi, pj = area.pop()
                    office[pi][pj] = 0

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctv = []
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # R D L U
area = []   # cctv 방향이 바뀔 때 이전에 봤던 감시구역은 초기화해야 하므로 복구를 위해 #으로 변한 위치 정보 area 리스트에 저장
result = 64

# CCTV 위치 찾기
for r in range(N):
    for c in range(M):
        if office[r][c] != 0 and office[r][c] != 6:
            cctv.append((r, c))

blind_spot(0)

print(result)