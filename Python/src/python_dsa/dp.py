import time
import sys

# Increase recursion limit for deep recursion demonstrations
sys.setrecursionlimit(2000)

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def master_dynamic_programming():
    """
    A comprehensive guide to DP:
    1. The Evolution (Naive -> Memoization -> Tabulation)
    2. 1D DP: Climbing Stairs
    3. 2D DP: The 0/1 Knapsack Problem (The "Boss" Level)
    """

    # ==========================================
    # PART 1: THE EVOLUTION (Fibonacci)
    # ==========================================
    section("PART 1: The Evolution (Fibonacci)")
    
    n_val = 35  # Large enough to slow down naive recursion
    
    # --- LEVEL 0: NAIVE RECURSION (Bad) ---
    def fib_naive(n):
        if n <= 1: return n
        return fib_naive(n-1) + fib_naive(n-2)

    print(f"Calculating fib({n_val}) Naively...")
    t0 = time.time()
    res = fib_naive(n_val)
    t1 = time.time()
    print(f"Naive Result: {res}")
    print(f"Time: {t1-t0:.4f} sec (Slow! O(2^n))")


    # --- LEVEL 1: TOP-DOWN (Memoization) ---
    # Strategy: "Check Dictionary before calculating"
    memo = {}
    def fib_memo(n):
        if n <= 1: return n
        if n in memo: return memo[n]  # The Magic Line
        
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]

    t2 = time.time()
    res = fib_memo(n_val)
    t3 = time.time()
    print(f"\nMemoized Result: {res}")
    print(f"Time: {t3-t2:.6f} sec (Instant! O(n))")


    # --- LEVEL 2: BOTTOM-UP (Tabulation) ---
    # Strategy: "Fill a table from 0 to n"
    def fib_tabulation(n):
        if n <= 1: return n
        # Create table of size n+1
        table = [0] * (n + 1)
        table[1] = 1
        
        # Loop forward
        for i in range(2, n + 1):
            table[i] = table[i-1] + table[i-2]
        
        return table[n]

    t4 = time.time()
    res = fib_tabulation(n_val)
    t5 = time.time()
    print(f"\nTabulation Result: {res}")
    print(f"Time: {t5-t4:.6f} sec (Instant! O(n))")
    
    # NOTE: Tabulation is often preferred in production because 
    # it avoids RecursionError on massive inputs.


    # ==========================================
    # PART 2: 1D DP (Climbing Stairs)
    # ==========================================
    section("PART 2: 1D DP (Climbing Stairs)")
    
    # Problem: You are at step 0. You can take 1 step or 2 steps.
    # How many distinct ways to reach step N?
    # Logic: To get to step 10, you must have come from step 9 (taking 1) OR step 8 (taking 2).
    # distinct_ways(i) = distinct_ways(i-1) + distinct_ways(i-2)
    # This is exactly Fibonacci!
    
    def climb_stairs(n):
        if n <= 2: return n
        
        # Space Optimization: We only need the last 2 numbers, not a whole list.
        prev2 = 1 # Way to reach step 0
        prev1 = 2 # Ways to reach step 1 (1, 1+1, 2)
        
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1

    steps = 10
    print(f"Ways to climb {steps} stairs: {climb_stairs(steps)}")


    # ==========================================
    # PART 3: 2D DP (The Knapsack Problem)
    # ==========================================
    section("PART 3: 2D DP (0/1 Knapsack)")
    
    # Problem: Maximize value in a bag of capacity W.
    # Constraint: You cannot break items (0 or 1).
    # Decision: For every item, we either INCLUDE it or EXCLUDE it.
    
    weights = [2, 3, 4, 5]
    values =  [3, 4, 5, 6]
    capacity = 5
    n_items = len(weights)
    
    # We build a 2D Table:
    # Rows (i) = Considering first 'i' items
    # Cols (w) = Considering capacity 'w'
    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n_items + 1)]
    
    for i in range(1, n_items + 1):
        for w in range(1, capacity + 1):
            
            curr_weight = weights[i-1]
            curr_val = values[i-1]
            
            if curr_weight <= w:
                # Option 1: Exclude item (Take value from row above)
                exclude_val = dp[i-1][w]
                
                # Option 2: Include item (Add value + space left for remaining weight)
                include_val = curr_val + dp[i-1][w - curr_weight]
                
                # Take the best of both
                dp[i][w] = max(exclude_val, include_val)
            else:
                # Cannot fit item, must exclude
                dp[i][w] = dp[i-1][w]

    print(f"Items (Weight): {weights}")
    print(f"Items (Value):  {values}")
    print(f"Max Capacity:   {capacity}")
    print(f"\nMaximum Value Possible: {dp[n_items][capacity]}")
    
    # Visualizing the Decision Table
    print("\nDP Table (Decision Matrix):")
    for row in dp:
        print(row)

if __name__ == "__main__":
    master_dynamic_programming()