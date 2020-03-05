"""
There is one meeting room in a firm. There are N meetings in the form of (Si, Fi) where Si is the start time of meeting i and Fi is finish time of meeting i. The task is to find the maximum number of meetings that can be accommodated in the meeting room. Print all meeting numbers.
"""

if __name__ == '__main__':
	N = int(input("Enter total Number of meetings: "))
	S = list()
	F = list()
	for i in range(1, N+1):
		print(i,"th Meeting:")
		S.append(int(input("Start time=")))
		F.append(int(input("End time=")))
	S.sort()
	F.sort()
	resst = [0]*N
	resf = [0]*N
	mnum = [0]*N
	resst[0] = S[0]
	resf[0] = F[0]
	p = 0
	q = 0
	mnum[0] = 1
	for i in range(1, N):
		if S[i]>resf[p]:
			q += 1
			p += 1
			resst[q] = S[i]
			resf[p] = F[i]
			mnum[q] = i+1
	print("Maximum number of meeting:", q+1)
	
	print("Meeting numbers are: ")
	print(mnum)
	for i in range(q+1):
		print(resst[i], resf[i])

	 
	
