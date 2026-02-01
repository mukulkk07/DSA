import random
import secrets
import time
import collections

# Try importing numpy for scientific randomness
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def master_randomness():
    """
    A comprehensive guide to Randomness in Python:
    1. Basic PRNG (Pseudo-Random Number Generation)
    2. Reproducibility (The Seed)
    3. Selection & Shuffling (Games & Logic)
    4. Weighted Probability (Biased Randomness)
    5. Cryptographic Security (secrets vs random)
    6. Scientific Distributions (Gaussian/Normal)
    """

    # ==========================================
    # PART 1: THE BASICS (random module)
    # ==========================================
    section("PART 1: The Basics (Uniform Distribution)")
    
    # 1. Float between 0.0 and 1.0
    # The foundation of almost all random logic
    r_float = random.random()
    print(f"Random Float (0.0-1.0): {r_float:.6f}")
    
    # 2. Integer Range (Inclusive)
    # Good for rolling dice
    r_int = random.randint(1, 6)
    print(f"Dice Roll (1-6): {r_int}")
    
    # 3. Float Range
    # Good for physical simulations (e.g., angle, temperature)
    r_uniform = random.uniform(10.5, 20.5)
    print(f"Random Temperature (10.5-20.5): {r_uniform:.2f}")


    # ==========================================
    # PART 2: THE "SEED" (Controlling Chaos)
    # ==========================================
    section("PART 2: Seeding (Reproducibility)")
    
    # If you are debugging code, you want the "random" errors to happen 
    # the exact same way every time. You do this by setting the seed.
    
    print("Run A (Seed 42):")
    random.seed(42)
    print(f" -> {random.randint(1, 100)}, {random.randint(1, 100)}")
    
    print("Run B (Seed 99):")
    random.seed(99)
    print(f" -> {random.randint(1, 100)}, {random.randint(1, 100)}")
    
    print("Run C (Seed 42 again - Watch numbers repeat!):")
    random.seed(42)
    print(f" -> {random.randint(1, 100)}, {random.randint(1, 100)}")
    
    # Reset seed to system time for actual randomness
    random.seed() 


    # ==========================================
    # PART 3: SELECTION & SHUFFLING
    # ==========================================
    section("PART 3: Selection & Shuffling")
    
    deck = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
    
    # 1. Pick One (Choice)
    card = random.choice(deck)
    print(f"Picked 1 card: {card}")
    
    # 2. Pick Multiple with Replacement (Choices)
    # Like rolling a dice twice (you can get 6 twice)
    hand_replace = random.choices(deck, k=3)
    print(f"Pick 3 (Replacement allowed): {hand_replace}")
    
    # 3. Pick Multiple UNIQUE (Sample)
    # Like dealing cards (cannot get the Ace twice)
    hand_unique = random.sample(deck, k=3)
    print(f"Pick 3 (Unique): {hand_unique}")
    
    # 4. Shuffle (In-Place)
    # Warning: This modifies the original list! returns None.
    print(f"Deck before shuffle: {deck}")
    random.shuffle(deck)
    print(f"Deck after shuffle:  {deck}")


    # ==========================================
    # PART 4: WEIGHTED PROBABILITY
    # ==========================================
    section("PART 4: Weighted Choice (Bias)")
    
    # Scenario: A Loot Box in a game.
    # Common item: 60% chance, Rare: 30%, Legendary: 10%
    loot_table = ["Common", "Rare", "Legendary"]
    probabilities = [60, 30, 10]
    
    # Simulate opening 100 boxes
    results = random.choices(loot_table, weights=probabilities, k=100)
    counts = collections.Counter(results)
    
    print(f"Opened 100 boxes with weights {probabilities}:")
    print(dict(counts))


    # ==========================================
    # PART 5: SECURITY (secrets vs random)
    # ==========================================
    section("PART 5: Cryptography (secrets module)")
    
    # WARNING: NEVER use 'random' for passwords or API keys.
    # It is predictable. Use 'secrets' instead.
    
    # 1. Generate a secure token for a Password Reset URL
    token = secrets.token_urlsafe(16)
    print(f"Secure Token: https://mysite.com/reset?token={token}")
    
    # 2. Secure Hex (Good for API Keys)
    api_key = secrets.token_hex(32)
    print(f"API Key: {api_key}")


    # ==========================================
    # PART 6: SCIENTIFIC DISTRIBUTIONS (NumPy)
    # ==========================================
    section("PART 6: Distributions (Normal/Gaussian)")
    
    if HAS_NUMPY:
        # random.random() gives a "Uniform" distribution (flat).
        # Real life (Heights, IQ, Errors) follows a "Normal" (Bell Curve) distribution.
        
        # Mean (average) = 100, Standard Deviation = 15 (IQ scores)
        iq_scores = np.random.normal(100, 15, 1000)
        
        print(f"Generated 1,000 IQ scores.")
        print(f"Average: {np.mean(iq_scores):.2f}")
        print(f"Min: {np.min(iq_scores):.2f}")
        print(f"Max: {np.max(iq_scores):.2f}")
        
    else:
        print("NumPy not installed. Skipping Scientific Distributions.")
        # Native Python approximation of Gaussian
        # random.gauss(mu, sigma) exists!
        print("Using native random.gauss instead:")
        val = random.gauss(100, 15)
        print(f"Single IQ score: {val:.2f}")

if __name__ == "__main__":
    master_randomness()