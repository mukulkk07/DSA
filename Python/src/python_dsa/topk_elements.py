import heapq
import random
import time
import collections

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def master_top_k():
    """
    A comprehensive guide to finding the 'Top K' elements:
    1. Naive Sorting (Easiest, Slower)
    2. The Min-Heap Strategy (Memory Efficient, Standard)
    3. Python's Built-in Optimized Tools
    4. QuickSelect (The O(N) algorithmic approach)
    5. Real World Application (Frequency Analysis)
    """

    # ==========================================
    # PART 1: THE STRATEGIES
    # ==========================================
    section("PART 1: Strategy Comparison")
    
    # Let's generate a dataset of 1 million numbers
    N = 1_000_000
    K = 10
    print(f"Generating {N:,} random numbers...")
    data = [random.randint(0, 10_000_000) for _ in range(N)]
    print(f"Goal: Find the {K} largest numbers.")

    # --- STRATEGY A: NAIVE SORTING ---
    # Sort the whole list, take the last K.
    # Complexity: O(N log N)
    t0 = time.time()
    sorted_method = sorted(data, reverse=True)[:K]
    t1 = time.time()
    print(f"\n1. Sort & Slice:     {t1-t0:.4f} sec (Slowest)")
    print(f"   Result: {sorted_method}")


    # --- STRATEGY B: MIN-HEAP (Keep only K items) ---
    # We maintain a heap of size K. If a new number is bigger than the
    # smallest number in our heap, we swap them.
    # Complexity: O(N log K) - Much faster if K is small!
    t2 = time.time()
    
    heap = []
    for num in data:
        # Push first K elements
        if len(heap) < K:
            heapq.heappush(heap, num)
        else:
            # If current num is larger than the smallest in heap...
            if num > heap[0]:
                # Replace the smallest with current num
                heapq.heapreplace(heap, num)
    
    # Sort final heap to match previous output
    heap_method = sorted(heap, reverse=True) 
    t3 = time.time()
    
    print(f"2. Manual Min-Heap:  {t3-t2:.4f} sec (Memory Efficient)")
    print(f"   Result: {heap_method}")


    # --- STRATEGY C: PYTHON'S BUILT-IN (Optimized C) ---
    # Python's heapq.nlargest does Strategy B efficiently in C.
    t4 = time.time()
    builtin_method = heapq.nlargest(K, data)
    t5 = time.time()
    
    print(f"3. heapq.nlargest:   {t5-t4:.4f} sec (Best balance)")
    print(f"   Result: {builtin_method}")


    # ==========================================
    # PART 2: THE ALGORITHMIC BEAST (QuickSelect)
    # ==========================================
    section("PART 2: QuickSelect (Average O(N))")
    
    # QuickSelect is related to QuickSort. instead of sorting both sides,
    # we only dive into the side that contains the Kth element.
    # Note: Pure Python recursion hits limits, so this is for education.
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            # We want largest, so we look for elements > pivot
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quickselect(arr, low, high, k):
        if low <= high:
            pivot_index = partition(arr, low, high)
            
            # Did we land exactly on the Kth element?
            if pivot_index == k:
                return arr[:k+1] # Return everything up to K
            elif pivot_index > k:
                return quickselect(arr, low, pivot_index - 1, k)
            else:
                return quickselect(arr, pivot_index + 1, high, k)
        return []

    # Run on a smaller copy to avoid recursion depth issues or modifying original
    # QuickSelect modifies the list in-place!
    data_copy = data[:100_000] # Smaller subset for safety
    k_index = K - 1
    
    t6 = time.time()
    # This rearranges the list so top K are at the front (unsorted)
    quickselect(data_copy, 0, len(data_copy)-1, k_index)
    qs_result = sorted(data_copy[:K], reverse=True)
    t7 = time.time()
    
    print(f"QuickSelect (on 100k items): {t7-t6:.4f} sec")
    print(f"Result: {qs_result}")


    # ==========================================
    # PART 3: REAL WORLD APPLICATION (Frequency)
    # ==========================================
    section("PART 3: Top K Frequent Items")
    
    # Problem: Given a massive log of IP addresses, find the Top 3 most active.
    
    logs = [
        "192.168.1.1", "10.0.0.1", "192.168.1.1", "127.0.0.1",
        "10.0.0.1", "192.168.1.1", "8.8.8.8", "10.0.0.1", "10.0.0.1"
    ]
    
    # 1. Count frequencies (HashMap)
    counts = collections.Counter(logs)
    print(f"Raw Counts: {dict(counts)}")
    
    # 2. Extract Top K (Uses Heap strategy internally)
    top_2 = counts.most_common(2)
    
    print(f"Top 2 IPs: {top_2}")

if __name__ == "__main__":
    master_top_k()