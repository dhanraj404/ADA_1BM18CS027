def binary(L,x):
    L.sort()
    l = 0
    r = len(L)-1
    while l <= r:
        mid = int((l+r)/2)
        if L[mid] == x:
            i = mid
            k = mid
            while L[i] == x and i != 0:
                f_pos = i
                i -= 1
            while L[k] == x and k != r:
                l_pos = k
                k += 1
            print('The first occurrence of the key is at:',f_pos,'\nLast occurrence is at ',l_pos)
            print('Count:',(l_pos-f_pos+1))
            return
        elif L[mid] < x:
            l = mid+1
        else :
            r = mid-1
        
    else:
        print('Element not found.')
        return
    

L = list(map(int, input('Enter the Array:').split()))
binary(L, int(input('Enter the search element:')))
