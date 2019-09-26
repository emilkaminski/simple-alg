
def quick_sort(array,l,r):
    if l>=r:
        return
    pivot_index = particion(array, l, r)

    quick_sort(array,0,pivot_index-1)
    quick_sort(array,pivot_index+1,r)
    

def particion(array, left, right):

    pivot_index = right
    pivot_value = array[pivot_index]
    i = left

    while 1:
        if array[i] >= pivot_value:
            array[i], array[pivot_index-1] = array[pivot_index-1],array[i]
            array[pivot_index-1],array[pivot_index]=array[pivot_index],array[pivot_index-1]
            pivot_index -= 1
            i = left

        i += 1
        if i >= pivot_index:
           return pivot_index

A = [7,5,12,43,2,1,55,65,1,23,12,6,54,2,1,2,3,6,7,3,4]

#particion(A,0,len(A)-1)
quick_sort(A,0,len(A)-1)
print(A)
