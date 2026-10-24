# 올바른 괄호

def solution(s):
    answer = True
    
    stack = []
    for c in s:
        if c == '(':
            stack.append(str)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
                
    if stack:
        answer = False

    return answer

'''
def solution(s):
    # 현재 열려 있는(아직 짝을 못 찾은) '(' 의 개수
    count = 0

    for ch in s:
        if ch == '(':
            # 여는 괄호: 짝을 기다리는 '('가 하나 늘어남
            count += 1
        else:
            # 닫는 괄호: 짝을 기다리던 '(' 하나와 매칭되어 하나 줄어듦
            count -= 1

            # 짝지을 '('가 없는데 ')'가 나온 경우
            # 예: ")(" 처럼 닫는 괄호가 먼저 나오면 바로 잘못된 괄호
            if count < 0:
                return False

    # 끝까지 돌았을 때 count가 0이어야 모든 '('가 짝을 찾은 것
    # 0보다 크면 짝을 못 찾은 '('가 남아 있다는 뜻 (예: "(()")
    return count == 0
'''