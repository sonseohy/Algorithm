# 오픈채팅방

def solution(record):
    answer = []

    # 모든 record를 돌며 uid -> 최종 닉네임 확정
    nick_dict = {}
    for r in record:
        parts = r.split()

        if parts[0] != "Leave":
            nick_dict[parts[1]] = parts[2]

    # 최종 닉네임으로 메시지 생성
    for r in record:
        # [오답] `status, uid, name = r.split()`
        #   - Leave는 "Leave uid"로 단어가 2개뿐이라 3개로 언패킹하면 ValueError
        #   -> split() 결과를 리스트로 받고, 필요한 것만 꺼내 쓰기
        parts = r.split()
        status, uid = parts[0], parts[1]

        if status == "Enter":
            answer.append(f"{nick_dict[uid]}님이 들어왔습니다.")
        elif status == "Leave":
            answer.append(f"{nick_dict[uid]}님이 나갔습니다.")

        # [오답] 문제에서 Change는 메시지를 출력하지 않음

    return answer