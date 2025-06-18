# Contact Management System

contacts = []

# Function to add a new contact
def add_contact():
    store_name = input("Enter Store Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contact = {
        "Store Name": store_name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    
    contacts.append(contact)
    print("Contact added successfully.\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['Store Name']} - {contact['Phone']}")
    print()

# Function to search contact by name or phone
def search_contact():
    query = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if query in contact['Store Name'].lower() or query in contact['Phone']:
            print("\nContact Found:")
            for key, value in contact.items():
                print(f"{key}: {value}")
            found = True
            break
    if not found:
        print("Contact not found.\n")

# Function to update contact
def update_contact():
    name = input("Enter the store name to update: ").lower()
    for contact in contacts:
        if contact['Store Name'].lower() == name:
            print("Leave blank to keep current value.")
            phone = input(f"New Phone ({contact['Phone']}): ") or contact['Phone']
            email = input(f"New Email ({contact['Email']}): ") or contact['Email']
            address = input(f"New Address ({contact['Address']}): ") or contact['Address']
            
            contact['Phone'] = phone
            contact['Email'] = email
            contact['Address'] = address
            print("Contact updated successfully.\n")
            return
    print("Contact not found.\n")

# Function to delete contact
def delete_contact():
    name = input("Enter the store name to delete: ").lower()
    for i, contact in enumerate(contacts):
        if contact['Store Name'].lower() == name:
            del contacts[i]
            print("Contact deleted successfully.\n")
            return
    print("Contact not found.\n")

# Main menu
def main():
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
