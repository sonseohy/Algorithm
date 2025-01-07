# 한수
# 어떤 양의 정수 X의 각 자리가 등차수열을 이루면 그 수는 한수
# 등차수열이란 연속된 두개의 수의 차가 일정한 수열
# 1 <= 한수 <= N인 한수 개수 출력

N = int(input())
result = 0

for i in range(1, N+1):
    cnt = 0
    if i < 10:  # i가 한자리수이면 cnt += 1
        cnt += 1
    else:       # i가 두자리수 이상일 때
        num = str(i)    # i를 문자열로 변환해 num에 저장
        difference = int(num[1]) - int(num[0])  # 앞의 두 숫자 차이를 difference에 저장
        for j in range(1, len(num)):
            if int(num[j]) - int(num[j-1]) == difference:   # 각 자리의 차가 difference와 같은지 확인해 등차수열 여부 확인
                cnt = 1
            else:   # 하나라도 difference만큼의 차이를 보이지 않으면 등차수열이 아니므로 cnt 0으로 초기화 후 break
                cnt = 0
                break
    result += cnt   # 숫자 i에 대해 등차수열 판단이 끝나면 cnt를 result에 저장

print(result)
