import collections

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

class Graph:
    def __init__(self):
        # Adjacency List: {'A': ['B', 'C'], 'B': ['D'], ...}
        self.graph = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u) # Undirected Graph

    # ==========================================
    # PART 1: BFS (Breadth-First Search)
    # ==========================================
    def bfs_traversal(self, start_node):
        """
        Uses a QUEUE (First-In, First-Out).
        Explores layer by layer.
        """
        visited = set()
        queue = collections.deque([start_node])
        visited.add(start_node)
        
        order = []
        
        while queue:
            # DEQUEUE: Remove from the front
            current = queue.popleft()
            order.append(current)
            
            # ENQUEUE: Add unvisited neighbors to the back
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return order

    def bfs_shortest_path(self, start, end):
        """
        BFS is the ONLY algorithm that guarantees the shortest path
        in an unweighted graph (least number of hops).
        """
        queue = collections.deque([[start]]) # Store PATHS, not just nodes
        visited = set([start])
        
        while queue:
            path = queue.popleft() # Get the path waiting longest
            current_node = path[-1]
            
            if current_node == end:
                return path # Found it! First one found is shortest.
            
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return None

    # ==========================================
    # PART 2: DFS (Depth-First Search)
    # ==========================================
    def dfs_recursive(self, start_node):
        """
        Uses the CALL STACK (Recursion).
        Dives deep immediately.
        """
        visited = set()
        order = []
        
        def _dfs_helper(node):
            visited.add(node)
            order.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    _dfs_helper(neighbor)
        
        _dfs_helper(start_node)
        return order

    def dfs_iterative(self, start_node):
        """
        Uses an explicit STACK (Last-In, First-Out).
        Useful to avoid recursion depth limits.
        """
        visited = set()
        stack = [start_node] # Push
        order = []
        
        while stack:
            # POP: Remove from the top (end of list)
            current = stack.pop()
            
            if current not in visited:
                visited.add(current)
                order.append(current)
                
                # Add neighbors to stack.
                # Note: We reverse them so the first neighbor is popped first 
                # (mimicking left-to-right recursion order)
                for neighbor in reversed(self.graph[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order


# ==========================================
# PART 3: EXECUTION & COMPARISON
# ==========================================
def master_bfs_dfs():
    # 1. Setup a Graph
    # Structure:
    #       A
    #     /   \
    #    B     C
    #   / \     \
    #  D   E     F
    
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    
    section("Graph Structure")
    print("      A")
    print("    /   \\")
    print("   B     C")
    print("  / \\     \\")
    print(" D   E     F")

    # 2. Compare Traversals
    section("Traversal Comparison")
    
    # BFS: Should be A, then (B, C), then (D, E, F)
    # Layer 1 -> Layer 2 -> Layer 3
    print(f"BFS Order (Layers):    {g.bfs_traversal('A')}")
    
    # DFS: Should be A -> B -> D ... (Dives deep left first)
    print(f"DFS Order (Recursive): {g.dfs_recursive('A')}")
    print(f"DFS Order (Iterative): {g.dfs_iterative('A')}")
    
    # 3. The BFS Superpower (Shortest Path)
    section("Shortest Path (BFS)")
    
    # Let's add a long path to make it interesting
    # A -> C -> F -> G -> H -> D (Connects D back to the right side)
    g.add_edge('F', 'G')
    g.add_edge('G', 'H')
    g.add_edge('H', 'D')
    
    print("Goal: Go from 'A' to 'D'")
    
    # DFS might go A -> C -> F -> G -> H -> D (Long way!)
    # BFS will find A -> B -> D (Direct way!)
    
    bfs_path = g.bfs_shortest_path('A', 'D')
    print(f"BFS found Shortest Path: {bfs_path} (Length: {len(bfs_path)-1})")
    print("Note: BFS found the direct path via 'B', ignoring the long loop via 'C'.")

if __name__ == "__main__":
    master_bfs_dfs()