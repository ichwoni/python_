n1, n2, n3=input().split(' ')

a=[]
a.append(int(n1))
a.append(int(n2))
a.append(int(n3))

for i in a:
    if i%2==0:
        print('even')
    else:
        print('odd')