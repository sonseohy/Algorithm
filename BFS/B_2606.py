# 바이러스
# 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결된 모든 컴퓨터도 바이러스에 걸림
# 컴퓨터의 수 : 100 이하 양의 정수
# 출력 : 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수
def BFS(s):
    visited = [0] * (COM+1)
    visited[s] = 1
    queue = []
    queue.append(s)
    cnt = 0

    while queue:
        t = queue.pop(0)

        for w in graph[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1
                cnt += 1
    return cnt

COM = int(input())
PAIR = int(input())
graph = [[] for _ in range(COM+1)]
for _ in range(PAIR):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(BFS(1))