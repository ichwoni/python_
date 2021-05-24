omp=[]
for i in range(19):
    omp.append([])
    for j in range(19):
        omp[i].append(0)

n=int(input())
for i in range(n):
    x, y=input().split(' ')
    omp[int(x)-1][int(y)-1]=1

for i in range(19):
    for j in range(19):
        print(omp[i][j], end=' ')
    print(' ')

