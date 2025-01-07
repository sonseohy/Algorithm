# 주식
# 홍준이는 매일 1. 주식을 하나 산다, 2. 원하는만큼 가지고 있는 주식을 판다, 3. 아무것도 안한다. 3가지 중 한 행동을 한다.
# 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산

# 뒤에서부터 하는 것이 시간 줄일 수 있음
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    STOCK = list(map(int, input().split()))

    max_v = STOCK[N-1]
    buy = []
    result = 0
    for i in range(N-2, -1, -1):
        if STOCK[i] < max_v:
            result += max_v - STOCK[i]
        else:
            max_v = STOCK[i]

    print(result)

# 시도1. 시간초과
# import sys
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     STOCK = list(map(int, input().split())) + [0]

#     max_v = max(STOCK)
#     buy = []
#     result = 0
#     for i in range(N):
#         if STOCK[i] >= max_v:
#             for v in buy:
#                 result += max_v - v
#             max_v = max(STOCK[i+1:])
#             buy = []
#         elif STOCK[i] <= max_v:
#             buy.append(STOCK[i])
#         else:
#             result = 0
#             break

#     print(result)