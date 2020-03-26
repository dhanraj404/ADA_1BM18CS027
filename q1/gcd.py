def gcd(m , n):
    if n == 0:
        return m
    return gcd(n, m%n)

if __name__ == "__main__":
    import time
    start = time.process_time()
    m = int(input("Enter First Number: \n"))
    n = int(input("Enter Second Number: \n"))
    print("GCD: {}\nTime Taken in Seconds:{}".format(gcd(m,n), time.process_time()-start))