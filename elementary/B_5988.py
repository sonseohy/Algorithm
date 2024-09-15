# 홀수일까 짝수일까
# N개의 정수가 주어지면 홀수인지 짝수인지를 출력

N = int(input())
for _ in range(N):
    number = int(input())
    if number % 2 == 0:
        print('even')
    else:
        print('odd')