##########################
# Knapsack problem
#
##########################

# Given two arrays wt and val, goal is to find maximum value in a knapsack with capacity N
#   
def knap_sack(W , wt , val , n): 
    """
    Returns the maximum value that can be put in a knapsack of capacity W 

    """
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knap_sack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knap_sack(W-wt[n-1] , wt , val , n-1), 
                   knap_sack(W , wt , val , n-1)) 

def run_knapsack(val, wt, W, n):
    print("val-->", val)
    print("wt -->", wt)
    print("capacity-->", W)
    print("======= Results =======")
    print("Max value--->", knap_sack(W , wt , val , n) ) 
    print("=======================\n")
   
if __name__ == "__main__":
    val = [60, 100, 120] 
    wt = [10, 20, 30] 
    W = 50
    n = len(val) 
    run_knapsack(val, wt, W, n)

    # 2nd run
    val = [6, 10, 5, 4, 2 ] 
    wt = [10, 20, 30, 40, 50] 
    W = 60
    n = len(val) 
    run_knapsack(val, wt, W, n)

