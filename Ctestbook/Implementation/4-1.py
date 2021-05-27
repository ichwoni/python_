'''
nxn 지도에서 이동, 첫 좌표는 1,1
방향은 R, L, U, D
경로에 따라 이동, 최종 좌표 구하기
'''
n=int(input())
x,y=1,1
plan=input().split()

dx=[0, 0, -1, 1] #이거 좌표 잘 이해하기.. 그려서 너가 이해하고 시작하기...
dy=[-1, 1, 0, 0]
mvtype=['L', 'R', 'U', 'D']

for p in plan: #경로 안에서
    for i in range(len(mvtype)): #방향 별로 비교
        if p == mvtype[i]: #방향이 맞으면
            if x+dx[i]<1 or y+dy[i]<1 or x+dx[i]>n or y+dy[i]>n:
                continue #저거면 암것도 하지 말고 쓰루
            x+=dx[i] #좌표값 더해주기
            y+=dy[i]

print(x,y)