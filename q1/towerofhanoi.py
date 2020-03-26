def tower(n ,source = 'A', aux = 'B', destination = 'C'):
    if n == 1:
        print('Move disk',n,'from',source,'to',destination)
        return
    tower(n-1, source, destination, aux)
    print('Move disk',n,'from',source,'to',destination)
    tower(n-1, aux, source, destination)

if __name__ == "__main__":
    import time
    N = int(input("Enter the Number of Disks: "))
    start = time.process_time()
    tower(N)
    print("Time taken in seconds:",time.process_time()-start)