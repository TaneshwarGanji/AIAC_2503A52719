'''class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return len(self.items) == 0
print("Stack implementation initialized.")
print("You can use the push, pop, peek, and is_empty methods to interact with the stack.")
print("Example usage:")
stack = Stack()
stack.push(1)
stack.push(2)
print("Top item after pushing 1 and 2:", stack.peek())  # Output: 2
print("Popped item:", stack.pop())  # Output: 2
print("Is stack empty?", stack.is_empty())  # Output: False'''



