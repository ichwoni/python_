#selection sort
#가장 작은 데이터를 앞으로 보내는 과정 반복

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    minidx=i #임시 최솟값 = 현재 인덱스
    for j in range(i+1, len(array)): #minidx 뒤의 수들에서 다시 탐색
        if array[minidx]>array[j]: #새로운 최솟값 발견
            minidx=j #변경
    #python swap는 이렇게 함,, 
    array[i], array[minidx]=array[minidx], array[i] #최솟값과 현재 탐색 중인 인덱스 변경

print(array)