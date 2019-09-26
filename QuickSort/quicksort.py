
def quick_sort(array, left, right):
    
    if left >= right:
        return

    pivot = (left + right) // 2
    l = left
    r = right

    while 1:

        while array[l] <= array[pivot] and l < pivot:
            l+=1

        while array[r] >= array[pivot] and r >= pivot:
            r -= 1
            if r <= pivot:
                break

        if l >= r:
            break
        else:
            array[l], array[r] = array[r], array[l]

    if l > (left+1):
        quick_sort(array, left, l)

    if r < (right-1):
        quick_sort(array, r, right)

A = [2,1,1,4,6,11,12,2,3,4,1,1,1,1,1]
B = [1,1,1,1,1]
L = 0
R = len(A)-1
RB = len(B)-1

quick_sort(B,L,RB)

print(B)
