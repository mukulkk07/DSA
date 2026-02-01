import collections
import heapq  # Essential for Dijkstra's Algorithm

def section(title):
    print(f"\n{'='*10} {title} {'='*10}")

class Graph:
    def __init__(self, directed=False):
        """
        Adjacency List Implementation.
        self.graph = {
            'A': {'B': 5, 'C': 10},  # Node A connects to B (weight 5) and C (weight 10)
            'B': {'A': 5}
        }
        """
        self.graph = collections.defaultdict(dict)
        self.directed = directed

    # ==========================================
    # PART 1: CONSTRUCTION
    # ==========================================
    def add_edge(self, u, v, weight=1):
        """
        Connects node u to node v.
        If weighted, adds cost. If undirected, adds valid connection back.
        """
        self.graph[u][v] = weight
        if not self.directed:
            self.graph[v][u] = weight # Symmetry for undirected graphs

    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node} connects to -> {list(neighbors.items())}")

    # ==========================================
    # PART 2: BFS (Breadth-First Search)
    # ==========================================
    def bfs(self, start_node):
        """
        Explores neighbors, then neighbors of neighbors. (Layer by layer).
        Great for finding the shortest path in UNWEIGHTED graphs.
        """
        visited = set()
        queue = collections.deque([start_node])
        visited.add(start_node)
        
        traversal = []
        
        while queue:
            current = queue.popleft()
            traversal.append(current)
            
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return traversal

    # ==========================================
    # PART 3: DFS (Depth-First Search)
    # ==========================================
    def dfs(self, start_node):
        """
        Explores as deep as possible along each branch before backtracking.
        Great for mazes and puzzle solving.
        """
        visited = set()
        traversal = []
        
        def _dfs_recursive(node):
            visited.add(node)
            traversal.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    _dfs_recursive(neighbor)
        
        _dfs_recursive(start_node)
        return traversal

    # ==========================================
    # PART 4: DIJKSTRA'S ALGORITHM (Shortest Path)
    # ==========================================
    def shortest_path(self, start, end):
        """
        Finds the shortest path in a WEIGHTED graph.
        Uses a Min-Heap (Priority Queue) to always explore the cheapest node next.
        """
        # Priority Queue stores tuples: (current_cost, current_node)
        pq = [(0, start)]
        
        # Tracks the lowest cost found to reach each node
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        
        # To reconstruct the path, we remember where we came from
        previous_nodes = {node: None for node in self.graph}
        
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            
            # Optimization: If we found a shorter way to this node already, skip
            if current_dist > distances[current_node]:
                continue
            
            if current_node == end:
                break # We found the destination!
            
            # Check neighbors
            for neighbor, weight in self.graph[current_node].items():
                distance = current_dist + weight
                
                # If we found a cheaper path to the neighbor, update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
        
        return self._reconstruct_path(previous_nodes, start, end, distances[end])

    def _reconstruct_path(self, previous_nodes, start, end, final_cost):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse() # We tracked it backwards, so flip it
        
        return path, final_cost


# ==========================================
# PART 5: EXECUTION BLOCK
# ==========================================
def master_graphs():
    # 1. Build a Social Network (Undirected, Unweighted)
    section("1. Social Network (BFS/DFS)")
    social_net = Graph(directed=False)
    social_net.add_edge("Alice", "Bob")
    social_net.add_edge("Alice", "Charlie")
    social_net.add_edge("Bob", "Dave")
    social_net.add_edge("Charlie", "Eve")
    social_net.add_edge("Dave", "Eve") # A cycle!
    
    print("Structure:")
    social_net.print_graph()
    
    print(f"\nBFS (Layer-wise from Alice): {social_net.bfs('Alice')}")
    # Likely: Alice -> Bob, Charlie -> Dave, Eve
    
    print(f"DFS (Deep-dive from Alice):  {social_net.dfs('Alice')}")
    # Likely: Alice -> Bob -> Dave -> Eve -> Charlie (depends on dict order)

    # 2. Build a City Map (Weighted) for Navigation
    section("2. GPS Navigation (Dijkstra)")
    city_map = Graph(directed=False)
    
    # Edges represent roads with traffic cost (weight)
    city_map.add_edge("Home", "A", 5)
    city_map.add_edge("Home", "B", 2)  # B is closer initially
    city_map.add_edge("A", "Office", 10)
    city_map.add_edge("B", "C", 2)
    city_map.add_edge("C", "Office", 2) # Taking the "B-C" route is longer but faster!
    
    print("Map Connections:")
    city_map.print_graph()
    
    print("\nFinding fastest route from Home -> Office...")
    path, cost = city_map.shortest_path("Home", "Office")
    
    print(f"Optimal Path: {' -> '.join(path)}")
    print(f"Total Cost:   {cost} minutes")
    # Note: A Greedy algorithm might have picked Home->A because it connects directly,
    # but Dijkstra finds Home->B->C->Office is cheaper (2+2+2=6) vs (5+10=15).

if __name__ == "__main__":
    master_graphs()