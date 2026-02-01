import sys
import time

# Increase recursion limit just in case
sys.setrecursionlimit(2000)

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def master_divide_and_conquer():
    """
    A comprehensive guide to the Divide and Conquer paradigm:
    1. The Concept (Explained)
    2. Applied to Sorting (Merge Sort)
    3. Applied to Math (Binary Exponentiation)
    4. Applied to Optimization (Max Subarray Sum)
    """

    # ==========================================
    # PART 1: THE CONCEPT
    # ==========================================
    section("PART 1: The Strategy")
    print("Strategy: Divide -> Conquer -> Combine")
    print("1. Divide the problem into sub-problems.")
    print("2. Solve the sub-problems recursively.")
    print("3. Combine the results into a final solution.")


    # ==========================================
    # PART 2: APPLIED TO SORTING (Merge Sort)
    # ==========================================
    section("PART 2: Sorting (Merge Sort)")
    
    def dnc_merge_sort(arr):
        # 1. BASE CASE (Conquer)
        if len(arr) <= 1:
            return arr
            
        # 2. DIVIDE
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # 3. CONQUER (Recursive Calls)
        left_sorted = dnc_merge_sort(left_half)
        right_sorted = dnc_merge_sort(right_half)
        
        # 4. COMBINE
        return merge(left_sorted, right_sorted)

    def merge(left, right):
        result = []
        i = j = 0
        # Compare and merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {data}")
    print(f"Sorted:   {dnc_merge_sort(data)}")


    # ==========================================
    # PART 3: APPLIED TO MATH (Binary Exponentiation)
    # ==========================================
    section("PART 3: Math (Powering a Number)")
    
    # Problem: Calculate x^n
    # Naive approach: Multiply x by itself n times. O(n)
    # D&C approach: x^100 is just (x^50) * (x^50). O(log n)
    
    def dnc_power(x, n):
        # 1. BASE CASE
        if n == 0:
            return 1
        
        # 2. DIVIDE & CONQUER
        # Calculate x^(n/2) once, store it
        half_power = dnc_power(x, n // 2)
        
        # 3. COMBINE
        if n % 2 == 0:
            return half_power * half_power
        else:
            return x * half_power * half_power

    base = 2
    exp = 100_000 # Massive number
    
    # Let's time the difference?
    # Note: Python's built-in pow() actually uses this method!
    t0 = time.time()
    result = dnc_power(base, exp)
    t1 = time.time()
    
    print(f"Calculated 2^{exp:,} (Result has {len(str(result))} digits)")
    print(f"Time Taken: {t1-t0:.6f} sec (Instant!)")
    print("If we did a loop 100,000 times, this would be much slower.")


    # ==========================================
    # PART 4: APPLIED TO OPTIMIZATION (Max Subarray)
    # ==========================================
    section("PART 4: Optimization (Max Subarray Sum)")
    
    # Problem: Find the contiguous slice of the list with the largest sum.
    # Data: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Answer should be [4, -1, 2, 1] which sums to 6.
    
    def max_crossing_sum(arr, low, mid, high):
        # Find best sum starting at mid and going left
        left_sum = float('-inf')
        total = 0
        for i in range(mid, low - 1, -1):
            total += arr[i]
            if total > left_sum:
                left_sum = total
        
        # Find best sum starting at mid+1 and going right
        right_sum = float('-inf')
        total = 0
        for i in range(mid + 1, high + 1):
            total += arr[i]
            if total > right_sum:
                right_sum = total
                
        # Combine
        return left_sum + right_sum

    def dnc_max_subarray(arr, low, high):
        # 1. BASE CASE
        if low == high:
            return arr[low]
        
        # 2. DIVIDE
        mid = (low + high) // 2
        
        # 3. CONQUER
        # The maximum sum is either entirely in the left half,
        # entirely in the right half, or crossing the middle.
        left_max = dnc_max_subarray(arr, low, mid)
        right_max = dnc_max_subarray(arr, mid + 1, high)
        cross_max = max_crossing_sum(arr, low, mid, high)
        
        # 4. COMBINE (Pick the winner)
        return max(left_max, right_max, cross_max)

    stock_prices_change = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(stock_prices_change)
    max_profit = dnc_max_subarray(stock_prices_change, 0, n-1)
    
    print(f"Data: {stock_prices_change}")
    print(f"Max Contiguous Sum: {max_profit}")
    # Note: Kadane's Algorithm can solve this in O(n), but D&C is O(n log n).
    # D&C is useful here if you need to parallelize the calculation across CPUs.

if __name__ == "__main__":
    master_divide_and_conquer()