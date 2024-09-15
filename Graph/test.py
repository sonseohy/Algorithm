from collections import deque

def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited = [0] * (N+1)
    visited[start_node] = 1
    cnt = 0

    while queue:
        node = queue.popleft()
        cnt += 1
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                queue.append(neighbor)

    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

max_cnt = 0
result = []

for i in range(1, N + 1):
    if graph[i]:  # 노드 i에 연결된 엣지가 있는 경우
        cnt = bfs(i)
        if cnt > max_cnt:
            max_cnt = cnt
            result = [i]
        elif cnt == max_cnt:
            result.append(i)

print(*result)
