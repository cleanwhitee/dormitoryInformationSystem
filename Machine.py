class Machine:
    def _init_(self, machine_id, is_empty=True):
        self.machine_id = machine_id
        self.is_empty = is_empty
        self.children = []

def add_machine(parent, machine_id, is_empty=True):
    new_machine = Machine(machine_id, is_empty)
    parent.children.append(new_machine)
    return new_machine

def is_empty(machine):
    return machine.is_empty

def is_full(machine):
    return not machine.is_empty

def get_empty_machines(machine):
    empty_machines = []
    if machine.is_empty:
        empty_machines.append(machine.machine_id)
    for child in machine.children:
        empty_machines.extend(get_empty_machines(child))
    return empty_machines

def get_full_machines(machine):
    full_machines = []
    if not machine.is_empty:
        full_machines.append(machine.machine_id)
    for child in machine.children:
        full_machines.extend(get_full_machines(child))
    return full_machines

def show_menu():
    print("1. Add Machine")
    print("2. Check if a Machine is Empty")
    print("3. Check if a Machine is Full")
    print("4. List Empty Machines")
    print("5. List Full Machines")
    print("6. Exit")

def laundry_management():
    root_machine = Machine("root")  # Ana makineyi oluşturuyoruz

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            parent_id = input("Enter parent machine ID (or 'root' for main): ")
            parent = root_machine if parent_id.lower() == 'root' else find_machine(root_machine, parent_id)
            machine_id = input("Enter machine ID: ")
            is_empty = input("Is the machine empty? (True/False): ").capitalize() == "True"
            add_machine(parent, machine_id, is_empty)
        elif choice == "2":
            machine_id = input("Enter machine ID: ")
            machine = find_machine(root_machine, machine_id)
            result = is_empty(machine)
            print(f"Machine {machine_id} is {'empty' if result else 'not empty'}")
        elif choice == "3":
            machine_id = input("Enter machine ID: ")
            machine = find_machine(root_machine, machine_id)
            result = is_full(machine)
            print(f"Machine {machine_id} is {'full' if result else 'not full'}")
        elif choice == "4":
            empty_machines = get_empty_machines(root_machine)
            print("Empty Machines:", empty_machines)
        elif choice == "5":
            full_machines = get_full_machines(root_machine)
            print("Full Machines:", full_machines)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def find_machine(node, machine_id):
    if node.machine_id == machine_id:
        return node
    for child in node.children:
        found_machine = find_machine(child, machine_id)
        if found_machine:
            return found_machine
    return None

if _name_ == "_main_":
    laundry_management()