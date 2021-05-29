#DFS Basic, recursive

def dfs(graph, v, visited):
    visited[v]=True 
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

graph=[
    [], #인덱스 1번부터 시작되기 때문에 node 0은 비워둠
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited=[False]*9 #처음에는 모든 노드를 방문하지 않음(초기화), 인덱스 0번도 false로 초기화

dfs(graph, 1, visited)