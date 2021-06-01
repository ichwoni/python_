#Insertion Sort

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)): #2번째 인덱스부터 시작 -> 첫번째 데이터는 그 자체로 정렬되어 있다고 판단
    for j in range(i, 0, -1):
        if array[j]<array[j-1]: #나보다 작은 수 만나면
            array[j], array[j-1]=array[j-1], array[j] #바꾸기
        else: #자기보다 작은 수 만나면 스탑
            break

print(array)