class CoffeeShop:
    # Class Attribute: This belongs to the Class, not any specific object.
    # All coffee shops share this profit margin initially.
    profit_margin = 0.20  # 20%

    def __init__(self, name, city):
        # Instance Attributes: Specific to ONE shop object.
        self.name = name
        self.city = city
        self.orders = 0
        print(f"--- Opened new branch: {self.name} in {self.city} ---")

    # ==========================================
    # 1. INSTANCE METHOD
    # ==========================================
    # Characteristics:
    # - Receives 'self' as the first argument.
    # - Can access/modify the specific object's data (self.orders).
    # - Can access class state (self.profit_margin).
    def make_coffee(self, price):
        self.orders += 1
        # Calculate profit using the class attribute
        profit = price * self.profit_margin
        print(f"[{self.name}] Brewing coffee... Sold for ${price}. Profit: ${profit:.2f}")

    # ==========================================
    # 2. CLASS METHOD
    # ==========================================
    # Characteristics:
    # - Uses the @classmethod decorator.
    # - Receives 'cls' (The Class itself) as the first argument, not 'self'.
    # - Can modify class state that applies to ALL instances.
    # - Cannot access specific instance data (like self.name).
    @classmethod
    def set_profit_margin(cls, new_margin):
        print(f"\n[Headquarters] Changing global profit margin to {new_margin * 100}%...")
        cls.profit_margin = new_margin

    @classmethod
    def create_franchise_nyc(cls, name):
        """A common use of Class Methods is as 'Alternative Constructors'"""
        return cls(name, "New York")

    # ==========================================
    # 3. STATIC METHOD
    # ==========================================
    # Characteristics:
    # - Uses the @staticmethod decorator.
    # - Receives neither 'self' nor 'cls'.
    # - It works like a regular function but belongs inside the class's namespace
    #   because it is logically related to Coffee Shops.
    @staticmethod
    def check_temperature(temp):
        if temp > 95:
            return "Too Hot! (Burnt beans)"
        elif temp < 85:
            return "Too Cold! (Underextracted)"
        else:
            return "Perfect Temperature."


# ==========================================
# Main Execution Block
# ==========================================
if __name__ == "__main__":
    # --- 1. Using Static Methods (Utility) ---
    # We don't need a shop object to check if water temp is okay.
    print(f"Temp Check 90C: {CoffeeShop.check_temperature(90)}")
    print(f"Temp Check 100C: {CoffeeShop.check_temperature(100)}\n")

    # --- 2. Using Instance Methods ---
    shop_a = CoffeeShop("StarCapa", "Seattle")
    shop_b = CoffeeShop("JavaBean", "Boston")

    shop_a.make_coffee(5.00)  # Uses 20% margin
    shop_b.make_coffee(5.00)  # Uses 20% margin

    # --- 3. Using Class Methods (Global Change) ---
    # The HQ decides to increase profit margins.
    # We call this on the Class, not the object (though you can call it on objects too).
    CoffeeShop.set_profit_margin(0.30)

    # Now, ALL shops (existing and new) are affected.
    print("   -> (Shop A sells another coffee with new margin)")
    shop_a.make_coffee(5.00)

    # --- 4. Class Method as a Constructor ---
    # Creating a new object using a factory logic defined in the class method
    shop_c = CoffeeShop.create_franchise_nyc("EmpireBrew")