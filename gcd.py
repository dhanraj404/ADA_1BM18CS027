#Eucild Algorithm to find GCD

def GCD(m, n):
    if n == 0:
        return m
    return GCD(n, m%n)

if __name__ == "__main__":
    m = int(input('Enter First Number:'))
    n = int(input('Enter Second Number:'))
    print(GCD(m, n))