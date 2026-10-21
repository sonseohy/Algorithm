# 신규 아이디 추천

def solution(new_id):
    answer = ''
    # 1단계 : 소문자 치환
    answer = new_id.lower()

    # 2단계 : 허용 문자 외 제거
    # isalnum(): 문자가 알파벳 또는 숫자면 True, 아니면 False
    answer = ''.join(c for c in answer if c.isalnum() or c in '-_.')

    # 3단계 : 마침표 2번 이상 연속 하나로 치환
    # [오답] x in y : x가 y 안에 있는지
    # replace(a, b): 문자열 속 a를 모두 b로 바꾼 새 문자열을 돌려준다(원본은 그대로).
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 4단계 : 처음이나 끝 마침표 제거
    # strip('.'): 문자열 맨 앞뒤의 .을 연속으로 모두 제거하고, 중간은 건드리지 않는다.
    answer = answer.strip('.')

    # 5단계 : 빈 문자열은 'a' 대입
    if answer == '':
        answer += 'a'

    # 6단계 : 길이가 16자 이상이면 앞 15자 이후 제거
    # [오답] 자른 뒤 끝이 '.' 이면 한 번 더 제거해야 함
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')

    # 7단계 : 길이가 2자 이하면 마지막 문자를 길이 3까지 반복
    while len(answer) < 3:
        answer += answer[-1]    
    
    return answer