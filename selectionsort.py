#selection sort

import time
import random
import matplotlib.pyplot as plt
start_time = time.process_time()

def selection(A):
	for i in range(len(A)):
		min_index = i
		for j in range(i+1, len(A)):
			if A[min_index] > A[j]:
				min_index = j
		A[i],A[min_index] = A[min_index],A[i]
	print("Sorted Array: \n", A)
	
'''
if __name__ == '__main__':
	A = list(map(int, input("Enter the elements").split()))
	selection(A)
'''
if __name__ == '__main__':
        ti=[]
        ite=[i for i in range(100)]
        for i in ite:
                start_time=time.time()
                a=random.sample(range(1,i*1000),i)
                selection(a)
                timee=(time.time()-start_time)
                print("SECONDS for ", i,"samples=",timee)
                ti.append(timee)
        plt.plot(ite,ti)
        plt.show()

