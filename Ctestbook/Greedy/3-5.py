# 1이 될 때까지
# n=나눌 수 k=몇으로 나눌 지
# 1) n-1 2) n/k(n이 k로 나눠 떨어질 때만)
# 최대한 많이 나누고, 안 나눠질 때만 빼기 -> 이게 그나마 최적의 해임

n,k=map(int, input().split())
rst=0

while n>=k: # n이 k 이상이라면 계속 나눔
    if (n%k)!=0: # 안 나눠지면
        n-=1 # 빼자
        rst+=1
    else:
        n//=k
        rst+=1

'''
while n>=k:
    while (n%k)!=0:
        n-=1
        rst+=1
    n//k
    rst+=1
'''

while n>1: # 이제 더 이상 안 나눠지면
    n-=1 # 빼자
    rst+=1

print(rst)