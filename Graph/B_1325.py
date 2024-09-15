# 효율적인 해킹
# 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다
# 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력

# 시간초과 : 해결 실패..
def hacking(node, idx):
    global max_cnt, result
    q = []
    q.append(node)
    cnt = 0

    while q:
        t = q.pop(0)
        cnt += 1
        if t == []:
            cnt -= 1
            if max_cnt == cnt:
                result.append(idx)
            elif max_cnt < cnt:
                max_cnt = cnt
                result = []
                result.append(idx)

        else:
            for n in t:
                q.append(graph[n])

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

max_cnt = 0
result = []
for i in range(1, N+1):
    if len(graph[i]) > 0:
        hacking(graph[i], i)

print(*set(result))

##########################
# GPT 수정
from collections import deque

def bfs(start_node):
    # BFS를 수행하는 함수
    queue = deque()
    queue.append(start_node)  # 시작 노드를 큐에 추가
    visited = [0] * (N + 1)  # 노드 방문 여부를 체크하는 리스트
    visited[start_node] = 1  # 시작 노드를 방문한 것으로 표시
    cnt = 0  # 방문한 노드의 개수 카운트

    while queue:
        node = queue.popleft()  # 큐에서 노드를 꺼냄
        cnt += 1  # 노드를 방문했으므로 카운트 증가
        for neighbor in graph[node]:  # 현재 노드의 모든 이웃 노드에 대해
            if visited[neighbor] == 0:  # 이웃 노드를 방문하지 않은 경우
                visited[neighbor] = 1  # 이웃 노드를 방문한 것으로 표시
                queue.append(neighbor)  # 이웃 노드를 큐에 추가

    return cnt  # 총 방문한 노드의 개수를 반환

# 입력을 읽어들임
N, M = map(int, input().split())  # N: 노드의 수, M: 간선의 수
graph = [[] for _ in range(N + 1)]  # 그래프 초기화 (인덱스 1부터 N까지)

# 간선 정보를 그래프에 추가
for _ in range(M):
    A, B = map(int, input().split())  # A에서 B로 가는 간선
    graph[B].append(A)  # 역방향 그래프를 저장

max_cnt = 0  # 최대 방문한 노드의 개수
result = []  # 최대 방문한 노드를 가진 노드들의 리스트

# 각 노드에 대해 BFS를 수행
for i in range(1, N + 1):
    if graph[i]:  # 노드 i에 연결된 간선이 있는 경우
        cnt = bfs(i)  # 노드 i를 시작으로 BFS 수행
        if cnt > max_cnt:  # 방문한 노드의 개수가 최대값을 초과하는 경우
            max_cnt = cnt  # 최대값 갱신
            result = [i]  # 결과 리스트를 현재 노드로 초기화
        elif cnt == max_cnt:  # 방문한 노드의 개수가 현재 최대값과 같은 경우
            result.append(i)  # 결과 리스트에 현재 노드를 추가

# 결과를 출력 (최대 방문 노드 수를 가진 노드들을 출력)
print(*result)
