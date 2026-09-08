# ── 시간복잡도 ──
# dict/set 조회, 삽입, 삭제: 평균 O(1)
# list의 in, .index(): O(N)  ← 반복문 안에서 쓰면 전체 O(N^2)
# 그래서 반복 조회가 필요하면 list 대신 dict/set 사용

def solution(participant, completion):
    answer = ''
    hash_dict = {}

# ── dict.get(key, default) ──
# 딕셔너리에서 값을 안전하게 조회
# key: 찾을 키 / default: 키 없을 때 반환할 값
# default를 안 쓰면 None 반환 (에러 X)
# d[key]는 키 없으면 KeyError, get은 에러 없이 default(또는 None) 반환

    # participant 이름별 등장 횟수 카운트
    for name in participant:
        hash_dict[name] = hash_dict.get(name, 0) + 1

    # completion에서 하나씩 빼기
    for name in completion:
        hash_dict[name] -= 1

# ── dict.items() ──
# (키, 값) 쌍으로 순회
# 키만: d.keys() / 값만: d.values()

    # 값이 남아있는 사람이 완주 못한 사람
    for name, count in hash_dict.items():
        if count != 0:
            answer = name

    return answer
