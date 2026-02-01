import random
import time
import sys

# Increase recursion depth for deep recursion in Quick/Merge sort
sys.setrecursionlimit(2000)

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def measure_time(name, func, arr):
    """Helper to time a sorting function"""
    # Create a copy so we don't sort an already sorted list for the next algorithm
    data = arr.copy()
    
    start = time.time()
    result = func(data)
    end = time.time()
    
    # Validation check (crucial!)
    if result != sorted(arr):
        print(f"❌ {name} FAILED! Result not sorted.")
        return
        
    print(f"✅ {name:15}: {end - start:.6f} seconds")

# ==========================================
# PART 1: THE "SLOW" SORTS (O(n²))
# ==========================================
# These are intuitive but choke on large datasets.

def bubble_sort(arr):
    """
    Repeatedly swaps adjacent elements if they are in wrong order.
    The largest elements 'bubble' to the top.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap
                swapped = True
        # Optimization: If no swaps occurred, list is already sorted
        if not swapped:
            break
    return arr

def selection_sort(arr):
    """
    Finds the minimum element and moves it to the front.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """
    Builds the sorted array one item at a time.
    Like sorting playing cards in your hand.
    VERY FAST for small or nearly-sorted lists.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # Shift right
            j -= 1
        arr[j + 1] = key
    return arr


# ==========================================
# PART 2: THE "FAST" SORTS (O(n log n))
# ==========================================
# These use "Divide and Conquer" logic.

def merge_sort(arr):
    """
    Recursively splits list in half, sorts halves, then merges them.
    Pros: Stable, guaranteed O(n log n).
    Cons: Uses extra memory.
    """
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)

def _merge(left, right):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Append any leftovers
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def quick_sort(arr):
    """
    Picks a 'pivot', puts smaller items left, larger right.
    Pros: Usually the fastest in practice (Cache friendly).
    Cons: Worst case O(n²) if pivot is bad (rare with random pivot).
    Note: This is the readable 'Pythonic' version (not in-place).
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


# ==========================================
# PART 3: PYTHON'S NATIVE (Timsort)
# ==========================================
def python_native_sort(arr):
    """
    Uses Timsort (Hybrid of Merge Sort + Insertion Sort).
    Highly optimized in C.
    """
    return sorted(arr)


# ==========================================
# PART 4: THE RACE
# ==========================================
def master_sorting():
    section("Sorting Algorithm Showdown")
    
    # 1. Setup Data
    size = 2000  # Kept small (2000) so O(n^2) sorts don't freeze your computer
    print(f"Generating random list of {size} integers...")
    test_data = [random.randint(0, 10000) for _ in range(size)]
    
    # 2. Race the Slow Algos
    section("Round 1: The O(n²) Club")
    measure_time("Bubble Sort", bubble_sort, test_data)
    measure_time("Selection Sort", selection_sort, test_data)
    measure_time("Insertion Sort", insertion_sort, test_data)
    
    # 3. Race the Fast Algos
    section("Round 2: The O(n log n) Club")
    # Increase size to show true power
    big_size = 100_000
    print(f"(Switching to {big_size:,} items for Fast Sorts...)")
    big_data = [random.randint(0, 1_000_000) for _ in range(big_size)]
    
    measure_time("Merge Sort", merge_sort, big_data)
    measure_time("Quick Sort", quick_sort, big_data)
    measure_time("Python Native", python_native_sort, big_data)
    
    # 4. The Insertion Sort Advantage
    section("Round 3: The 'Nearly Sorted' Case")
    print("Sorting a list that is already 99% sorted...")
    nearly_sorted = list(range(2000))
    nearly_sorted[1900] = 5  # Swap one item
    
    measure_time("Bubble Sort", bubble_sort, nearly_sorted)
    measure_time("Insertion Sort", insertion_sort, nearly_sorted)
    measure_time("Quick Sort", quick_sort, nearly_sorted)
    
    print("\nObservation: Insertion Sort destroys Quick Sort on nearly sorted data!")

if __name__ == "__main__":
    master_sorting()