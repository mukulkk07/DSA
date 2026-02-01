import time
import heapq
from collections import deque
from queue import Queue

def section(title):
    print(f"\n{'-'*10} {title} {'-'*10}")

def master_queues():
    """
    A comprehensive guide to Queues:
    1. The Performance Trap (Lists)
    2. The Standard Queue (Deque)
    3. The Thread-Safe Queue
    4. The Priority Queue
    """

    # ==========================================
    # PART 1: THE PERFORMANCE TRAP (List vs Deque)
    # ==========================================
    section("PART 1: The Trap (Why NOT to use List)")
    
    # We will simulate a queue with 100,000 items.
    N = 100_000
    
    # --- BAD WAY (List) ---
    bad_queue = list(range(N))
    start = time.time()
    while bad_queue:
        # pop(0) forces Python to shift N-1 elements every single time!
        # This is O(n) complexity per pop.
        bad_queue.pop(0) 
    end = time.time()
    print(f"List Queue (pop(0)) time: {end - start:.4f} seconds")

    # --- GOOD WAY (Deque) ---
    # Deque (Double Ended Queue) is optimized for adding/removing from ends.
    good_queue = deque(range(N))
    start = time.time()
    while good_queue:
        # popleft() is O(1). No shifting required.
        good_queue.popleft()
    end = time.time()
    print(f"Deque Queue (popleft) time: {end - start:.4f} seconds")
    print("Notice the massive speed difference!")


    # ==========================================
    # PART 2: THE STANDARD QUEUE (Deque Implementation)
    # ==========================================
    section("PART 2: The Standard Queue (Deque)")
    
    # In 99% of single-threaded Python scripts, use collections.deque
    
    queue = deque()
    
    # ENQUEUE (Add to rear)
    print("Enqueueing: Alice, Bob, Charlie")
    queue.append("Alice")
    queue.append("Bob")
    queue.append("Charlie")
    
    # PEEK (Look at front)
    print(f"Front of line: {queue[0]}")
    
    # DEQUEUE (Remove from front)
    served = queue.popleft()
    print(f"Served: {served}")
    print(f"Next in line: {queue[0]}")
    print(f"Remaining Queue: {queue}")


    # ==========================================
    # PART 3: THE THREAD-SAFE QUEUE
    # ==========================================
    section("PART 3: Thread-Safe Queue (queue.Queue)")
    
    # Used when you have "Producer" threads creating work and "Consumer" threads
    # processing it. It handles locking automatically.
    
    ts_queue = Queue(maxsize=3) # Limit size to 3 items
    
    ts_queue.put("Task 1")
    ts_queue.put("Task 2")
    ts_queue.put("Task 3")
    
    # ts_queue.put("Task 4") -> This would BLOCK (freeze) the program until space opens up!
    
    print(f"Thread-Safe Queue Full? {ts_queue.full()}")
    print(f"Processing: {ts_queue.get()}")
    print(f"Processing: {ts_queue.get()}")
    
    # .task_done() is often used to track progress in threaded apps
    ts_queue.task_done() 
    ts_queue.task_done()


    # ==========================================
    # PART 4: THE PRIORITY QUEUE
    # ==========================================
    section("PART 4: Priority Queue (Ordering by Importance)")
    
    # Sometimes FIFO isn't what you want. You want the "most important" item first.
    # We use 'heapq' (Min-Heap) for this.
    # Python sorts tuples by the first item. Format: (priority, data)
    
    # Lower number = Higher priority
    tasks = []
    
    heapq.heappush(tasks, (3, "Clean Desk"))   # Priority 3 (Low)
    heapq.heappush(tasks, (1, "Fix Server"))   # Priority 1 (Critical)
    heapq.heappush(tasks, (2, "Reply Email"))  # Priority 2 (Medium)
    
    print("Tasks in queue (Unsorted view):", tasks)
    
    # Popping will always return the smallest number (highest priority)
    print(f"Doing first: {heapq.heappop(tasks)}") # Should be Fix Server
    print(f"Doing next:  {heapq.heappop(tasks)}") # Should be Reply Email
    print(f"Doing last:  {heapq.heappop(tasks)}") # Should be Clean Desk


    # ==========================================
    # PART 5: REAL WORLD APPLICATION (Print Spooler)
    # ==========================================
    section("PART 5: Application - Print Spooler Simulation")
    
    class PrintSpooler:
        def __init__(self):
            self.queue = deque()
            
        def add_job(self, document):
            print(f"[Input] Added '{document}' to spooler.")
            self.queue.append(document)
            
        def process_job(self):
            if not self.queue:
                print("[Printer] No jobs to print.")
                return
            
            job = self.queue.popleft()
            print(f"[Printer] Printing: '{job}'... Done.")

    spooler = PrintSpooler()
    spooler.add_job("Tax_Returns.pdf")
    spooler.add_job("Vacation_Photo.jpg")
    
    spooler.process_job() # Prints Tax Returns
    spooler.add_job("Resume.docx") # New job comes in while printing
    
    spooler.process_job() # Prints Vacation Photo
    spooler.process_job() # Prints Resume

if __name__ == "__main__":
    master_queues()