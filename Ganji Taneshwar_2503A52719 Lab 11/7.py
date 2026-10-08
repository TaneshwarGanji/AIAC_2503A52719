"""Campus Resource Management System

Feature selection and justification:

1. Student Attendance Tracking — Queue
   A queue keeps a record of students in arrival order, which is useful for
   processing entry and exit logs. It also supports FIFO operations, making it
   suitable for tracking check-ins in sequence.

2. Event Registration System — Hash Table
   A hash table provides O(1) average-time lookup, insertion, and deletion by
   participant ID, allowing quick search and removal. It also keeps participant
   records organized for efficient access.

3. Library Book Borrowing — Linked List
   A linked list can store books in a flexible sequence and supports easy
   insertion and removal when borrowing records change. It is useful when the
   number of borrowed books varies dynamically.

4. Bus Scheduling System — Graph
   A graph represents stops as nodes and routes as connections, making it
   suitable for planning routes and finding connections between stops. It can
   also support route optimization and travel-time analysis.

5. Cafeteria Order Queue — Queue
   A queue serves students in the order they arrive, which matches the
   requirement to process cafeteria orders fairly. It supports simple enqueue
   and dequeue operations for sequential service.

Chosen feature: Event Registration System
"""

from typing import Dict, Optional


class EventRegistrationSystem:
    """Manage event participants using a hash table.

    Each participant is stored by a unique participant ID. The dictionary
    provides fast lookup, insertion, and removal operations.
    """

    def __init__(self) -> None:
        self._participants: Dict[str, dict] = {}

    def register_participant(
        self, participant_id: str, name: str, department: str
    ) -> None:
        """Register a participant if the ID is not already in use."""
        if participant_id in self._participants:
            raise ValueError(f"Participant {participant_id} is already registered.")

        self._participants[participant_id] = {
            "participant_id": participant_id,
            "name": name,
            "department": department,
        }

    def search_participant(self, participant_id: str) -> Optional[dict]:
        """Return the participant record, or None if the ID is not found."""
        return self._participants.get(participant_id)

    def remove_participant(self, participant_id: str) -> None:
        """Remove a participant using their unique registration ID."""
        if participant_id not in self._participants:
            raise ValueError(f"Participant {participant_id} was not found.")

        del self._participants[participant_id]

    def display_participants(self) -> None:
        """Display all registered participants in a readable table."""
        if not self._participants:
            print("No participants are registered.")
            return

        print("\nRegistered Participants")
        print("-" * 60)
        print(f"{'ID':<12} {'Name':<20} {'Department':<15}")
        print("-" * 60)

        for participant in self._participants.values():
            print(
                f"{participant['participant_id']:<12} "
                f"{participant['name']:<20} "
                f"{participant['department']:<15}"
            )

    def get_participant_count(self) -> int:
        """Return the number of registered participants."""
        return len(self._participants)


def main() -> None:
    """Run a simple event registration menu."""
    event_system = EventRegistrationSystem()

    while True:
        print("\nCampus Event Registration System")
        print("1. Register participant")
        print("2. Search participant")
        print("3. Remove participant")
        print("4. Display all participants")
        print("5. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            participant_id = input("Enter participant ID: ").strip()
            name = input("Enter participant name: ").strip()
            department = input("Enter department: ").strip()

            try:
                event_system.register_participant(participant_id, name, department)
                print("Participant registered successfully.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            participant_id = input("Enter participant ID: ").strip()
            participant = event_system.search_participant(participant_id)
            if participant is None:
                print("Participant not found.")
            else:
                print("Participant found:")
                print(participant)

        elif choice == "3":
            participant_id = input("Enter participant ID: ").strip()
            try:
                event_system.remove_participant(participant_id)
                print("Participant removed successfully.")
            except ValueError as error:
                print(error)

        elif choice == "4":
            event_system.display_participants()

        elif choice == "5":
            print("Exiting the event registration system.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
