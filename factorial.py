#  Finding factorial of a given number
import time
start = time.process_time()
def factorial(N):
	if N == 0 or N == 1:
		return 1
	return N*factorial(N-1)
	
print(factorial(int(input("Enter Any +ve integer :"))))


print(str(time.process_time()-start)+'s')

