# 가스관
# 유럽은 R행 C열, 가스는 모스크바(M) -> 자그레브(Z)
# 각 칸은 비어 있거나 7가지 기본 블록
# 해커가 어떤 칸을 지웠고, 그 칸에는 원래 어떤 블록이 있었는지 구하는 프로그램을 작성

import sys
from collections import deque
input = sys.stdin.readline

def find_pipe(bi, bj):
    # 방향별로 연결될 수 있는 파이프 모양을 딕셔너리 값으로 저장
    possible_pipe = {'0': ('-', '+', '1', '2'),'1': ('|', '+', '2', '3'), '2': ('-', '+', '3', '4'), '3': ('|', '+', '1', '4')}
    
    k_lst = []  # 상하좌우를 확인하면서 연결할 수 있는 파이프가 있는 칸의 방향을 리스트에 담기
    for k in range(4):
        ni, nj = bi+di[k], bj+dj[k]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != '.' and arr[ni][nj] in possible_pipe[str(k)]:
            k_lst.append(k)

    # 모든 방향에 파이프가 존재한다면 가능한 파이프는 '+' 밖에 없으므로 '+' 반환
    if len(k_lst) == 4:
        return '+'

    # k_lst에 담긴 방향 값으로 gas_block에서 해당하는 딕셔너리 키를 찾아 반환
    pipe_key = [key for key, value in gas_block.items() if value == tuple(k_lst)]
    return pipe_key

def gas_pipe(i, j, p):
    queue = deque()
    queue.append([i, j, p]) # 파이프 모양인 p도 함께 큐에 저장
    visited = [[0]*C for _ in range(R)]
    visited[i][j] = 1

    while queue:
        ti, tj, tp = queue.popleft()

        for k in gas_block[tp]:
            ni, nj = ti+di[k], tj+dj[k]
            if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0 and arr[ni][nj] != '.' and arr[ni][nj] != 'Z':
                queue.append([ni, nj, arr[ni][nj]])
                visited[ni][nj] = 1
                continue

        # 다음으로 이동할 파이프가 없으면
        if tp != 'start':
            for p in gas_block[tp]:
                blank_i = ti + di[p]
                blank_j = tj + dj[p]
                if visited[blank_i][blank_j] == 0:
                    # 가스관이 끊긴 곳에 놓을 파이프 찾기
                    pipe = find_pipe(ti + di[p], tj + dj[p])
                    return blank_i, blank_j, pipe

def find_moscow(row, col):
    for r in range(row):
        for c in range(col):
            if arr[r][c] == 'M':
                return r, c

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

# 시작지점인 모스크바(M) 찾기
sti, stj = find_moscow(R, C)

# 좌 하 우 상
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

# 가스 블록별 갈 수 있는 방향 k값 저장
# 시작지점은 4방향 다 봐야 하므로 start에 0~4 저장
gas_block = {
    'start': (0, 1, 2, 3), '|': (1, 3), '-': (0, 2), '+': (0, 1, 2, 3),
    '1': (1, 2), '2': (2, 3), '3': (0, 3), '4': (0, 1)
}

result_i, result_j, result_pipe = gas_pipe(sti, stj, 'start')
# 문제에서 인덱스 0번 행과 열을 1로 보고 있으므로 result i와 j의 값에 1 더해 출력
# result_pipe가 리스트로 반환되었으므로 *result_pipe
print(result_i+1, result_j+1, *result_pipe)