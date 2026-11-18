# day04_contact_book

# 1 — Add or update a contact
# 2 — Search for a contact by name
# 3 — View all contacts
# 4 — Delete a contact
# 5 — Exit


# day04_contact_book.py

contacts = {}
print("--- Contact Book ---")
print("1. Add/Update | 2. Search | 3. View All | 4. Delete | 5. Exit")

while True:
  choice = input("\nChoose an option (1-5): ").strip()

  if choice == "1":
    name = input("Enter name: ").strip().title()
    number = input("Enter phone number: ").strip()

    if not name:
      print("Name cannot be empty.")
    elif number.isdigit():
      action = "Updated" if name in contacts else "Saved"
      contacts[name] = number
      print(f"{action} contact: {name} -> {number}")
    else:
      print("Please enter a valid numeric phone number.")

  elif choice == "2":
    name = input("Enter name to search: ").strip().title()
    number = contacts.get(name)
    if number:
      print(f"{name}'s number: {number}")
    else:
      print("Contact not found.")

  elif choice == "3":
    if not contacts:
      print("Contact book is empty.")
    else:
      for name, number in contacts.items():
        print(f"{name} : {number}")

  elif choice == "4":
    name = input("Enter name to delete: ").strip().title()
    if name in contacts:
      contacts.pop(name)
      print(f"Deleted contact: {name}")
    else:
      print("Contact not found.")

  elif choice == "5":
    print("Exiting Contact Book. Goodbye!")
    break

  else:
    print("Invalid input. Please choose a number between 1 and 5.")