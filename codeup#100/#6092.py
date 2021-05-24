#입력 횟수
n=int(input())
#불려진 출석번호
num=input().split(' ')
for i in range(n):
    num[i]=int(num[i])
#출석 번호에 불려진 횟수 대응 저장
mnum=[]

#mnum에 일단 0 저장
for i in range(23):
    mnum.append(0)

for i in range(23):
    for j in range(n):
        if (num[j]==i+1): #i는 0부터 시작하니까 1 더해줘야 함
            mnum[i]+=1

for i in mnum:
    print(i, end=' ')
