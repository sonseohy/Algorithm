# [모의 SW 역량테스트] 디저트 카페
# 한 변의 길이가 N인 정사각형 모양을 가진 지역에 디저트 카페가 모여 있다.
# 원 안의 숫자는 해당 디저트 카페에서 팔고 있는 디저트의 종류를 의미하고, 카페들 사이에는 대각선 방향으로 움직일 수 있는 길들이 있다.
# 디저트 카페 투어는 어느 한 카페에서 출발하여 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다.
# 1. 카페 투어를 하는 도중 해당 지역을 벗어나면 안 되며, 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 된다.
# 2. 하나의 카페에서 디저트를 먹는 것도 안 되며, 왔던 길을 다시 돌아가는 것도 안 된다.
# 디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때의 디저트 수를 정답으로 출력하는 프로그램을 작성
# 만약, 디저트를 먹을 수 없는 경우 -1을 출력
def tour(num):
    cafe_lst = []
    cnt = 0

    for i in range((N-2-num)**2*(2**(num!=0))): # num이 0일 때(한칸씩 상하좌우 확인할 때)는 2를 곱해주면 안되고 num이 0이 아니면 2를 곱해줘야 하므로 2**(num!=0)
        if cnt == 4+(num*2):
            return cnt
        
        cur_i = i // (N-2) + 1
        cur_j = i % (N-2) + 1

        for k in range(num+1):
            cur_i += cross[k-1]
            cur_j += cross[k-1]
            for di, dj in move:
                ni, nj = di+cur_i, dj+cur_j
                if cafe[ni][nj] in cafe_lst:
                    break
                if cafe[ni][nj] not in cafe_lst and visited[ni][nj] == 0:
                    cafe_lst.append(cafe[ni][nj])
                    visited[ni][nj] = 1
                    cnt += 1


    return -1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    move = [(0,1), (1,0), (0,-1), (-1, 0)]
    cross = [(1,1), (1,-1)]
    for i in range(N-2):
        visited = [[0]*N for _ in range(N)]
        dessert = tour(i)
        result = max(dessert, result)
    
    print(f'#{tc} {result}')

                
# 시도 1. 수학적 규칙 찾아 접근 (미완성)
"""
def tour(num):
    cafe_lst = []
    cnt = 0

    for i in range((N-2-num)**2*(2**(num!=0))): # num이 0일 때(한칸씩 상하좌우 확인할 때)는 2를 곱해주면 안되고 num이 0이 아니면 2를 곱해줘야 하므로 2**(num!=0)
        if cnt == 4+(num*2):
            return cnt
        
        cur_i = i // (N-2) + 1
        cur_j = i % (N-2) + 1

        for di, dj in move:
            ni, nj = di+cur_i, dj+cur_j
            if cafe[ni][nj] in cafe_lst:
                break
            if cafe[ni][nj] not in cafe_lst and visited[ni][nj] == 0:
                cafe_lst.append(cafe[ni][nj])
                visited[ni][nj] = 1
                cnt += 1


    return -1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    move = [(0,1), (1,0), (0,-1), (-1, 0)]
    cross = [(1,1), (1,-1)]
    for i in range(N-2):
        visited = [[0]*N for _ in range(N)]
        dessert = tour(i)
        result = max(dessert, result)
    
    print(f'#{tc} {result}')
"""