
def sort(array):
    
    for n in range(0,len(array)-1):
        change = False
        for i in range(n,len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                change = True
        print(array)
        if change == False: # job done
            return

A = [2,0,5,1,6,3]

sort(A)
 
