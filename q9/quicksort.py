def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]     
  
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
def quicksort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quicksort(arr, low, pi-1) 
        quicksort(arr, pi+1, high) 

if __name__ == "__main__":
    from random import randint
    import time 
    for size in range(0, 50000, 1000):
        arr = [randint(0, 99999) for _ in range(size)]
        start = time.process_time()
        quicksort(arr, 0, size-1)
        print('Time taken to sort  {} elements is {} seconds'.format(size, time.process_time()-start))


