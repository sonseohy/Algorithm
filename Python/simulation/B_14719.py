# 빗물
# 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
# 빗물이 전혀 고이지 않을 경우 0을 출력
# 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하자.
H, W = map(int, input().split())
block = list(map(int, input().split()))
start_idx = 0   # 빗물이 고이기 시작하는 블록 인덱스 저장 : 각 블록의 왼쪽에 해당하는 인덱스 저장
rainwater = 0
hole = []   # start_idx 보다 작은 블록의 높이 저장 (빗물이 고이는 지점이므로)

for k in range(1, len(block)):
    # start 블록 보다 높이가 높은 블록이 나왔을 때 : 지금까지 저장해둔 hole에 빗물이 고였을 것이므로 hole 높이 차를 rainwater에 저장
    if block[start_idx] <= block[k]:
        if len(hole):   # 이미 hole에 저장된 블록들이 있다면 반복을 통해 높이차만큼 빗물 저장
            for h in hole:
                rainwater += block[start_idx] - h
            hole = []   # 빗물 저장 후 hole 리스트 비움
        start_idx = k   # 빗물이 고이기 시작하는 블록 지점 start_idx을 k로 지정 (새로운 시작점 설정)
    else:
        hole.append(block[k])   # start_idx보다 작은 블록들은 hole에 저장

# hole에 저장된 블록들이 있다면 hole 리스트를 뒤에서부터 보면서 높이가 last보다 크면 last 갱신, 작으면 last와의 높이차만큼 빗물 저장
# 위에서 한 과정을 한번 더 해주는 방식
if len(hole) > 0:
    last = hole.pop()
    for idx in range(len(hole)-1, -1, -1):
        if last < hole[idx]:
            last = hole[idx]
        else:
            rainwater += last - hole[idx]
print(rainwater)