contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name}.")

def search_contact(name):
    phone = contacts.get(name, "Contact not found.")
    print(f"{name}: {phone}")

# Test the system
add_contact("Alice", "555-0199")
add_contact("Bob", "555-0143")

search_contact("Alice")
search_contact("Charlie")