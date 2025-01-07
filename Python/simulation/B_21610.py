# 마법사 상어와 비바라기
# 비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
# 모든 구름이 di 방향으로 Si칸 이동하고 구름 위치에 비가 내려 구름 위치 바구니에 저장된 물의 양이 1 증가
# 구름이 모두 사라지고 물이 증가한 칸에 물복사 버그 마법 시전
# 물복사 버그 마법을 사용하면 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수 만큼 바구니의 물 양 증가
# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어듦, 이때 구름이 생기틑 칸은 위에서 이전에 구름이 사라진 칸이 아니여야 함
# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구하라
import sys
input = sys.stdin.readline

def cloud_generate(cloud_pos):
    new_pos = []
    for r in range(N):
        for c in range(N):
            if (r,c) not in cloud_pos:
                if basket[r][c] >= 2:
                    basket[r][c] -= 2
                    new_pos.append((r, c))
    return new_pos

def water_bug(i, j):
    # 대각선 방향으로 거리가 1인 칸의 물 확인
    for k in [2, 4, 6, 8]:
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < N and basket[ni][nj] > 0:
            basket[i][j] += 1
    
def cloud_move(ci, cj, k, move_n):
    ci += di[k] * move_n
    cj += dj[k] * move_n
    # 이동했을때 인덱스 범위를 넘어가는 경우를 고려해 ci, cj 한번 더 계산
    ci = (ci % N + N) % N
    cj = (cj % N + N) % N
    return (ci, cj)

N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]
movement = [list(map(int, input().split())) for _ in range(M)]

# 방향이 1번부터 8가지 있으므로 1번 인덱스부터 방향 저장
di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 처음 구름이 생성되는 위치를 cloud_lst에 넣어줌
# 문제에서 가장 왼쪽 윗 칸을 (1, 1)로 보고 있으므로 -1씩 해서 구름 위치 저장
cloud_lst = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for m in range(M):
    cloud_pos = []
    # 구름 이동
    for c in cloud_lst:
        cloud = cloud_move(c[0], c[1], movement[m][0], movement[m][1])  # 구름 위치 인덱스 i, j와 이동방향, 이동횟수를 함수로 넘겨줌
        cloud_pos.append(cloud)
        
    # 구름 위치에 비 내림
    for cp in cloud_pos:
        basket[cp[0]][cp[1]] += 1

    # 물 복사 버그 마법
    for pi, pj in cloud_pos:
        water_bug(pi, pj)

    # 물의 양이 2 이상인 칸 확인 후 구름 생성
    cloud_lst = cloud_generate(cloud_pos)

sum_v = 0
for i in range(N):
    for j in range(N):
        sum_v += basket[i][j]

print(sum_v)


# 시도 1. 시간초과
"""
import sys
input = sys.stdin.readline

def cloud_generate(cloud_pos):
    new_pos = []
    for r in range(N):
        for c in range(N):
            if [r,c] not in cloud_pos:
                if basket[r][c] >= 2:
                    basket[r][c] -= 2
                    new_pos.append([r, c])
    return new_pos

def water_bug(i, j):
    # 대각선 방향으로 거리가 1인 칸의 물 확인
    for k in [2, 4, 6, 8]:
        ni, nj = i+di[k], j+dj[k]
        if 0 <= ni < N and 0 <= nj < N and basket[ni][nj] > 0:
            basket[i][j] += 1
    
def cloud_move(ci, cj, k, move_n):
    ci += di[k] * move_n
    cj += dj[k] * move_n
    # 이동했을때 인덱스 범위를 넘어가는 경우를 고려해 ci, cj 한번 더 계산
    ci = (ci % N + N) % N
    cj = (cj % N + N) % N
    return [ci, cj]

N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]
movement = [list(map(int, input().split())) for _ in range(M)]

# 방향이 1번부터 8가지 있으므로 1번 인덱스부터 방향 저장
di = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dj = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 처음 구름이 생성되는 위치를 cloud_lst에 넣어줌
# 문제에서 가장 왼쪽 윗 칸을 (1, 1)로 보고 있으므로 -1씩 해서 구름 위치 저장
cloud_lst = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for m in range(M):
    cloud_pos = []
    # 구름 이동
    for c in cloud_lst:
        cloud = cloud_move(c[0], c[1], movement[m][0], movement[m][1])  # 구름 위치 인덱스 i, j와 이동방향, 이동횟수를 함수로 넘겨줌
        cloud_pos.append(cloud)
        
    # 구름 위치에 비 내림
    for cp in cloud_pos:
        basket[cp[0]][cp[1]] += 1

    # 물 복사 버그 마법
    for pi, pj in cloud_pos:
        water_bug(pi, pj)

    # 물의 양이 2 이상인 칸 확인 후 구름 생성
    cloud_lst = cloud_generate(cloud_pos)

sum_v = 0
for i in range(N):
    for j in range(N):
        sum_v += basket[i][j]

print(sum_v)
"""