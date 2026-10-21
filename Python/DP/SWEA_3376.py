# 파도반 수열
# 삼각형이 나선 모양으로 늘어서 있는 처음에 이 나선은 한 변의 길이가 1인 정삼각형에서 시작한다.
# 현재 만들어진 나선에서 가장 긴 변에 그 변의 길이와 같은 크기의 정삼각형을 추가해 넣는다.
# 파도반 수열 P(N)은 나선에 N번째로 추가한 나선의 길이를 의미하는 수열
# N이 주어질 때 P(N)을 구하는 프로그램을 작성하라. (1 <= N <= 100)
memo = [-1] * 101

def padovan(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 3:
        memo[n] = 1
    else:
        memo[n] = padovan(n - 2) + padovan(n - 3)
    return memo[n]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {padovan(N)}')