def fib(n):
    """
    description: fibonacci recursive implementation
    in: number
    out: fibonacci serices number at index n
    """
    if n <=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print("fibonacci series first 10 elements")
    for i in range(10):
        print(i+1,"-->",fib(i))