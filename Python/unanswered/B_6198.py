# 옥상 정원 꾸미기
# 빌딩 관리인들은 다른 빌딩의 옥상 정원을 벤치마킹 하고 싶어한다.
# 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.
# 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다
# 각 관리인들이 벤치마킹이 가능한 빌딩의 수의 합을 출력
N = int(input())
BUILDNIG = []
check = [True] * N

for n in range(N):
    b = int(input())
    BUILDNIG.append(b)
    if n > 0 and BUILDNIG[n-1] <= b:
        check[n-1] = False

result = 0
for i in range(N):
    if check[i]:
        result += 1
        
    





# 1. 시간초과
"""
def rooftop(idx):
    cnt = 0
    v = BUILDNIG[idx]
    for k in range(idx+1, N):
        if BUILDNIG[k] < v:
            cnt += 1
        else:
            return cnt

    return cnt


N = int(input())
BUILDNIG = [int(input()) for _ in range(N)]

result = 0
for i in range(N-1):
    result += rooftop(i)

print(result)
"""