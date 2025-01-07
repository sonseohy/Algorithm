# 선수과목
from collections import deque

def topology_sort():    # 위상 정렬
    result = [0] * (N+1)    # 최소 학기 저장
    dq = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:    # 들어오는 간선 수가 0인 정점을 큐에 append
            dq.append(i)    
            result[i] = 1       # 선수 과목이 없는 과목이므로 최소 학기를 1로 저장

    while dq:
        next = dq.popleft()     # 정점을 하나 꺼내서
        for i in graph[next]:   # 정점에 연결된 모든 정점 i의 간선 수 감소
            indegree[i] -= 1
            result[i] = result[next]+1  # 이전 과목의 최소학기에 1을 더해 최소 학기를 갱신
            if indegree[i] == 0:    # 들어오는 간선 수가 0이 되면 큐에 append
                dq.append(i)
    
    return result[1:]

N, M = map(int, input().split())
indegree = [0] * (N+1)      # 들어오는 간선 수 저장
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

print(*topology_sort())
