# [모의 SW 역량테스트] 미생물 격리
# 미생물들이 구역을 벗어나는걸 방지하기 위해, 가장 바깥쪽 가장자리 부분에 위치한 셀들에는 특수한 약품이 칠해져 있다.
# 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고, 이동방향이 반대로 바뀐다. 
# 살아남은 미생물 수 = 원래 미생물 수를 2로 나눈 후 소수점 이하를 버림 한 값
# 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우 군집들이 합쳐지게 된다. 
# 군집의 이동방향 (상: 1, 하: 2, 좌: 3, 우: 4)
# 미생물 군집의 정보는 세로 위치, 가로 위치, 미생물 수, 이동 방향 순으로 4개의 정수가 주어진다.

def isolation(time):
    tmp = []
    for idx in range(K):
        if population[idx] == None:
            continue

        r, c, num, dr = population[idx]

        if num == 0:
            continue

        ni, nj = r + move[str(dr)][0], c + move[str(dr)][1]
        if 0 < ni < N-1 and 0 < nj < N-1 and area[ni][nj] == -1:
            area[r][c] = -1
            area[ni][nj] = idx
        elif 0 < ni < N-1 and 0 < nj < N-1 and area[ni][nj] != -1:
            if population[area[ni][nj]] != None:
                area[r][c] = -1
                if area[ni][nj] < idx:
                    sum_v = population[area[ni][nj]][2] + num
                    if population[area[ni][nj]][2] > num:
                        population[idx] = None
                        population[area[ni][nj]][2] = sum_v
                    else:
                        population[area[ni][nj]] = None
                        area[ni][nj] = idx
                        population[idx][2] = sum_v
                else:
                    tmp.append(idx)
        elif ni == 0 or ni == N-1 or nj == 0 or nj == N-1:
            population[idx][2] //= 2
            area[r][c] = -1
            if population[idx][2] == 0:
                population[idx] = None
            else:
                area[ni][nj] = idx
            if dr % 2:
                population[idx][3] += 1
            else:
                population[idx][3] -= 1
        if population[idx]:
            population[idx][0] = ni
            population[idx][1] = nj

    if len(tmp):
        for tp in tmp:
            if area[population[tp][0]][population[tp][1]] == -1:
                area[population[tp][0]][population[tp][1]] = tp
            else:
                sum_v = population[area[population[tp][0]][population[tp][1]]][2] + population[tp][2]
                if population[area[population[tp][0]][population[tp][1]]][2] > population[tp][2]:
                    population[tp] = None
                    population[area[population[tp][0]][population[tp][1]]][2] = sum_v
                else:
                    population[area[population[tp][0]][population[tp][1]]] = None
                    area[population[tp][0]][population[tp][1]] = tp
                    population[tp][2] = sum_v


    if time == M-1:
        total = 0
        for p in population:
            if p != None:
                total += p[2]

        return total
    
T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    population = [list(map(int, input().split())) for _ in range(K)]

    result = 0
    move = {'1': (-1, 0), '2': (1, 0), '3': (0, -1), '4': (0, 1)}
    area = [[-1]*N for _ in range(N)]

    for start in range(K):
        area[population[start][0]][population[start][1]] = start

    for time in range(M):
        result = isolation(time)

    print(f'#{tc} {result}')
