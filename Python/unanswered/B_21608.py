# 상어 초등학교
# 상어 초등학교에는 교실이 하나 있고, 교실은 N×N 크기의 격자로 나타낼 수 있다. 학교에 다니는 학생의 수는 N^2명이다.
# 교실의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다.
# 선생님은 학생의 순서를 정했고, 각 학생이 좋아하는 학생 4명도 모두 조사했다. 이제 다음과 같은 규칙을 이용해 정해진 순서대로 학생의 자리를 정하려고 한다.
# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
# 자리 배치가 모두 끝난 후 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해 학생의 만족도를 구해야 한다. 
# 인접한 칸에 좋아하는 학생의 수가 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
def like_seat(student, person):
    pos_seat = set()
    for r in range(N):
        for c in range(N):
            if space[r][c] in like[student]:
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = di + r, dj + c
                    if 0 <= ni < N and 0 <= nj < N and space[ni][nj] == 0:
                        pos_seat.add((ni, nj))
    
    if len(pos_seat) == 0:
        # 아무 자리도 배정되지 않았을 때
        if person:
            for r in range(N):
                for c in range(N):
                    check = 0
                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ni, nj = di + r, dj + c
                        if 0 <= ni < N and 0 <= nj < N:
                            check += 1
                    if check == 4:
                        space[r][c] = student
                        return False
        # 이미 자리에 배정된 사람이 있으나 앉은 사람들 중 선호하는 사람이 없을 때
        # 빈칸이 많은 곳 중 행 값이 작고 열 값이 작은 곳에 배정
        else:
            max_blank = 0
            bi = -1
            bj = -1
            for r in range(N):
                for c in range(N):
                    if space[r][c] == 0:
                        blank = 0
                        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                            ni, nj = di + r, dj + c
                            if 0 <= ni < N and 0 <= nj < N and space[ni][nj] == 0:
                                blank += 1
                        if max_blank < blank:
                            max_blank = blank
                            bi = r
                            bj = c
                        elif max_blank == blank and bi == -1:
                            bi = r
                            bj = c
            space[bi][bj] = student
            return False

    return pos_seat

def assign_seat(lst, student):
    max_blank = 0
    max_like_person = 0
    spot = []

    for ti, tj in lst:
        blank_cnt = 0
        like_person = 0
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = di + ti, dj + tj
            if 0 <= ni < N and 0 <= nj < N and space[ni][nj] == 0:
                blank_cnt += 1
            elif 0 <= ni < N and 0 <= nj < N and space[ni][nj] in like[student]:
                like_person += 1
        if max_like_person < like_person:
            max_like_person = like_person
            max_blank = blank_cnt
            spot = []
            spot.append((ti, tj))
        elif max_like_person == like_person:       
            if max_blank < blank_cnt:
                max_blank = blank_cnt
                spot = []
                spot.append((ti, tj))
            elif max_blank == blank_cnt:
                spot.append((ti, tj))

    ti, tj = spot.pop(0)
    if len(spot):
        for spot_i, spot_j in spot:
            if ti > spot_i or (ti == spot_i and tj > spot_j):
                ti, tj = spot_i, spot_j
                break
    
    space[ti][tj] = student


N = int(input())
like = [[] for _ in range(N*N + 1)]
space = [[0]*N for _ in range(N)]
'''
for _ in range(N*N):
    num, *lst = map(int, input().split())     # 첫번째 들어오는 값은 학생 번호, 나머지는 그 학생이 좋아하는 학생 번호
    like[num].extend(lst)   # extend : 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣는다. (append로 넣으면 리스트로 두번 감싸져서 저장되는데 extend는 iterable 모든 항목을 만들어진 리스트에 저장 가능)
'''

no_person = True    # 아무도 자리 배정을 하지 않은 상태를 True로 정의
for _ in range(N*N):
    num, *lst = map(int, input().split())
    like[num].extend(lst)
    seat_lst = like_seat(num, no_person)
    if seat_lst:
        assign_seat(seat_lst, num)
    no_person = False
    print("----------")
    for test in range(N):
        print(*space[test])

# 학생의 만족도 총합 구하기
result = 0
for i in range(N):
    for j in range(N):
        satisfy = 0
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = di + i, dj + j
            if 0 <= ni < N and 0 <= nj < N and space[ni][nj] in like[space[i][j]]:
                satisfy += 1
        if satisfy == 1:
            result += 1
        elif satisfy == 2:
            result += 10
        elif satisfy == 3:
            result += 100
        elif satisfy == 4:
            result += 1000

print(result)
    