class Node:
    """Represents a single node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list implementation with insertion and display."""

    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        """Print all values in the list in order."""
        current = self.head
        values = []

        while current is not None:
            values.append(str(current.data))
            current = current.next

        if values:
            print(" -> ".join(values))
        else:
            print("Linked list is empty")


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)
    linked_list.display()
