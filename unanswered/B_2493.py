# 탑
# 직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고, 각 탑의 꼭대기에 레이저 송신기를 설치
# 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능
# 탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램

# GPT
N = int(input())
TOWER = list(map(int, input().split()))
receive = [0] * N
stack = []

for i in range(N):
    while stack and TOWER[stack[-1]] < TOWER[i]:
        stack.pop()
    if stack:
        receive[i] = stack[-1] + 1
    stack.append(i)

print(*receive)




"""
# 시도1. 시간초과
N = int(input())
TOWER = list(map(int, input().split()))
receive = [0] * N
top = N - 1
i = 0

while top > -1:
    laser = N-1-i
    top -= 1
    if TOWER[laser] < TOWER[top]:
        receive[laser] = top + 1
        TOWER.pop()
        i += 1
        top = N - 1 - i
        continue

    if top == 0:
        i += 1
        top = N - 1 - i

print(*receive)


# GPT 코드
# 입력값을 받습니다. N은 타워의 개수입니다.
N = int(input())
# TOWER 리스트에 각 타워의 높이를 저장합니다.
TOWER = list(map(int, input().split()))
# 각 타워가 수신한 레이저를 발사한 타워의 인덱스를 저장할 리스트입니다.
receive = [0] * N
# 타워의 인덱스를 저장할 스택입니다.
stack = []

# 각 타워를 순회합니다.
for i in range(N):
    # 현재 타워의 높이(TOWER[i])보다 낮은 타워들을 스택에서 제거합니다.
    while stack and TOWER[stack[-1]] < TOWER[i]:
        stack.pop()
    
    # 스택이 비어있지 않다면, 스택의 최상단 인덱스가 현재 타워의 레이저를 발사한 타워입니다.
    if stack:
        receive[i] = stack[-1] + 1  # 타워의 인덱스를 1 기반으로 변환하여 저장합니다.
    
    # 현재 타워의 인덱스를 스택에 추가합니다.
    stack.append(i)

# 최종 결과를 공백으로 구분하여 출력합니다.
print(*receive)

"""