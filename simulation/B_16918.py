# 봄버맨
# 크기가 R×C인 직사각형 격자판 위에서 살고 있는데, 각 칸은 비어있거나 폭탄이 들어있다.
# 폭탄이 있는 칸은 3초가 지난 후에 폭발하고, 폭발한 이후에는 폭탄이 있던 칸이 파괴되어 빈 칸이 되며, 인접한 네 칸도 함께 파괴된다.
# 만약, 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다. 따라서, 연쇄 반응은 없다.
# 빈 칸은 '.'로, 폭탄은 'O'로

# 3초 전 설치한 폭탄이 터짐
def burst(bomb_num):
    for i in range(R):
        for j in range(C):              
            if MAP[i][j] == bomb_num:
                # 3초전 설치한 폭탄 터짐
                MAP[i][j] = 0
                # 상하좌우 폭탄 터짐
                for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    ni, nj = i+di, j+dj
                    # 상하좌우가 터질때 미리 3초전 설치한 폭탄이 터지면 안되므로 MAP[ni][nj] != bomb_num 조건 추가
                    if 0 <= ni < R and 0 <= nj < C and MAP[ni][nj] != bomb_num:
                        MAP[ni][nj] = 0

# 폭탄이 비어있는 곳에 폭탄 설치
def put_bomb(t):
    for i in range(R):
        for j in range(C):
            if MAP[i][j] == '.' or MAP[i][j] == 0:
                MAP[i][j] = t

R, C, N = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

# N = 1일 때는 아무것도 안하므로 제외하고 반복
for n in range(2, N+1):
    # 짝수이면 폭탄이 없는 모든 곳에 폭탄 설치
    if n % 2 == 0:
        put_bomb(n)
    # 홀수이면 3초 전 설치한 폭탄 터짐
    else:
        if n == 3:  # 초기 상태 폭탄이 터질 때 'O'가 터져야 하므로 bomb_num으로 'O' 넘겨줌
            burst('O')
        else:
            burst(n-3)

for r in range(R):
    for c in range(C):
        if MAP[r][c] == '.' or MAP[r][c] == 0:
            print('.', end='')
        else:
            print('O', end='')
    print()