import time
import collections
from sys import getsizeof

def section(title):
    print(f"\n{'-'*10} {title} {'-'*10}")

def master_hashmaps():
    """
    A comprehensive guide to Python Dictionaries (Hashmaps):
    1. Basics (CRUD Operations)
    2. The Mechanics (Hashing & Immutability)
    3. Safe Access & Defaults (get, setdefault, defaultdict)
    4. Advanced Variants (Counter, OrderedDict)
    5. Performance Showdown (List vs Dict)
    """

    # ==========================================
    # PART 1: THE BASICS (CRUD)
    # ==========================================
    section("PART 1: The Basics (Key-Value Pairs)")
    
    # Creation
    # Keys must be unique. Values can be anything.
    user_db = {
        "user_id": 101,
        "username": "coder_x",
        "is_active": True,
        "skills": ["Python", "Linux"]
    }
    
    # Read (Access by Key) - O(1)
    print(f"Username: {user_db['username']}")
    
    # Update (Mutable)
    user_db["username"] = "master_coder" # Change existing
    user_db["level"] = 99                # Add new
    
    # Delete
    del user_db["is_active"] # Removes key & value
    
    print(f"Updated DB: {user_db}")
    
    # Iteration (Views)
    print("\nIterating:")
    for key, val in user_db.items():
        print(f" -> {key}: {val}")


    # ==========================================
    # PART 2: THE MECHANICS (Hashing & Immutability)
    # ==========================================
    section("PART 2: How it works (Hashing)")
    
    # Python uses a function hash(key) to calculate a memory address.
    # Therefore, KEYS MUST BE IMMUTABLE (Strings, Numbers, Tuples).
    
    key_string = "Hello"
    key_tuple = (1, 2)
    
    print(f"Hash of 'Hello': {hash(key_string)}")
    print(f"Hash of (1, 2):  {hash(key_tuple)}")
    
    # The Trap: Mutable keys are forbidden.
    try:
        bad_dict = {}
        my_list = [1, 2, 3] # Lists can change, so their hash is unstable
        bad_dict[my_list] = "Will Fail"
    except TypeError as e:
        print(f"\nExpected Error: {e}")
        print("Reason: You cannot use a List as a Key because it is mutable.")


    # ==========================================
    # PART 3: SAFE ACCESS & DEFAULTS
    # ==========================================
    section("PART 3: Handling Missing Keys")
    
    inventory = {"apple": 5, "banana": 2}
    
    # The unsafe way (Risk of KeyError)
    # print(inventory["orange"]) -> CRASH!
    
    # 1. The .get() method (Safe)
    # Returns None (or a default) if key missing
    print(f"Orange count: {inventory.get('orange', 0)}")
    
    # 2. collections.defaultdict (The Automatic Way)
    # Great for grouping data
    grouped_words = collections.defaultdict(list)
    words = ["apple", "bat", "ant", "ball", "cat"]
    
    for w in words:
        first_letter = w[0]
        grouped_words[first_letter].append(w)
        
    print(f"Grouped by letter: {dict(grouped_words)}")


    # ==========================================
    # PART 4: ADVANCED TOOLS (Counter)
    # ==========================================
    section("PART 4: Frequency Counting (Counter)")
    
    # A specialized dictionary designed for counting stuff
    text = "banana apple apple banana banana cherry"
    words = text.split()
    
    counts = collections.Counter(words)
    print(f"Counts: {counts}")
    print(f"Most common: {counts.most_common(1)}")
    
    # You can even do math on them!
    sales_monday = collections.Counter({"apple": 10, "orange": 5})
    sales_tuesday = collections.Counter({"apple": 2, "orange": 3})
    total_sales = sales_monday + sales_tuesday
    print(f"Total Sales: {total_sales}")


    # ==========================================
    # PART 5: PERFORMANCE SHOWDOWN (List vs Dict)
    # ==========================================
    section("PART 5: Performance (The O(1) Magic)")
    
    size = 1_000_000
    print(f"Generating dataset of {size:,} items...")
    
    # Create a list and a set (sets use hashmap logic internally)
    haystack_list = list(range(size))
    haystack_dict = {i: True for i in range(size)}
    
    target = size - 1 # Look for the very last item (Worst case for list)
    
    # Test List Search
    t0 = time.time()
    found = target in haystack_list # Scans 0 to 999,999 one by one
    t1 = time.time()
    print(f"List Search Time: {t1-t0:.6f} sec (Slow, O(n))")
    
    # Test Dict Search
    t2 = time.time()
    found = target in haystack_dict # Jumps directly to memory address
    t3 = time.time()
    print(f"Dict Search Time: {t3-t2:.6f} sec (Instant, O(1))")
    
    speedup = (t1-t0) / (t3-t2)
    print(f"\nConclusion: Hashmap lookup is ~{speedup:.0f}x faster here.")

if __name__ == "__main__":
    master_hashmaps()