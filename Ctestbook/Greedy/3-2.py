#큰 수의 법칙
#N=배열의 길이, M=총 더해지는 횟수, K=횟수 제한

n, m, k=map(int, input().split())
data=list(map(int, input().split()))

data.sort() #작은 수부터 차례대로 정렬(반대는 .sort(reverse=True))
fst=data[n-1]
scd=data[n-2]

count=int(m/(k+1))*k+m%(k+1)

result=0
result=(fst*count)+(scd*(m-count))

print(result)