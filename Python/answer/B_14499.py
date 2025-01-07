# 주사위 굴리기 답 (문어박사)
N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

n1 = n2 = n3 = n4 = n5 = n6 = 0     # 주사위 면 0으로 초기화화
di, dj = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
result = []

for d in lst:
    ni, nj = x + di[d], y + dj[d]
    if 0 <= ni < N and 0 <= nj < M:
        if d == 1:       # 동
            n1,n3,n4,n6 = n4,n1,n6,n3
        elif d == 2:     # 서
            n1,n3,n4,n6 = n3,n6,n1,n4
        elif d == 3:     # 북
            n1,n2,n5,n6 = n5,n1,n6,n2
        else:           # 남
            n1,n2,n5,n6 = n2,n6,n1,n5

        # 이동한 바닥판이 0인지 체크크
        if arr[ni][nj] == 0:
            arr[ni][nj] = n6
        else:
            n6, arr[ni][nj] = arr[ni][nj],0

        result.append(n1) # 윗면의 값을 ans에 추가
        x, y = ni,nj

for ans in result:
    print(ans)