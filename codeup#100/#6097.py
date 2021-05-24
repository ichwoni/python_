pan=[]
h, w=input().split(' ')
for i in range(int(h)):
    pan.append([])
    for j in range(int(w)):
        pan[i].append(0)

n=int(input())
md=[]

for i in range(n):
    md.append([])
    l, d, x, y=input().split(' ')
    md[i]=[int(l), int(d), int(x), int(y)]

for i in range(0, n, 1):
    if md[i][1] == 0: #가로, x
        a=md[i][2]-1
        b=md[i][3]-1
        for i in range(0, md[i][0], 1):
            if (pan[a][b]!=0):
                pan[a][b]=1
            a+=1
    else: #세로, y
        a=md[i][2]-1
        b=md[i][3]-1
        for i in range(0, md[i][0], 1):
            if (pan[a][b]!=0):
                pan[a][b]=1
            b+=1

for i in range(int(h)):
    for j in range(int(w)):
        print(pan[int(h)-1][int(w)-1], end=' ')
    print(' ')