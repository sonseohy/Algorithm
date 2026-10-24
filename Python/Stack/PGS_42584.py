# 주식 가격
def solution(prices):
    n = len(prices)
    answer = [0] * n   # 각 시점별로 가격이 떨어지지 않은 기간
    stack = []         # 아직 가격이 떨어지지 않은 시점(인덱스)을 담는 스택

    for i, price in enumerate(prices):
        # 현재 가격이 스택 top 시점의 가격보다 낮아졌다면
        # 그 시점은 i 시점에 처음으로 가격이 떨어진 것
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j   # j 시점부터 i 시점까지 유지된 기간

        # 현재 시점은 아직 가격이 떨어지지 않았으므로 스택에 추가
        stack.append(i)

    # 반복문이 끝난 뒤에도 스택에 남은 시점들은
    # 끝까지 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = (n - 1) - j   # 마지막 시점까지의 기간

    return answer

# 내 풀이 : O(N^2)
'''
def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
        
    return answer
'''