import collections

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

# ==========================================
# PART 1: THE NODE (The Building Block)
# ==========================================
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None   # Pointer to left child (Smaller)
        self.right = None  # Pointer to right child (Larger)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ==========================================
    # PART 2: INSERTION (Recursive)
    # ==========================================
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        # 1. Go Left?
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        # 2. Go Right?
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)
        # 3. Value exists? Do nothing (No duplicates in this BST)

    # ==========================================
    # PART 3: SEARCHING (The Superpower)
    # ==========================================
    def contains(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False # Hit the bottom, didn't find it
        if value == node.value:
            return True  # Found it!
        
        # Decide direction
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    # ==========================================
    # PART 4: DEPTH FIRST TRAVERSALS (DFS)
    # ==========================================
    # In-Order: Left -> Root -> Right (Sorts the data!)
    def print_in_order(self):
        print("In-Order (Sorted): ", end="")
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.left)  # Visit Left
            print(f"{node.value}", end=" ")      # Visit Root
            self._in_order_recursive(node.right) # Visit Right

    # Pre-Order: Root -> Left -> Right (Good for copying trees)
    def print_pre_order(self):
        print("Pre-Order (Structure): ", end="")
        self._pre_order_recursive(self.root)
        print()

    def _pre_order_recursive(self, node):
        if node:
            print(f"{node.value}", end=" ")      # Visit Root
            self._pre_order_recursive(node.left) # Visit Left
            self._pre_order_recursive(node.right)# Visit Right

    # ==========================================
    # PART 5: BREADTH FIRST TRAVERSAL (BFS)
    # ==========================================
    def print_level_order(self):
        # Uses a Queue to traverse level by level (Top to Bottom)
        if not self.root:
            return
        
        queue = collections.deque([self.root])
        print("Level-Order (BFS): ", end="")
        
        while queue:
            current = queue.popleft()
            print(f"{current.value}", end=" ")
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

    # ==========================================
    # PART 6: VISUALIZATION (Pretty Print)
    # ==========================================
    def print_tree(self):
        # A recursive helper to print the tree structure visually
        print("\nVisual Structure:")
        self._print_structure(self.root, 0)

    def _print_structure(self, node, level):
        if node is None:
            return
        # Print Right side first (so it appears on top)
        self._print_structure(node.right, level + 1)
        # Print current node
        print("    " * level + f"-> {node.value}")
        # Print Left side
        self._print_structure(node.left, level + 1)

# ==========================================
# PART 7: EXECUTION
# ==========================================
if __name__ == "__main__":
    
    # 1. Setup
    bst = BinarySearchTree()
    # We insert numbers in a random-ish order to make the tree interesting.
    # If we inserted 1,2,3,4,5 it would just be a line (linked list)!
    numbers = [50, 30, 70, 20, 40, 60, 80]
    
    section("1. Building the Tree")
    print(f"Inserting: {numbers}")
    for n in numbers:
        bst.insert(n)
        
    bst.print_tree()
    
    section("2. Searching")
    print(f"Contains 40? {bst.contains(40)}")
    print(f"Contains 99? {bst.contains(99)}")
    
    section("3. Traversals (Reading the data)")
    # Notice: In-Order automatically sorts the data!
    bst.print_in_order()   # 20 30 40 50 60 70 80
    bst.print_pre_order()  # 50 30 20 40 70 60 80
    bst.print_level_order()# 50 30 70 20 40 60 80