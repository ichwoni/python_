#DFS Basic, recursive, dictionary

def dfs(graph, v, visited):
    #visited[v]=True 
    visited.append(v)
    print(v, end=' ')

    for i in graph[v]:
        if i not in visited:
            dfs(graph, i , visited)
    

graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

visited=[] #처음에는 모든 노드를 방문하지 않음(초기화), 인덱스 0번도 false로 초기화

dfs(graph, 'A', visited)