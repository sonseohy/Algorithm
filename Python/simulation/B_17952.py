# 과제는 끝나지 않아!
# 과제는 가장 최근에 나온 순서대로 한다. 또한 과제를 받으면 바로 시작한다.
# 과제를 하던 도중 새로운 과제가 나온다면, 하던 과제를 중단하고 새로운 과제를 진행
# 새로운 과제가 끝났다면, 이전에 하던 과제를 이전에 하던 부분부터 이어서 한다.
# 과제를 받자마자 이 과제가 몇 분이 걸릴지 정확하게 알 수 있고, 성애가 제출한 과제는 무조건 만점을 받는다.
# 이번 학기에 자기가 받을 과제 점수를 예상
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
homeworks = [list(map(int, input().split())) for _ in range(N)]

stack = deque()
score = 0
for i in range(N):
    # 새로운 과제가 나오지 않았을 때
    if homeworks[i][0] == 0 and len(stack):
        stack[-1][2] -= 1
        if stack[-1][2] == 0:
            hw = stack.pop()
            score += hw[1]
    # 새로운 과제가 나왔을 때
    elif homeworks[i][0] == 1:     # 오답(런타임 에러) 포인트 : else로 쓰면 과제가 나오지 않고 stack이 비었을 때도 else 코드가 실행되므로 elif문 써줘야 함
        homeworks[i][2] -= 1
        if homeworks[i][2]:
            stack.append(homeworks[i])
        else:
            score += homeworks[i][1]

print(score)
