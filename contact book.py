import json
import os

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists('contacts.json'):
            with open('contacts.json', 'r') as file:
                self.contacts = json.load(file)

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        
        if name and phone and email and address:
            self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
            print("Contact added successfully!")
            self.save_contacts()
        else:
            print("Please fill in all fields.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        if not search_term:
            return
        
        found_contacts = [contact for contact in self.contacts if search_term in contact['name'] or search_term in contact['phone']]
        
        if not found_contacts:
            print("No contact found with the given name or phone number.")
            return
        
        for contact in found_contacts:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

    def update_contact(self):
        search_term = input("Enter name or phone number to update: ")
        if not search_term:
            return
        
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                new_name = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
                new_phone = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
                new_email = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
                new_address = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
                
                contact['name'] = new_name
                contact['phone'] = new_phone
                contact['email'] = new_email
                contact['address'] = new_address
                print("Contact updated successfully.")
                self.save_contacts()
                return
        
        print("No contact found with the given name or phone number.")

    def delete_contact(self):
        search_term = input("Enter name or phone number to delete: ")
        if not search_term:
            return
        
        for contact in self.contacts:
            if search_term in contact['name'] or search_term in contact['phone']:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                self.save_contacts()
                return
        
        print("No contact found with the given name or phone number.")

    def main_menu(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.main_menu()
