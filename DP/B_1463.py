# 1로 만들기 (미완)
# 정수 x에 사용할 수 있는 연산은 3가지
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값 출력

def one(n, cnt):
    global result

    if n == 1:
        result = min(cnt, result)
        return memo[n]


    if n > 1 and memo[n] == 0:
        memo[n] = one(n-1, cnt+1)
    
    if n % 2 == 0 and memo[n] == 0:
        memo[n] = one(n//2, cnt+1)
    
    if n % 3 == 0 and memo[n] == 0:
        memo[n] = one(n//3, cnt+1)

    return memo[n]
        
N = int(input())
memo = [0] * (N+1)
result = 1e6 + 1
one(N, 0)
print(result)