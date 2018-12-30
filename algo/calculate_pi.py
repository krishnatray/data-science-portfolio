# Leibniz formula
# pi = 4/1 - 4/3 + 4/5 - 4/7 +.....
#

def cal_pi(n):
    numerator = 4.0
    denominator = 1.0
    operator = 1.0
    pi = 0.0   
    for i in range(n):
        pi +=  operator * (numerator / denominator )
        denominator += 2
        operator *= -1.0
    
    return pi

if __name__ == "__main__":
    print(cal_pi(10))
    print(cal_pi(50))
