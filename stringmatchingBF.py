#stringmatching

def stringmatching(S, t):
	n = len(S)
	m = len(t)
	for i in range(n-m+1):
		j = 0
		while j<m and t[j] == S[i+j]:
			j+=1
			if j == m:
				return i
	else :
		return -1
	
if __name__ == '__main__':
	S = input("Enter a string: ")
	print(stringmatching(S, input("Enter smaller string to check match: ")))
	
			
