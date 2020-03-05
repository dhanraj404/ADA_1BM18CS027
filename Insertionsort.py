
# Insertion Sort 

def insertionSort(arr): 

	for i in range(1, len(arr)): 

		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key
	for i in arr:
		print("%d"%i) 

arr = list(map(int, input("Enter the Array elements:\n").split()))
insertionSort(arr)
