#Write an efficient program for printing k largest elements in an array. Elements in the array can be in any order. It is given that all #array elements are distinct.

import time
start = time.process_time()

L = list(map(int, input('Enter the array : ').split()))
print(sorted(L, reverse = True)[:int(input('Value of K'))])


print(time.process_time() - start,'s') 
