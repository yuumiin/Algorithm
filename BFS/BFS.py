"""
BFS 기본 코드

1. 탐색 시작 node를 큐에 삽입하고 방문 처리
2. 큐에서 node를 꺼내 해당node의 인접node 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
3. 2번 과정 반복
"""

from collections import deque

def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[True]

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)