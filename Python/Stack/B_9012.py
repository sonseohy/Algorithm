# 괄호
# 괄호 문자열(PS)은 두 개의 괄호 기호 '(', ')' 만으로 구성되어 있는 문자열
# 그 중 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(VPS)이라고 부름
# 한 쌍의 괄호 기호로 된 "()" 문자열은 기본 VPS
# 만일 x가 VPS라면 하나의 괄호에 넣은 새로운 문자열 "(x)"도 VPS가 된다.
# 두 VPS x와 y를 접합시킨 새로운 문자열 xy도 VPS가 된다.
# 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 함

def check_vpn(lst, size):   # ( 는 항상 stack에 저장, )는 항상 pop 해서 왼쪽괄호가 있는지 확인
    stack = []

    for i in range(size):
        if lst[i] == '(':
            stack.append(lst[i])
        if lst[i] == ')':
            if len(stack) == 0: # stack에 괄호가 없을 때
                return 'NO'
            stack.pop()
    if len(stack):  # stack에 괄호가 남아있을 때
        return 'NO'
    return 'YES'
        

T = int(input())
VPS = [list(input()) for _ in range(T)]

for v in VPS:
    print(check_vpn(v, len(v)))