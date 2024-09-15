# 블랙잭
# 카드 합이 21을 넘지 않는 한도 내에서, 카드 합을 최대한 크게 만드는 게임
# 각 카드에 양의 정수가 쓰여있고, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓음
# 그런 후 딜러는 숫자 M을 크게 외침
# 플레이어는 제한된 시간 안에 N장의 카드 중 3장의 카드 골라야 함
# 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 함
# 출력 : M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합

# 카드의 합을 계산해야 하므로 sum_v 같이 넘겨줌
def blackjack(card_num, sum_v):
    global max_v
    # 가지치기 : 카드 합이 M을 넘어가면 더이상 보지 않음
    if sum_v > M:
        return

    # 기저 조건 : 카드를 3장 뽑으면 return
    if card_num == 3:
        max_v = max(max_v, sum_v)
        return
    
    # 후보군 : 카드 개수 N
    for i in range(N):
        if used[i] == 1:
            continue
        used[i] = 1
        blackjack(card_num + 1, sum_v + CARDS[i])
        used[i] = 0


N, M = map(int, input().split())
CARDS = list(map(int, input().split()))

max_v = 0   # 합이 M을 넘지 않으면서 M에 최대한 가까운 카드 합 저장할 변수
used = [0] * N
blackjack(0, 0)

print(max_v)