# 로봇 청소기
# 로봇 청소기는 현재 칸이 청소되지 않은 경우, 현재 칸을 청소한다.
# 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우, 바라보는 방향을 유지하고 한칸 후진할 수 있으면 후진, 후진할 수 없으면 작동 중단
# 4칸 중 청소되지 않은 빈 칸이 있는 경우, 반시계 방향 90도 회전, 바라보는 방향 기준 앞쪽 칸이 청소되지 않았다면 전진
# d = 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
# 0은 청소되지 않은 빈 칸, 1인 경우 벽, 로봇 청소기가 있는 칸은 항상 빈 칸
def clean(sti, stj, d):
    cnt = 1
    room[sti][stj] = 2    # 청소된 칸은 2로 표시
    visited = [[0] * M for _ in range(N)]
    visited[sti][stj] = 1
    cur_i, cur_j, cur_d = sti, stj, d

    while True:
        check = 0
        for di, dj in direction:
            ni, nj = di + cur_i, dj + cur_j
            # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
            if 0 <= ni < N and 0 <= nj < M and room[ni][nj] == 0:
                cur_d = (cur_d - 1) % 4     # 반시계 방향 90도 회전
                next_i = cur_i + direction[cur_d][0]
                next_j = cur_j + direction[cur_d][1]
                if room[next_i][next_j] == 0:   # 회전 후 앞쪽 칸이 청소되지 않은 빈 칸인 경우 전진
                    visited[next_i][next_j] = 1
                    room[next_i][next_j] = 2
                    cnt += 1
                    cur_i, cur_j = next_i, next_j
                    break

            elif 0 <= ni < N and 0 <= nj < M and room[ni][nj]:  # 청소된 빈 칸 체크
                check += 1

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if check == 4:
            back = (cur_d - 2) % 4  # 후진
            bi = cur_i + direction[back][0]
            bj = cur_j + direction[back][1]
            if room[bi][bj] == 0:   # 후진 후 청소되지 않은 칸일 때
                cur_i, cur_j = bi, bj
                cnt += 1
            elif room[bi][bj] == 2: # 청소된 칸이지만 후진 가능한 경우
                cur_i, cur_j = bi, bj
            elif room[bi][bj] == 1: # 벽이라 후진할 수 없는 경우
                return cnt


N, M = map(int, input().split())
R, C, D = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
print(clean(R, C, D))