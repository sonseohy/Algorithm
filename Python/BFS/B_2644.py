# 촌수계산
# 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산
# 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.
# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성
from collections import deque

def bfs(s, v):
    queue = deque()
    queue.append((s, 0))
    visited = [0]*(N+1)
    visited[s] = 1
    
    while queue:
        t, cnt = queue.popleft()

        if t == v:
            return cnt

        for w in graph[t]:
            if visited[w] == 0:
                queue.append((w, cnt+1))
                visited[w]= 1

    return -1
        

N = int(input())
p1, p2 = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(p1, p2))