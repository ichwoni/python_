#입력 횟수
n=int(input())
#불려진 출석번호
num=input().split(' ')
for i in range(n):
    num[i]=int(num[i])

for i in range(n-1, -1, -1):
    print(num[i], end=' ')