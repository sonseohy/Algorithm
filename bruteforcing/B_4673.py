# 셀프 넘버
# 양의 정수 n에 대해서 d(n) = n + n의 각 자리수
# n, d(n), d(d(N)) ... 과 같이 무한 수열 만들 수 있음
# n을 d(n)의 생성자라고 함
# 생성자가 없는 숫자를 셀프 넘버라고 함
# 출력 : 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력

creator_num = []
n = 1
while n <= 10000:
    sum_v = n   # 처음 sum_v에 n 저장
    n = str(n)
    for i in range(len(n)):
        sum_v += int(n[i])  # n의 각 자리수 합 sum_v에 더해줌
    creator_num.append(sum_v)   # 생성자 배열에 sum_v 값 저장

    n = int(n)
    n += 1


for i in range(1, 10001):
    if i not in creator_num:    # creator_num 배열에 없는 숫자가 셀프 넘버이므로 creator_num에 없는 숫자만 출력
        print(i)