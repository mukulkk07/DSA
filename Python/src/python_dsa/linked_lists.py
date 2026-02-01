class Node:
    """
    The building block of a Linked List.
    It holds data and a reference (pointer) to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Initially, a node points to nothing

class LinkedList:
    """
    The manager class. It controls the 'head' (start) of the list.
    """
    def __init__(self):
        self.head = None
    
    # ==========================================
    # 1. TRAVERSAL & DISPLAY
    # ==========================================
    def __repr__(self):
        """Returns a string representation: 1 -> 2 -> 3 -> None"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __len__(self):
        """Allows use of len(my_list)"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ==========================================
    # 2. INSERTION
    # ==========================================
    def append(self, data):
        """Add to the END of the list. O(n) complexity."""
        new_node = Node(data)
        
        # Case 1: List is empty
        if not self.head:
            self.head = new_node
            return
        
        # Case 2: List has items, traverse to the end
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Add to the START of the list. O(1) complexity."""
        new_node = Node(data)
        new_node.next = self.head  # Point new node to current head
        self.head = new_node       # Update head to be new node

    def insert_after_node(self, prev_node_data, data):
        """Insert a new node after a specific node value."""
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_node_data} not found.")

    # ==========================================
    # 3. DELETION
    # ==========================================
    def delete_value(self, key):
        """Removes the first occurrence of a value."""
        current = self.head
        
        # Case 1: List is empty
        if not current:
            return

        # Case 2: The head is the node to delete
        if current.data == key:
            self.head = current.next
            current = None
            return

        # Case 3: Search for the node (keep track of previous)
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        # If key was not present
        if current is None:
            print(f"Value {key} not found in list.")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    # ==========================================
    # 4. ADVANCED OPERATIONS (Interview Favorites)
    # ==========================================
    def reverse(self):
        """Reverses the linked list in-place. O(n)."""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # 1. Save next
            current.next = prev       # 2. Reverse pointer
            prev = current            # 3. Move prev forward
            current = next_node       # 4. Move current forward
        self.head = prev

    def has_cycle(self):
        """
        Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
        Detects if the list loops back on itself.
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            if slow == fast:
                return True
        return False

# ==========================================
# 5. EXECUTION BLOCK
# ==========================================
if __name__ == "__main__":
    print("--- Linked List Master Program ---")
    
    ll = LinkedList()
    
    print("\n1. Building the list...")
    ll.append("A")
    ll.append("B")
    ll.append("C")
    ll.prepend("Start")
    print(f"Current List: {ll}")  # Uses __repr__
    
    print("\n2. Inserting 'X' after 'B'...")
    ll.insert_after_node("B", "X")
    print(f"Current List: {ll}")

    print("\n3. Deleting 'A'...")
    ll.delete_value("A")
    print(f"Current List: {ll}")
    
    print("\n4. Reversing the list...")
    ll.reverse()
    print(f"Reversed List: {ll}")
    
    print("\n5. Testing Cycle Detection...")
    print(f"Has Cycle? {ll.has_cycle()}")
    
    # Artificially create a cycle for testing (Danger zone!)
    # Point the last node back to the head
    print("Creating artificial cycle (connecting Tail -> Head)...")
    curr = ll.head
    while curr.next:
        curr = curr.next
    curr.next = ll.head
    
    print(f"Has Cycle? {ll.has_cycle()}")