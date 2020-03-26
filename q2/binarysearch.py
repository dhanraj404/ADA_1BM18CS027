def binary(arr, l, r, x): 
	if r >= l: 

		mid = l + (r - l)//2
		if arr[mid] == x: 
			return mid 
		elif arr[mid] > x: 
			return binary(arr, l, mid-1, x) 
		else: 
			return binary(arr, mid+1, r, x) 

	else: 
		return -1

import time
from random import randint
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000*5)

if __name__=="__main__":
        ti=[]
        ite=[i for i in range(100, 10000, 100)]
        for i in ite:
                start_time=time.time()
                arr = [randint(1, 10000) for _ in range(i)]
                arr.sort()
                pos = binary(arr, randint(1, 10000), 0, i-1)
                timee=(time.time()-start_time)
                print("SECONDS for ", i,"samples=",timee)
                ti.append(timee)
        plt.plot(ite,ti)
        plt.show()