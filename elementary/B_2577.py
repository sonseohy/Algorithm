# 숫자의 개수
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하기

A = int(input())
B = int(input())
C = int(input())

calculate = A * B * C
num = str(calculate)
counts = [0]*10

for n in num:
    counts[int(n)] += 1

for c in counts:
    print(c)