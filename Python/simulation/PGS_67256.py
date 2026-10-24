# 키패드 누르기

def solution(numbers, hand):
    answer = ''  # 각 번호를 어느 손으로 눌렀는지 기록할 결과 문자열

    # 각 키의 (행, 열) 좌표. '*', '#'도 키로 포함해서 시작 위치를 같은 방식으로 다룬다
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]    # 무조건 왼손으로 누르는 키
    right = [3,6,9]   # 무조건 오른손으로 누르는 키

    # 엄지의 현재 위치를 "좌표"가 아니라 "키 이름"으로 저장
    lhand = '*'       # 왼손 시작 위치
    rhand = '#'       # 오른손 시작 위치

    for i in numbers:
        # 1, 4, 7: 왼손으로 누르고 왼손 위치 갱신
        if i in left:
            answer += 'L'
            lhand = i

        # 3, 6, 9: 오른손으로 누르고 오른손 위치 갱신
        elif i in right:
            answer += 'R'
            rhand = i

        # 2, 5, 8, 0: 두 엄지 중 더 가까운 손으로 누름
        else:
            curPos = key_dict[i]       # 누를 키의 좌표
            lPos = key_dict[lhand]     # 왼손 엄지의 현재 좌표
            rPos = key_dict[rhand]     # 오른손 엄지의 현재 좌표

            # 맨해튼 거리: |행 차이| + |열 차이|
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:          # 왼손이 더 가까우면 왼손
                answer += 'L'
                lhand = i
            elif ldist > rdist:        # 오른손이 더 가까우면 오른손
                answer += 'R'
                rhand = i
            else:                      # 거리가 같으면 주로 쓰는 손(hand)으로 누름
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer