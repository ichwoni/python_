#Greedy Algorithm Basic - 거스름돈
#1260원을 얼마만에 동전으로 다 거슬러줄 수 있는지

n=1260
count=0

coin_type=[500, 100, 50, 10] #값이 큰 대로 나열

for coin in coin_type:
    count += n//coin #차례대로 거스름
    n %= coin #남은 금액 

print(count)
