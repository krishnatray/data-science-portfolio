""" 
def fib(n):
    # description: fibonacci recursive implementation
    # time complexity: O(2^n)
    #in: number
    # out: fibonacci serices number at index n
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
 """

# Non Recursive
def fib(n):
    """
    description: fibonacci implementation
    in: number
    out: fibonacci serices number at index n
    """
    fib_nums = [0,1,1]
    if n == 0:
        return 0    
    elif  n <= 2: 
        return 1
    else:
        for i in range(3, n+1):
            next = fib_nums[i-1] + fib_nums[i-2]
            fib_nums.append(next)
        return next

if __name__ == "__main__":
    print("fibonacci series first 10 elements")
    for i in range(10):
        print(i,"-->",fib(i))