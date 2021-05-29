#BFS

from collections import deque

def bfs(graph, start, visited):
    queue=deque([start]) #start를 큐에 먼저 넣은 큐 생성
    visited[start]=True #start 노드 방문 처리

    while queue: #큐가 빌 때까지 반복
        v=queue.popleft() #일단 하나 뽑고(방문한)
        print(v, end=' ') #출력

        for i in graph[v]:
            if not visited[i]: #그래프에서 이전 노드의 인접 노드들 중 방문 안 한 게 있으면
                queue.append(i) #큐에 넣고
                visited[i]=True #방문 처리


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

visited=[False]*9

bfs(graph, 1, visited)