# 헌내기는 친구가 필요해
# 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동
# 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력
# O는 빈 공간, X는 벽, I는 도연이, P는 사람. I가 한 번만 주어짐이 보장
from collections import deque

def find_person(sti, stj):
    global cnt
    visited = [[0]*M for _ in range(N)]
    visited[sti][stj] = 1
    dq = deque()
    dq.append([sti, stj])

    while dq:
        ti, tj = dq.popleft()
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and CAMPUS[ni][nj] != 'X':
                dq.append([ni, nj])
                visited[ni][nj] = 1
                if CAMPUS[ni][nj] == 'P':
                    cnt += 1

N, M = map(int, input().split())
CAMPUS = [list(input()) for _ in range(N)]

cnt = 0
for r in range(N):
    for c in range(M):
        if CAMPUS[r][c] == 'I':
            find_person(r, c)
if cnt:
    print(cnt)
else:
    print('TT')