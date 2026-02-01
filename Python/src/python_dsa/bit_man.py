def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def bin8(n):
    """Helper to display number as 8-bit binary (handling negatives for viz)"""
    return f"{n & 0xff:08b} (Decimal: {n})"

def master_bit_manipulation():
    """
    A comprehensive guide to Bit Manipulation:
    1. The Logical Operators (&, |, ^, ~)
    2. The Shifts (<<, >>)
    3. Bit Masking (Set, Clear, Toggle, Check)
    4. Two's Complement (How Python handles negatives)
    5. Famous Tricks (Power of 2, Swapping, Counting bits)
    """

    # ==========================================
    # PART 1: THE LOGIC GATES
    # ==========================================
    section("PART 1: Logic Gates")
    
    a = 0b1100 # 12
    b = 0b1010 # 10
    
    print(f"a = {bin8(a)}")
    print(f"b = {bin8(b)}")
    
    # AND (&): Both must be 1
    print(f"a & b (AND): {bin8(a & b)} -> Intersection")
    
    # OR (|): Either can be 1
    print(f"a | b (OR):  {bin8(a | b)} -> Union")
    
    # XOR (^): Different bits = 1, Same bits = 0
    # Crucial property: x ^ x = 0
    print(f"a ^ b (XOR): {bin8(a ^ b)} -> Difference")
    
    # NOT (~): Flips all bits (0->1, 1->0)
    # Formula: ~x = -x - 1
    print(f"~a    (NOT): {bin8(~a)} -> Inversion")


    # ==========================================
    # PART 2: SHIFTING (Math Shortcuts)
    # ==========================================
    section("PART 2: Bit Shifting")
    
    x = 5 # 00000101
    print(f"Original:   {bin8(x)}")
    
    # Left Shift (<<): Multiply by 2^k
    # 5 << 1 = 10, 5 << 2 = 20
    print(f"x << 1:     {bin8(x << 1)} (Multiply by 2)")
    print(f"x << 2:     {bin8(x << 2)} (Multiply by 4)")
    
    # Right Shift (>>): Floor Divide by 2^k
    y = 20
    print(f"y >> 1:     {bin8(y >> 1)} (20 // 2 = 10)")
    print(f"y >> 2:     {bin8(y >> 2)} (20 // 4 = 5)")


    # ==========================================
    # PART 3: BIT MASKS (The Toolbox)
    # ==========================================
    section("PART 3: Masking (Get/Set/Clear/Toggle)")
    
    # Imagine these bits represent 4 settings: [Sound, Video, Chat, Mic]
    # Current State: 0101 (Video ON, Mic ON)
    state = 0b0101
    print(f"Start State: {bin8(state)}")
    
    # 1. CHECK a bit (Using &)
    # Is the 0-th bit (Mic) ON?
    # We create a mask with only the 0-th bit set (1 << 0)
    if (state & (1 << 0)):
        print(" -> Mic is ON")
    else:
        print(" -> Mic is OFF")
        
    # 2. SET a bit (Using |)
    # Turn Sound (3rd bit) ON. Mask: 1000 (1 << 3)
    state = state | (1 << 3)
    print(f"Set Bit 3:   {bin8(state)} (Sound turned ON)")
    
    # 3. CLEAR a bit (Using & ~)
    # Turn Mic (0-th bit) OFF.
    # We want a mask like 11111110. This is ~(1 << 0).
    state = state & ~(1 << 0)
    print(f"Clear Bit 0: {bin8(state)} (Mic turned OFF)")
    
    # 4. TOGGLE a bit (Using ^)
    # Flip Video (2nd bit). If ON->OFF, if OFF->ON.
    state = state ^ (1 << 2)
    print(f"Toggle Bit 2:{bin8(state)} (Video flipped)")


    # ==========================================
    # PART 4: FAMOUS TRICKS (Interview Gold)
    # ==========================================
    section("PART 4: Algorithmic Magic")
    
    # Trick A: Check if number is Even or Odd
    # Odd numbers always have the last bit as 1.
    num = 13
    is_odd = (num & 1) == 1
    print(f"Is {num} odd? {is_odd}")
    
    # Trick B: Swapping without a temp variable
    # Uses the property that (a ^ b) ^ a = b
    a, b = 45, 99
    print(f"\nBefore Swap: a={a}, b={b}")
    a = a ^ b
    b = a ^ b # effectively (a^b)^b = a
    a = a ^ b # effectively (a^b)^a = b
    print(f"After Swap:  a={a}, b={b} (No temp var!)")
    
    # Trick C: Check if Power of 2
    # Powers of 2 have exactly one '1' bit (1, 2, 4, 8 -> 1, 10, 100, 1000)
    # If n is a power of 2, then n & (n-1) is ALWAYS 0.
    # Example: 8 (1000) & 7 (0111) = 0000
    check_pow = 16
    is_pow2 = (check_pow > 0) and (check_pow & (check_pow - 1) == 0)
    print(f"\nIs {check_pow} power of 2? {is_pow2}")
    
    # Trick D: Kernighan's Algorithm (Count set bits)
    # n = n & (n-1) removes the lowest set bit.
    n = 0b101101 # has 4 ones
    count = 0
    print(f"\nCounting bits in {bin(n)}:")
    while n > 0:
        n = n & (n - 1)
        count += 1
        print(f" -> Removed lowest bit, remaining: {bin(n)}")
    print(f"Total Set Bits: {count}")

if __name__ == "__main__":
    master_bit_manipulation()