'''
00:00:00~n:59:59까지 모든 시각 중에서 3이 하나라도 포함되면 cnt+1
'''
n=int(input())
m=59
s=59
cnt=0

for i in range(n+1):
    for j in range(m+1):
        for k in range(s+1):
            if '3' in str(i)+str(j)+str(k): # 전체 시각을 봐야 하니까...^^..
                cnt+=1

print(cnt)