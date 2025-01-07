# 차윤이의 RC칸
# G : RC카가 이동 가능한 땅, T : RC카가 이동 불가능한 나무
# X : 현재 RC카 위치, Y : RC카를 이동시키고자 하는 위치
# RC카 동작 : A - 앞으로 이동, L - 왼쪽으로 90도 회전, R - 오른쪽으로 90도 회전
# RC카를 항상 위를 바라보는 방향으로부터 조종 시작
# RC카를 조종한 커맨드가 주어졌을 때,  목적지에 도달 할 수 있는지 구하라.
def rc_car(i, j, cmd_n, cmd):
    # 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    k = 0
    for cn in range(cmd_n):
        if cmd[cn] == 'L':
            k = (k-1) % 4
        elif cmd[cn] == 'R':
            k = (k+1) % 4
        elif cmd[cn] == 'A' and 0 <= i+di[k] < N and 0 <= j+dj[k] < N and FIELD[i+di[k]][j+dj[k]] != 'T':
            i += di[k]
            j += dj[k]

    if FIELD[i][j] == 'Y':
        return 1
    else:
        return 0

def find_start(n):
    for r in range(n):
        for c in range(n):
            if FIELD[r][c] == 'X':
                return r, c

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    FIELD = [list(input()) for _ in range(N)]
    Q = int(input())
    COMMAND = [list(input().split()) for _ in range(Q)]

    sti, stj = find_start(N)

    result = []
    for q in range(Q):
        result.append(rc_car(sti, stj, int(COMMAND[q][0]), COMMAND[q][1]))
    print(f'#{test_case}', *result)
    