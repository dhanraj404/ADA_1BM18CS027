#selection sort

#
import time
start = time.process_time()

def selection(A):
	for i in range(len(A)):
		min_index = i
		for j in range(i+1, len(A)):
			if A[min_index] > A[j]:
				min_index = j
		A[i],A[min_index] = A[min_index],A[i]
	print("Sorted Array: \n", A)
if __name__ == '__main__':
	A = list(map(int, input("Enter the array element: ").split()))	
	selection(A)
	print(time.process_time()-start, 's')
