"""
DFS 기본 코드

1. 탐색 시작 node를 스택에 삽입하고 방문처리
2. 스택의 최상단 node에 방문하지 않은 인접 node가 있으면 인접node를 스택에 넣고 방문처리
2-1. 방문하지 않은 인접node가 없으면 스택에서 최상단 노드를 꺼냄
3. 2번과정 반복
"""
def dfs(graph, start, visited) :
    visited[start] = True 
    print(start, end = ' ')

    for i in graph[start]:
        if not visited[i] :
            dfs(graph, i, visited)

# 보통 node는 1부터라서 index 0은 비워둠
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

dfs(graph, 1, visited)
