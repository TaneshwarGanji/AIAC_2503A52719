from collections import deque


class DequeDS:
    """Double-ended queue implemented using collections.deque."""

    def __init__(self):
        """Initialize an empty deque."""
        self._queue = deque()

    def insert_front(self, value):
        """Insert a value at the front of the deque."""
        self._queue.appendleft(value)

    def insert_rear(self, value):
        """Insert a value at the rear of the deque."""
        self._queue.append(value)

    def remove_front(self):
        """Remove and return the value from the front of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._queue.popleft()

    def remove_rear(self):
        """Remove and return the value from the rear of the deque."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._queue.pop()

    def is_empty(self):
        """Return True if the deque is empty, otherwise False."""
        return len(self._queue) == 0

    def size(self):
        """Return the number of items in the deque."""
        return len(self._queue)

    def peek_front(self):
        """Return the front value without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._queue[0]

    def peek_rear(self):
        """Return the rear value without removing it."""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._queue[-1]
# Example usage:
if __name__ == "__main__":
    dq = DequeDS()
    dq.insert_rear("Task 1")
    dq.insert_front("Task 2")
    dq.insert_rear("Task 3")

    print("Deque contents (front to rear):", list(dq._queue))
    print("Removed from front:", dq.remove_front())
    print("Removed from rear:", dq.remove_rear())
    print("Deque contents after removals:", list(dq._queue))