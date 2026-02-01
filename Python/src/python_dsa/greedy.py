import sys

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

def master_greedy():
    """
    A comprehensive guide to Greedy Algorithms:
    1. The Concept (Explained)
    2. Success Case 1: Fractional Knapsack (Take the most valuable chunks)
    3. Success Case 2: Activity Selection (Do the most tasks possible)
    4. FAILURE Case: Coin Change (When Greedy is wrong)
    """

    # ==========================================
    # PART 1: THE PHILOSOPHY
    # ==========================================
    section("PART 1: The Philosophy")
    print("Strategy: Always choose the local optimum.")
    print("Advantage: Extremely fast.")
    print("Disadvantage: Can get stuck in 'local maxima' and miss the true answer.")


    # ==========================================
    # PART 2: SUCCESS CASE - FRACTIONAL KNAPSACK
    # ==========================================
    section("PART 2: Fractional Knapsack (Greedy Works!)")
    
    # Problem: You have a bag with capacity W. You want to maximize value.
    # You CAN cut items (like Gold dust, Silver powder).
    # Rule: Always take the item with the highest VALUE PER WEIGHT unit first.
    
    # Format: (Value, Weight)
    items = [
        (60, 10),  # Value 60, Weight 10 -> Ratio 6.0
        (100, 20), # Value 100, Weight 20 -> Ratio 5.0
        (120, 30)  # Value 120, Weight 30 -> Ratio 4.0
    ]
    capacity = 50
    
    def fractional_knapsack(items, capacity):
        # 1. Calculate ratios and Sort by Ratio (Highest first)
        # We add the index to keep track
        # (ratio, value, weight)
        ratio_list = [(v/w, v, w) for v, w in items]
        ratio_list.sort(key=lambda x: x[0], reverse=True)
        
        total_value = 0
        current_weight = 0
        
        print(f"Items sorted by value-density: {ratio_list}")
        
        for ratio, val, wt in ratio_list:
            if current_weight + wt <= capacity:
                # Take the whole item
                current_weight += wt
                total_value += val
                print(f" -> Took full item (Val: {val}, Wt: {wt})")
            else:
                # Take a fraction of the item
                remain = capacity - current_weight
                fraction = remain / wt
                value_added = val * fraction
                
                current_weight += remain
                total_value += value_added
                print(f" -> Took {fraction:.2f} of item (Val: {val}) = {value_added:.2f}")
                break # Knapsack is full
                
        return total_value

    max_val = fractional_knapsack(items, capacity)
    print(f"Total Value Collected: {max_val}")


    # ==========================================
    # PART 3: SUCCESS CASE - ACTIVITY SELECTION
    # ==========================================
    section("PART 3: Activity Selection (Interval Scheduling)")
    
    # Problem: You have many meetings with (start, end) times.
    # You want to attend as many as possible. You cannot be in two at once.
    # Rule: Always pick the meeting that ENDS EARLIEST (leaving more time for others).
    
    # (Start, End)
    meetings = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    
    def select_activities(meetings):
        # 1. Sort by FINISH time
        # If we sorted by start time, we might pick a meeting that lasts all day!
        sorted_meetings = sorted(meetings, key=lambda x: x[1])
        
        selected = []
        last_end_time = -1
        
        for start, end in sorted_meetings:
            if start >= last_end_time:
                selected.append((start, end))
                last_end_time = end # Update our availability
        
        return selected

    schedule = select_activities(meetings)
    print(f"All Meetings: {meetings}")
    print(f"Optimal Schedule: {schedule}")
    print(f"Count: {len(schedule)}")


    # ==========================================
    # PART 4: FAILURE CASE - COIN CHANGE
    # ==========================================
    section("PART 4: The Failure (Coin Change)")
    
    # Problem: Make change for target amount using fewest coins.
    # Standard Coins: [1, 5, 10, 25] -> Greedy works perfectly here.
    # Weird Coins: [1, 3, 4] -> Greedy FAILS here.
    
    target = 6
    coins = [1, 3, 4]
    
    print(f"Target: {target}")
    print(f"Coins Available: {coins}")
    
    # --- GREEDY ATTEMPT ---
    def greedy_coin_change(coins, target):
        # Sort largest to smallest
        coins = sorted(coins, reverse=True)
        count = 0
        details = []
        remainder = target
        
        for coin in coins:
            while remainder >= coin:
                remainder -= coin
                count += 1
                details.append(coin)
        
        return count, details

    g_count, g_coins = greedy_coin_change(coins, target)
    print(f"\nGreedy Logic: Pick largest coin (4), then remaining is 2. Pick (1), (1).")
    print(f"Greedy Result: {g_count} coins -> {g_coins}")
    
    # --- OPTIMAL REALITY ---
    print("\nActual Optimal Solution: Pick (3) and (3).")
    print("Optimal Result: 2 coins -> [3, 3]")
    print("Conclusion: Greedy FAILED because taking '4' blocked the better solution.")

if __name__ == "__main__":
    master_greedy()