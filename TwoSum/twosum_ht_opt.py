
def check (array, number):
    
    hash_table = {}

    index = 0
    for index in range (0,len(array)):
    
        a = array[index]
        b = number - a #this is our potencial b number.
                        #we just need to check if it exist

        if b in hash_table:
            return a, b
        else:
            hash_table[a] = True

        index += index


A = [2,4,5,2,7,8,11,9,10]
L = 20

a, b = check(A,L)
print(a, 'and', b)

