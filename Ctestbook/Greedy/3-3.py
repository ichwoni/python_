# 카드게임
# nxm으로 이루어진 카드
# 행 선택, 그 행에서 가장 낮은 숫자 선택 -> 행 별로 가장 낮은 숫자들 중에 제일 높은 숫자를 구해야 함

n, m=map(int, input().split())
result=0

for i in range(n):
    data=list(map(int, input().split())) # 행마다 새롭게 데이터 받고
    minval=min(data) # 그 행에서 가장 작은 수 구하고
    result=max(result, minval) # 이전 회차에서 구해진 result랑 다시 비교 

print(result)