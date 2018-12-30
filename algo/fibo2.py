# fibonacci series:
# 0,1,1,2,3,5,8,13,21, ....
# fibo(n) = fibo(n-1) + fibo(n-2)

import time

# using meomization
cached = {0: 0, 1: 1}
def fibo2(n):
    if n not in cached:
        #print("calculating element #", n)
        cached[n] = fibo2(n-1) + fibo2(n-2)
    
    return cached[n]
    

if __name__ == "__main__":
    start = time.time()
    print("fibo 5  ---->", fibo2(5))
    print("fibo 10 ---->", fibo2(10))
    print("fibo 50 ---->", fibo2(50))
    print("fibo 40 ---->", fibo2(40))
    print("Elapsed time", time.time()-start)
    print(cached)