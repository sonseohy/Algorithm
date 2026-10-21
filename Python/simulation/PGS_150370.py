# 개인정보 수집 유효기간

# 총 일수 (정수)
def to_days(date_str):
    # 모든 달이 28일이라서 연/월/일을 하나의 정수로 환산 가능
    year, month, day = list(map(int, date_str.split('.')))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []

    # 약관 종류별 유효기간(개월)을 딕셔너리로 저장
    term_dict = {}
    for term in terms:
        c, d = term.split()
        term_dict[c] = int(d)   # 문자열 정수 변환
    
    # today -> 일수
    day = to_days(today)

    # 날짜/종류 분리 -> 수집일 일수 + 개월수 * 28
    for i, privacy in enumerate(privacies, 1):
        date, cond = privacy.split()

        # 만료일(일수) = 수집일(일수) + 유효기간(개월) * 28
        # 월/연도 넘김 처리가 필요 없는 게 일수 환산의 장점
        expire = to_days(date) + term_dict[cond] * 28

        # 파기 대상 판단: 만료일 "다음 날"부터 파기
        # to_days(today)는 만료 시작일이 계산되어 나오므로 <=
        if expire <= to_days(today):
            answer.append(i)

    return answer