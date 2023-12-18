from collections import deque

class EventPlanningSystem:
    def _init_(self):
        self.events = {}
        self.students_tickets = {}
        self.reservation_queue = deque()
        self.bus_count = 0

    def add_event(self, event_name, event_date, ticket_limit):
        self.events[event_name] = {"date": event_date, "ticket_limit": ticket_limit}
        print(f"Event '{event_name}' added on {event_date} with a ticket limit of {ticket_limit}.")

    def show_events(self):
        if not self.events:
            print("No events available.")
            return

        print("Available Events:")
        for event_name, event_info in self.events.items():
            print(f"{event_name} - Date: {event_info['date']}, Ticket Limit: {event_info['ticket_limit']}")

    def reserve_ticket(self, student_name, event_name, ticket_count):
        if event_name not in self.events:
            print(f"Event '{event_name}' does not exist.")
            return

        if ticket_count <= 0:
            print("Invalid ticket count. Please reserve at least 1 ticket.")
            return

        if event_name not in self.students_tickets:
            self.students_tickets[event_name] = {}

        if student_name not in self.students_tickets[event_name]:
            self.students_tickets[event_name][student_name] = 0

        if self.students_tickets[event_name][student_name] + ticket_count > self.events[event_name]["ticket_limit"]:
            print(f"Cannot reserve {ticket_count} tickets for '{event_name}'. Exceeds ticket limit.")
            return

        self.reservation_queue.append((student_name, event_name, ticket_count))
        print(f"Reservation request for {ticket_count} tickets for '{event_name}' added to the queue.")

    def process_reservations(self):
        if not self.reservation_queue:
            print("No reservations to process.")
            return

        student_name, event_name, ticket_count = self.reservation_queue.popleft()
        if student_name not in self.students_tickets[event_name]:
            self.students_tickets[event_name][student_name] = 0

        self.students_tickets[event_name][student_name] += ticket_count
        print(f"{student_name} successfully reserved {ticket_count} tickets for '{event_name}'.")

    def show_student_tickets(self, student_name):
        if student_name not in self.students_tickets:
            print(f"{student_name} has not reserved tickets for any events.")
            return

        print(f"Tickets reserved by {student_name}:")
        for event_name, ticket_count in self.students_tickets[student_name].items():
            print(f"{event_name}: {ticket_count} tickets")

    def update_bus_count(self, new_bus_count):
        if new_bus_count < 0:
            print("Invalid bus count. Please provide a non-negative value.")
            return

        self.bus_count = new_bus_count
        print(f"Bus count updated to {new_bus_count}.")

    def update_ticket_limit(self, event_name, new_ticket_limit):
        if event_name not in self.events:
            print(f"Event '{event_name}' does not exist.")
            return

        if new_ticket_limit < 0:
            print("Invalid ticket limit. Please provide a non-negative value.")
            return

        self.events[event_name]["ticket_limit"] = new_ticket_limit
        print(f"Ticket limit for '{event_name}' updated to {new_ticket_limit}.")
event_system = EventPlanningSystem()

while True:
    print("\nEvent Planning System Menu:")
    print("1. Add Event")
    print("2. Show Available Events")
    print("3. Reserve Ticket")
    print("4. Process Reservations")
    print("5. Show Student's Tickets")
    print("6. Update Bus Count")
    print("7. Update Ticket Limit")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        event_name = input("Enter event name: ")
        event_date = input("Enter event date: ")
        ticket_limit = int(input("Enter ticket limit: "))
        event_system.add_event(event_name, event_date, ticket_limit)
    elif choice == "2":
        event_system.show_events()
    elif choice == "3":
        student_name = input("Enter student name: ")
        event_name = input("Enter event name: ")
        ticket_count = int(input("Enter ticket count: "))
        event_system.reserve_ticket(student_name, event_name, ticket_count)
    elif choice == "4":
        event_system.process_reservations()
    elif choice == "5":
        student_name = input("Enter student name: ")
        event_system.show_student_tickets(student_name)
    elif choice == "6":
        new_bus_count = int(input("Enter new bus count: "))
        event_system.update_bus_count(new_bus_count)
    elif choice == "7":
        event_name = input("Enter event name: ")
        new_ticket_limit = int(input("Enter new ticket limit: "))
        event_system.update_ticket_limit(event_name, new_ticket_limit)
    elif choice == "0":
        print("Exiting Event Planning System.")
        break
    else:
        print("Invalid choice. Please try again.")

