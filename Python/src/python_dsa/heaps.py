import heapq
import random

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def master_heaps():
    """
    A comprehensive guide to Heaps in Python:
    1. The Min-Heap (Standard Behavior)
    2. Heapify (Instant Construction)
    3. The Max-Heap Trick (The Workaround)
    4. Heap Sort (O(N log N))
    5. The "Top K" Shortcut
    """

    # ==========================================
    # PART 1: THE MIN-HEAP (Standard)
    # ==========================================
    section("PART 1: The Min-Heap (heapq)")
    
    # A heap is just a regular list, but we use special functions to modify it.
    heap = []
    
    # 1. PUSH (Add items) - O(log N)
    # The smallest item bubbles to index 0.
    heapq.heappush(heap, 10)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 5)
    
    print(f"Heap Structure: {heap}")
    # Note: It might look like [1, 10, 5]. 
    # Heaps are NOT sorted lists. They only guarantee heap[0] is the smallest.
    
    # 2. PEEK (Look at min) - O(1)
    print(f"Minimum Element: {heap[0]}")
    
    # 3. POP (Remove min) - O(log N)
    min_val = heapq.heappop(heap)
    print(f"Popped: {min_val}")
    print(f"Remaining Heap: {heap}")


    # ==========================================
    # PART 2: HEAPIFY (Instant Build)
    # ==========================================
    section("PART 2: Heapify (O(N))")
    
    # If you have a pre-existing list, don't push items one by one.
    # Use heapify() to rearrange them in-place efficiently.
    
    data = [9, 1, 5, 2, 8, 3]
    print(f"Original List: {data}")
    
    heapq.heapify(data)
    print(f"Heapified:     {data}")
    print(f"Smallest is now at data[0]: {data[0]}")


    # ==========================================
    # PART 3: THE MAX-HEAP TRICK
    # ==========================================
    section("PART 3: The Max-Heap Trick")
    
    # Python does NOT have a Max-Heap class.
    # TRICK: Multiply numbers by -1. 
    # The "smallest" negative number is actually the largest positive number.
    
    scores = [100, 50, 80, 20, 90]
    max_heap = []
    
    print(f"Scores: {scores}")
    
    # Add as negative
    for s in scores:
        heapq.heappush(max_heap, -s)
        
    print(f"Internal Storage: {max_heap}")
    
    # Retrieve as positive (multiply by -1 again)
    highest = -heapq.heappop(max_heap)
    next_highest = -heapq.heappop(max_heap)
    
    print(f"Highest Score: {highest}")
    print(f"Next Highest:  {next_highest}")


    # ==========================================
    # PART 4: HEAP SORT
    # ==========================================
    section("PART 4: Heap Sort")
    
    def heap_sort(arr):
        # 1. Convert to heap
        heapq.heapify(arr)
        sorted_arr = []
        
        # 2. Pop one by one
        while arr:
            sorted_arr.append(heapq.heappop(arr))
            
        return sorted_arr

    unsorted = [40, 10, 30, 50, 20]
    print(f"Unsorted: {unsorted}")
    print(f"Sorted:   {heap_sort(unsorted)}")


    # ==========================================
    # PART 5: EFFICIENT "TOP K"
    # ==========================================
    section("PART 5: nlargest & nsmallest")
    
    # You generally don't need to write the loops yourself.
    # heapq has highly optimized C-functions for this.
    
    large_dataset = [random.randint(1, 1000) for _ in range(20)]
    print(f"Dataset: {large_dataset}")
    
    # Get Top 3 largest
    top_3 = heapq.nlargest(3, large_dataset)
    print(f"Top 3 Largest:  {top_3}")
    
    # Get Top 3 smallest
    bottom_3 = heapq.nsmallest(3, large_dataset)
    print(f"Top 3 Smallest: {bottom_3}")

if __name__ == "__main__":
    master_heaps()