# 설탕 배달
# 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 함
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있는데, 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성
# 상근이가 배달하는 봉지의 최소 개수를 출력, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력

# 시간초과
def sugar_delivery(kg, idx, cnt):
    global min_v

    if kg == N:
        min_v = min(cnt, min_v)
        return

    if kg > N:
        return

    if memo[kg] == 0:
        for k in [3, 5]:
            memo[idx] = sugar_delivery(kg+k, idx+1, cnt+1)
        return memo[idx]

N = int(input())
min_v = 5001    # 최소 개수
memo = [0] * 5000
sugar_delivery(0, 1, 0)
if min_v == 5001:
    print(-1)
else:
    print(min_v)

"""
# GPT
def sugar_delivery(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(N + 1):
        if dp[i] != float('inf'):
            if i + 3 <= N:
                dp[i + 3] = min(dp[i + 3], dp[i] + 1)
            if i + 5 <= N:
                dp[i + 5] = min(dp[i + 5], dp[i] + 1)

    return dp[N] if dp[N] != float('inf') else -1

N = int(input())

print(sugar_delivery(N))
"""