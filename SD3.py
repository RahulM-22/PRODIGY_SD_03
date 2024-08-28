import json
import os

# Define the file name to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the contact name: ").strip()
    if name in contacts:
        print("A contact with this name already exists.")
        return
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 20)

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"Editing contact: {name}")
    phone = input(f"Enter the new phone number (current: {contacts[name]['phone']}): ").strip()
    email = input(f"Enter the new email address (current: {contacts[name]['email']}): ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} updated successfully.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact {name} deleted successfully.")

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit an existing contact")
        print("4. Delete a contact")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
