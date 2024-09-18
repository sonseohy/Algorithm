# 스택
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    if top == -1:
        return -1
    top -= 1
    return stack[top+1]

N = int(input())
command = [list(input().split()) for _ in range(N)]

size = N
stack = [0] * size
top = -1

for c in command:
    if c[0] == 'push':
        push(int(c[1]))
    elif c[0] == 'pop':
        print(pop())
    elif c[0] == 'size':    # size는 스택에 들어있는 정수의 개수므로 top이 stack의 인덱스를 저장하고 있으므로 top + 1 이 스택의 개수
        print(top+1)
    elif c[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])