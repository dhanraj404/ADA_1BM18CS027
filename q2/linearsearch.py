def linear(arr, key, front, rear):
    if front > rear:
        return -1
    if arr[front] == key:
        return front
    return linear(arr, key, front+1, rear)


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
                pos = linear(arr, randint(1, 10000), 0, i-1)
                timee=(time.time()-start_time)
                print("SECONDS for ", i,"samples=",timee)
                ti.append(timee)
        plt.plot(ite,ti)
        plt.show()