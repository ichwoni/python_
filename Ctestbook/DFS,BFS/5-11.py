from collections import deque

n,m=map(int, input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

#방향 설정해주기 ** 미로탈출,, 어디로 가는 거 등등 이런 거는 방향 설정이 기본이라고 생각
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque() #큐 생성
    queue.append((x,y)) #탐색할 노드 넣기
    
    while queue:
        x,y=queue.popleft()

        for i in range(4): #상하좌우로 탐색
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m: #범위 넘어가면
                continue #무시
            if graph[nx][ny]==0: #벽이면
                continue #무시
            if graph[nx][ny]==1: #탐색할 곳이면
                graph[nx][ny]=graph[x][y]+1 #경로 처리, 방문 처리 해주고 -> 이렇게 해야 또 방문 안 함
                queue.append((nx,ny)) #큐에 넣기
        
        return graph[n-1][m-1]

print(bfs(0,0))
