#Quick Sort(2)

array=[7,5,9,0,3,1,6,2,4,8]

def quick(array):
    if len(array)<=1:
        return array
    
    piv=array[0]
    tail=array[1:] #피봇을 제외한 리스트

    lft=[x for x in tail if x<=piv] #piv보다 작은 부분들
    rgt=[x for x in tail if x>piv] #piv보다 큰 부분들

    return quick(lft)+[piv]+quick(rgt) #왼편 다시 퀵 재귀로 수행, 피봇, 오른편 다시 퀵 재귀로 수행한 거 리턴

print(quick(array))