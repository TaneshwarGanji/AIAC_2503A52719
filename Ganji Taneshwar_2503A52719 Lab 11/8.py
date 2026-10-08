"""Smart Online Shopping System

This program demonstrates the order-processing feature using a FIFO queue.
Orders are processed in the exact sequence they are placed, which matches
customer requirements and ensures fair handling.
"""

from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class Order:
    """Represents a customer order."""
    order_id: str
    product_id: str
    quantity: int


class OrderQueue:
    """A FIFO queue for processing orders in their placement order."""

    def __init__(self) -> None:
        self._orders = deque()

    def place_order(self, order: Order) -> None:
        """Add an order to the back of the queue."""
        self._orders.append(order)

    def process_next_order(self) -> Optional[Order]:
        """Remove and return the next order, or None when the queue is empty."""
        if not self._orders:
            return None
        return self._orders.popleft()

    def __len__(self) -> int:
        """Return the number of orders waiting to be processed."""
        return len(self._orders)

    def __bool__(self) -> bool:
        """Return True when the queue contains orders."""
        return bool(self._orders)


# Feature selection table
FEATURE_TABLE = {
    "Shopping Cart Management": {
        "Data Structure": "Deque",
        "Justification": "A deque supports efficient additions and removals from both ends, "
                         "which is useful for dynamic cart operations and undoing recent actions."
    },
    "Order Processing System": {
        "Data Structure": "Queue",
        "Justification": "A queue follows FIFO order, so orders are processed in the same sequence "
                         "they were placed. It also provides O(1) enqueue and dequeue operations."
    },
    "Top-Selling Products Tracker": {
        "Data Structure": "Priority Queue",
        "Justification": "A priority queue can quickly retrieve the product with the highest sales count. "
                         "It is suitable when products must be ranked dynamically by popularity."
    },
    "Product Search Engine": {
        "Data Structure": "Binary Search Tree (BST)",
        "Justification": "A BST allows fast lookup, insertion, and deletion using product ID comparisons. "
                         "Average-case search time is O(log n), making it efficient for large catalogs."
    },
    "Delivery Route Planning": {
        "Data Structure": "Linked List",
        "Justification": "A linked list can represent a sequence of warehouses and delivery locations. "
                         "It supports easy insertion and traversal between connected route nodes."
    },
}


def display_table() -> None:
    """Print the feature-to-data-structure mapping and justification."""
    print("Feature → Chosen Data Structure → Justification")
    print("-" * 80)
    for feature, details in FEATURE_TABLE.items():
        print(f"{feature:<30} | {details['Data Structure']:<26} | {details['Justification']}")


def demonstrate_queue() -> None:
    """Show the queue processing system with sample orders."""
    queue = OrderQueue()
    orders = [
        Order("ORD-1001", "P-101", 2),
        Order("ORD-1002", "P-205", 1),
        Order("ORD-1003", "P-101", 3),
    ]

    for order in orders:
        queue.place_order(order)
        print(f"Placed: {order.order_id} -> {order.product_id} ({order.quantity})")

    print("\nProcessing orders:")
    while queue:
        order = queue.process_next_order()
        print(f"Processed: {order.order_id} -> {order.product_id} ({order.quantity})")


if __name__ == "__main__":
    print("Smart Online Shopping System")
    print("=" * 80)
    display_table()
    print("\n" + "=" * 80)
    demonstrate_queue()
