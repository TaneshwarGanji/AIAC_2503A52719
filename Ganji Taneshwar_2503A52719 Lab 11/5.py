import heapq


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0

    def enqueue(self, priority, value=None):
        """Add an item to the queue with the given priority."""
        if value is None:
            value = priority
        heapq.heappush(self._heap, (-priority, self._counter, value))
        self._counter += 1

    def dequeue(self):
        """Remove and return the item with the highest priority."""
        if not self._heap:
            raise IndexError("dequeue from empty priority queue")
        _, _, value = heapq.heappop(self._heap)
        return value

    def display(self):
        """Return all queued items ordered by highest priority."""
        return [value for _, _, value in sorted(self._heap, key=lambda x: x[0])]
# Example usage:
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(3, "Task 3")
    pq.enqueue(1, "Task 1")
    pq.enqueue(2, "Task 2")

    print("Priority Queue contents (highest priority first):", pq.display())
    print("Dequeued item:", pq.dequeue())
    print("Priority Queue contents after dequeue:", pq.display())   
     
