# 기능개발

def solution(progresses, speeds):
    answer = []
    days = []

    # 각 기능이 배포 가능해지기까지 걸리는 일수 계산
    for i in range(len(progresses)):
        d = (100 - progresses[i]) // speeds[i]       # 몫: 완전히 채워지는 일수
        if (100 - progresses[i]) % speeds[i] != 0:   # 나머지가 있으면 하루 더 필요 (올림)
            d += 1
        days.append(d)

    day = days[0]    # 현재 배포 묶음의 기준일 (묶음 안에서 가장 늦은 작업의 완료일)
    deploy = 1       # 현재 묶음에 포함된 기능 수 (첫 번째 기능 포함)

    for i in range(1, len(days)):
        if day >= days[i]:
            # 기준일 이내에 끝나는 작업 → 같은 날 함께 배포
            deploy += 1
        else:
            # 기준일보다 늦게 끝나는 작업 → 앞 묶음 확정, 새 묶음 시작
            answer.append(deploy)
            deploy = 1          # 새 기준 작업 자신이 첫 번째 원소
            day = days[i]       # 기준일 갱신

    answer.append(deploy)   # 마지막 묶음은 루프에서 추가되지 않으므로 따로 추가

    return answer

'''
import math

def solution(progresses, speeds):
    answer = []
    last_day = 0   # 현재 묶음의 배포 기준일

    # zip: 두 리스트를 같은 인덱스끼리 묶어서 (progresses[i], speeds[i]) 쌍으로 한 번에 꺼내줌
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)   # 이 기능의 완료 소요일 (올림)

        if answer and day <= last_day:
            # 앞 기능과 같은 날 배포 가능 → 마지막 묶음에 +1
            answer[-1] += 1
        else:
            # 새로운 배포일 → 새 묶음 생성
            answer.append(1)
            last_day = day

    return answer
'''