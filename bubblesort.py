#Sort a given set of N integer elements using Bubble Sort technique and compute its time taken. Run the program for different values of N #and record the time taken to sort.

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
if __name__ == '__main__':

	arr = list(map(int, input("Enter the Array Elements :").split()))
	import time 
	start = time.process_time() 
	bubbleSort(arr) 
	print ("Sorted array is:")
	for i in range(len(arr)):
	    print ("%d" %arr[i]),
	print("Time taken in s:")
	print(time.process_time() - start)
