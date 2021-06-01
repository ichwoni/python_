#Quick Sort(1)

array=[7,5,9,0,3,1,6,2,4,8]

def quick(array, start, end):
    if start>=end:
        return
    piv=start
    left=start+1 #2번째부터 시작
    right=end
    while left<=right:
        while left<=end and array[left]<=array[piv]:
            left+=1
        while right>start and array[right]>=array[piv]:
            right-=1
        if left>right:
            array[right], array[piv]=array[piv], array[right]
        else:
            array[left], array[right]=array[right], array[left]
    
    quick(array, start, right-1)
    quick(array, right+1, end)

quick(array, 0, len(array)-1)
print(array)
