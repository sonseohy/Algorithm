# 신고 결과 받기
def solution(id_list, report, k):
    # 1. 중복 신고 제거
    #    "신고자 피신고자" 쌍 단위로 중복을 없앱니다.
    #    같은 쌍이 여러 번 들어와도 1회로 처리됩니다.
    report = set(report)

    # 2. 피신고자별 신고 횟수 집계
    #    cnt = {피신고자: 신고받은 횟수} 형태의 딕셔너리
    cnt = {}
    for r in report:
        _, reported = r.split()                    # "신고자 피신고자"를 공백으로 나눔
        cnt[reported] = cnt.get(reported, 0) + 1   # 없으면 0으로 시작해서 +1

    # 3. 정지 대상 찾기
    #    신고 횟수가 k 이상인 유저를 집합에 담습니다.
    #    집합은 `in` 확인이 빠릅니다.
    stop = {user for user, c in cnt.items() if c >= k}

    # 4. 유저별 처리 결과 메일 수 초기화
    #    모든 유저를 0으로 시작해서, 메일을 받지 않은 유저도 결과에 포함되게 합니다.
    mail_cnt = {user: 0 for user in id_list}

    # 5. 메일 발송 횟수 집계
    #    각 신고 중 피신고자가 정지 대상이면, 신고자에게 메일 1회를 추가합니다.
    for r in report:
        reporter, reported = r.split()
        if reported in stop:
            mail_cnt[reporter] += 1

    # 6. id_list 순서대로 결과 반환
    return [mail_cnt[user] for user in id_list]

'''
def solution(id_list, report, k):
    # 결과를 담을 리스트. id_list 순서대로 0으로 초기화
    answer = [0] * len(id_list)

    # 유저별 신고당한 횟수를 담을 딕셔너리. 모든 유저를 0으로 시작
    reports = {x: 0 for x in id_list}

    # 중복 신고를 제거한 뒤, 신고당한 사람(split 후 두 번째 값)의 횟수를 1 증가
    for r in set(report):
        reports[r.split()[1]] += 1

    # 다시 중복 제거된 신고를 순회
    for r in set(report):
        # 신고당한 사람의 횟수가 k 이상이면 정지 대상
        if reports[r.split()[1]] >= k:
            # 신고한 사람(split 후 첫 번째 값)의 메일 수를 1 증가
            # id_list에서 신고자의 위치(index)를 찾아 answer의 같은 위치에 반영
            answer[id_list.index(r.split()[0])] += 1    # index(): 리스트에서 값이 처음 나오는 위치(인덱스)를 반환

    return answer
'''