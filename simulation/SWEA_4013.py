# [모의 SW 역량테스트] 특이한 자석
# N극 = 0, S극 = 1, 시계방향 : 1, 반시계방향 : -1
# 점수 : N극이면 0점, S극이면 1번 1점, 2번 2점, 3번 4점, 4번 8점
# 화살표 위치 인덱스 : 0, 오른쪽 90도 인덱스 : 2, 왼쪽 90도 인덱스 : 6
# 서로 붙어있는 날의 자성이 다를 경우 회전

# 회전 : 시계방향이면 뒤에서 빼서 앞에 넣어줌, 반시계 방향이면 앞에서 빼서 뒤에 넣어줌
def rotate(mag, direction):
    if direction == 1:
        v = GEARS[mag - 1].pop()
        GEARS[mag-1].insert(0, v)
    elif direction == -1:
        v = GEARS[mag - 1].pop(0)
        GEARS[mag - 1].append(v)

def move_gear(n, d):
    # 자석이 서로 붙은 날의 자성이 같은지 다른지 저장 (자석이 맞닿아 있는 3부분을 차례로 상태 저장)
    state = [0, 0, 0]
    # 자석이 서로 붙어 있는 날의 자성 확인
    for g in range(3):
        if GEARS[g][2] != GEARS[g+1][6]:
            state[g] = True # 회전해야 하면 (자성이 다르면) True

    # 자석별로 회전시킬 자석 순서를 딕셔너리 값으로 저장
    # 회전할 자석이 1 : 오른쪽으로 쭉 보기, 4 : 왼쪽으로 쭉 보기
    # 회전할 자석이 2 : 왼쪽 한번, 오른쪽 두번, 3 : 왼쪽 두번, 오른쪽 한번
    check_mag = {'1': (2, 3, 4), '2': (1, 3, 4), '3': (4, 2, 1), '4': (3, 2, 1)}

    # 회전할 자석 회전
    rotate(n, d)

    # 남은 자석 회전
    i = 0   # state idx 저장
    # 회전 여부 확인
    rotate_lst = [0, 0, 0, 0, 0]
    rotate_lst[n] = 1
    for check in check_mag[str(n)]:
        # check가 돌아야 할 방향 계산
        if check % 2 == n % 2:
            dir = d
        else:
            dir = -d
        
        # 1, 2는 state를 앞에서부터 차례로 보고, 3, 4는 state를 뒤에서부터 차례로 봄
        if (n == 1 or n == 2) and state[i]:
            if n == 2 and state == [0, 0, True]:    # 예외 경우1 : 돌려야 할 자석이 2인데 양 옆(1, 3) 자석이 자성이 같아 돌릴 필요 없으면 하나 남은 자석 4가 True이더라도 돌리지 않아야 함
                break
            rotate(check, dir)
            if n == 2 and state == [True, 0, True]: # 예외 경우2 : 돌려할 자석이 2인데 왼쪽(1)은 돌리고 오른쪽은 자성이 같아 돌릴 필요 없으면 하나 남은 자석 4가 True이더라도 돌리지 않아야 함, 따라서 state 0번은 True니까 돌리고 이후 돌리지 않아도 되므로 break해서 반복 종료
                break
        elif (n == 3 or n == 4) and state[2-i]:
            if n == 3 and state == [True, 0, 0]:    # 예외 경우1 : 돌려야 할 자석이 3인데 양 옆(2, 4) 자석이 자성이 같아 돌릴 필요 없으면 하나 남은 자석 1이 True이더라도 돌리지 않아야 함
                break
            rotate(check, dir)
            if n == 3 and state == [True, 0, True]: # 예외 경우2
                break
        else:
            if (n == 2 and rotate_lst[3] == 0) or (n == 3 and rotate_lst[2] == 0):  # 
                i += 1
                continue
            break
        rotate_lst[check] = 1   # 회전한 자석 체크
        i += 1



T = int(input())

for test_case in range(1, T+1):
    K = int(input())
    GEARS = [list(map(int, input().split())) for _ in range(4)]
    rotation = [list(map(int, input().split())) for _ in range(K)]

    for num, r in rotation:
        move_gear(num, r)

    result = 0
    # 점수 계산
    for i in range(4):
        if GEARS[i][0]:
            result += 2 ** i

    print(f'#{test_case} {result}')