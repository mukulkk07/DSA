import sys
import time
from functools import lru_cache

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def master_recursion():
    """
    A comprehensive guide to Recursion:
    1. The Stack Visualization (See it happen)
    2. Returning Values (Factorial)
    3. The Danger (Stack Overflow)
    4. The Performance Trap (Fibonacci)
    5. The Fix (Memoization)
    """

    # ==========================================
    # PART 1: THE STACK VISUALIZATION
    # ==========================================
    section("PART 1: Visualizing the Stack")
    
    def countdown_visual(n, level=0):
        # Indentation represents stack depth
        indent = "    " * level
        
        # 1. BASE CASE (The Stop Sign)
        if n == 0:
            print(f"{indent}🛑 Base Case Reached! (n=0)")
            return
        
        # 2. THE DIVE (Pre-recursion)
        print(f"{indent}⬇️ Pushing Frame n={n}")
        
        # 3. RECURSIVE STEP
        countdown_visual(n - 1, level + 1)
        
        # 4. THE SURFACE (Post-recursion)
        print(f"{indent}⬆️ Popping Frame n={n}")

    countdown_visual(3)
    print("\nNote: See how the code 'pauses' at n=3 while waiting for n=2?")


    # ==========================================
    # PART 2: ACCUMULATING VALUES (Factorial)
    # ==========================================
    section("PART 2: Passing Data Back Up")
    
    # Logic: 5! = 5 * 4!
    
    def factorial(n):
        if n == 1:
            return 1 # Base case: 1! is 1
        
        # The function pauses here until the child returns an answer
        sub_answer = factorial(n - 1)
        
        return n * sub_answer

    print(f"Factorial of 5: {factorial(5)}")


    # ==========================================
    # PART 3: THE DANGER ZONE (Stack Overflow)
    # ==========================================
    section("PART 3: RecursionLimit & Stack Overflow")
    
    # Python limits the stack depth to 1000 by default to prevent crashes.
    current_limit = sys.getrecursionlimit()
    print(f"Current Recursion Limit: {current_limit} frames")
    
    def infinite_dive(n):
        try:
            infinite_dive(n + 1)
        except RecursionError:
            print(f"💥 CRASHED at depth: {n}")
            return

    infinite_dive(1)
    
    # You can change this limit (use with caution!)
    # sys.setrecursionlimit(5000)


    # ==========================================
    # PART 4: THE TRAP (Exponential Growth)
    # ==========================================
    section("PART 4: The Fibonacci Trap (O(2^n))")
    
    # Fib: 0, 1, 1, 2, 3, 5, 8...
    # Rule: fib(n) = fib(n-1) + fib(n-2)
    
    def fib_naive(n):
        if n <= 1: return n
        return fib_naive(n-1) + fib_naive(n-2)

    n_val = 35
    print(f"Calculating fib({n_val}) WITHOUT optimization...")
    
    t0 = time.time()
    # This will be slow because it recalculates the same numbers millions of times
    result = fib_naive(n_val) 
    t1 = time.time()
    
    print(f"Result: {result}")
    print(f"Time Taken: {t1-t0:.4f} seconds (Slow!)")


    # ==========================================
    # PART 5: THE FIX (Memoization)
    # ==========================================
    section("PART 5: Memoization (Caching Results)")
    
    # We use a dictionary (hashmap) to remember answers we've already found.
    memo = {}
    
    def fib_memoized(n):
        if n <= 1: return n
        
        # Check cache first!
        if n in memo:
            return memo[n]
        
        # Calculate and Store
        memo[n] = fib_memoized(n-1) + fib_memoized(n-2)
        return memo[n]

    print(f"Calculating fib({n_val}) WITH optimization...")
    t2 = time.time()
    result_fast = fib_memoized(n_val)
    t3 = time.time()
    
    print(f"Result: {result_fast}")
    print(f"Time Taken: {t3-t2:.6f} seconds (Instant!)")
    
    # PRO TIP: Python has a built-in decorator for this!
    @lru_cache(maxsize=None)
    def fib_pythonic(n):
        if n <= 1: return n
        return fib_pythonic(n-1) + fib_pythonic(n-2)
    
    # It can handle massive numbers now
    print(f"Fib(100) using @lru_cache: {fib_pythonic(100)}")

if __name__ == "__main__":
    master_recursion()