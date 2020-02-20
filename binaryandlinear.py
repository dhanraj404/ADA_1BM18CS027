#Implement Recursive Binary search and Linear search and determine the time required to search an element. Repeat the experiment for #different values of N and plot a graph of the time taken versus N.

def binary(L,x):
    L.sort()
    l = 0
    n = r = len(L)-1
    while l <= r:
        mid = int((l+r)/2)
        if L[mid] == x:
            '''
            i = mid
            k = mid
            while L[i] == x and i >= 0:
                f_pos = i
                i -= 1
            while L[k] == x and k != n:
                l_pos = k
                k += 1
            if k == n:
                l_pos += 1
            print('The first occurrence of the key is at:',f_pos,'\nLast occurrence is at ',l_pos)
            print('Count:',(l_pos-f_pos+1))
            return
            '''
            print('Element found')
            return 
        elif L[mid] < x:
            l = mid+1
        else :
            r = mid-1
        
    else:
        print('Element not found.')
        return
    
def linear(L, x):
	L.sort()
	for i in range(len(L)+1):
		if L[i] == x:
			print("Element found")
	else :
		print("Element not found")
	
import time	
L = list(map(int, input('Enter the Array:').split()))
x = int(input('Enter the search element:'))
startB = time.process_time()
binary(L, x)
print("Binary Search",time.process_time()-startB)

startL = time.process_time()
linear(L, x)
print("Linear Search",time.process_time()-startL)

