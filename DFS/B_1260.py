# DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료
# 정점 번호는 1번부터 N번까지
from collections import deque

def dfs(s):
    stack = deque()
    stack.append(s)
    visited = [0] * (N+1)
    answer = []

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1
            answer.append(v)
            for w in range(len(graph[v])-1, -1, -1):
                if visited[graph[v][w]] == 0:
                    stack.append(graph[v][w])
    
    print(*answer)

def bfs(s):
    queue = deque()
    queue.append(s)
    visited = [0] * (N+1)
    visited[s] = 1
    answer = []
    answer.append(s)

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                answer.append(i)
    
    print(*answer)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)
bfs(V)