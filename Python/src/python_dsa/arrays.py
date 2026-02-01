
import time
import array
# We try to import numpy, which is the standard for heavy array usage
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("Note: NumPy not installed. Install via 'pip install numpy' for Part 3.")

def section_separator(title):
    print(f"\n{'='*10} {title} {'='*10}")

def master_arrays():
    """
    A comprehensive guide to Python Arrays: Lists, array module, and NumPy.
    """
    
    # ==========================================
    # PART 1: PYTHON LISTS (Dynamic Arrays)
    # ==========================================
    section_separator("PART 1: Python Lists (Dynamic & Flexible)")
    
    # 1. Creation and Heterogeneity
    # Unlike C++ or Java, Python lists can hold ANY data type mixed together.
    mixed_list = [1, "Hello", 3.14, True, [1, 2]] 
    print(f"Mixed List: {mixed_list}")
    
    # 2. Memory & References (The "Gotcha")
    # Lists store references (pointers) to objects, not the objects themselves.
    a = [1, 2, 3]
    b = a           # 'b' points to the same list as 'a'
    b[0] = 99
    print(f"Reference Check: Modified 'b', 'a' is now: {a} (They share memory!)")
    
    # To copy actual data, use slicing or .copy()
    c = a[:]        # Full slice copy
    c[0] = 1000
    print(f"Copy Check: Modified 'c', 'a' remains: {a}")

    # 3. Slicing (The Superpower)
    # Syntax: [start:stop:step]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Original: {numbers}")
    print(f"Slice [2:5]:   {numbers[2:5]}")
    print(f"Reverse [::-1]: {numbers[::-1]}")
    
    # 4. List Comprehension (Pythonic Transformation)
    # Create a new list by squaring even numbers only
    squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Comprehension (Squares of evens): {squares}")


    # ==========================================
    # PART 2: THE `array` MODULE (Strict & Efficient)
    # ==========================================
    section_separator("PART 2: The 'array' Module (C-style strictness)")
    
    # These are less common but useful when you need to store strictly one type of data
    # to save memory (e.g., millions of integers).
    
    # 'i' stands for signed integer (requires 2-4 bytes depending on machine)
    # You CANNOT put a string or float inside this.
    prim_array = array.array('i', [1, 2, 3, 4, 5])
    print(f"Array Module: {prim_array}")
    
    try:
        prim_array.append(3.14) # This will FAIL
    except TypeError as e:
        print(f"Constraint Enforcement: {e}")
        
    print(f"Item size: {prim_array.itemsize} bytes (Efficient memory usage)")


    # ==========================================
    # PART 3: NUMPY ARRAYS (The Data Science Standard)
    # ==========================================
    if HAS_NUMPY:
        section_separator("PART 3: NumPy (Vectorization & Power)")
        
        # 1. Creation
        # NumPy arrays are fixed type and fixed size (mostly).
        np_arr = np.array([1, 2, 3, 4, 5])
        
        # 2. Vectorization (Math without loops)
        # In lists, you loop to add. In NumPy, you just add.
        # This is heavily optimized in C under the hood.
        doubled = np_arr * 2
        print(f"Original: {np_arr}")
        print(f"Vectorized Multiplication (* 2): {doubled}")
        
        # 3. Broadcasting
        # Performing operations on arrays of different shapes
        matrix = np.array([[1, 2, 3], [4, 5, 6]])
        offset = np.array([10, 20, 30])
        print(f"\nMatrix:\n{matrix}")
        print(f"Matrix + Offset (Broadcasting):\n{matrix + offset}")
        
        # 4. Boolean Masking (Filtering)
        # Select elements greater than 3
        mask = np_arr > 3
        print(f"\nMask (Values > 3): {mask}")
        print(f"Filtered Data: {np_arr[mask]}")

    else:
        print("\n(Skipping Part 3: Install NumPy to see high-performance array features)")


    # ==========================================
    # PART 4: PERFORMANCE SHOWDOWN
    # ==========================================
    section_separator("PART 4: Performance Comparison")
    
    size = 1_000_000
    print(f"Creating and squaring {size:,} elements...")

    # Test Python List
    t0 = time.time()
    list_data = list(range(size))
    list_result = [x**2 for x in list_data]
    t1 = time.time()
    print(f"Python List time: {t1-t0:.4f} seconds")

    # Test NumPy (if available)
    if HAS_NUMPY:
        t2 = time.time()
        np_data = np.arange(size)
        np_result = np_data ** 2
        t3 = time.time()
        print(f"NumPy Array time: {t3-t2:.4f} seconds")
        print(f"NumPy is approx {(t1-t0)/(t3-t2):.1f}x faster here.")

if __name__ == "__main__":
    master_arrays()