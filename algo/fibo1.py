# fibonacci series:
# 0,1,1,2,3,5,8,13,21, ....
# fibo(n) = fibo(n-1) + fibo(n-2)

import time

def fibo1(n):
    if n < 2:
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)
    

if __name__ == "__main__":
    start = time.time()
    print("fibo 5  ---->", fibo1(5))
    print("fibo 10 ---->", fibo1(10))
    print("Elapsed time", time.time()-start)