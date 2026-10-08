'''class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
print("Queue implementation initialized.")
print("You can use the enqueue, dequeue, peek, size, and is_empty methods to interact with the queue.")     
#test the Queue implementation
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print("Front item after enqueueing 1 and 2:", queue.peek())  # Output: 1
print("Dequeued item:", queue.dequeue())  # Output: 1
print("Is queue empty?", queue.is_empty())  '''# Output: False


