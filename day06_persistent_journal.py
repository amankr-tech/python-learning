
# day06_persistent_journal.py

FILE_NAME = "journal.txt"

while True:
  print("\n--- Persistent Journal ---")
  print("1. Add Entry | 2. View All | 3. Search | 4. Exit")
  choice = input("Choose an option (1-4): ").strip()

  if choice == "1":
    value = input("Write your entry: ").strip()
    if not value:
      print("Entry cannot be empty.")
      continue
    with open(FILE_NAME, "a", encoding="utf-8") as file:
      file.write(value + "\n")
    print("Entry saved to journal.txt!")

  elif choice == "2":
    try:
      with open(FILE_NAME, "r", encoding="utf-8") as file:
        entries = [line.strip() for line in file if line.strip()]
      if not entries:
        print("No entries yet.")
      else:
        for idx, entry in enumerate(entries, start=1):
          print(f"{idx}. {entry}")
    except FileNotFoundError:
      print("No notes file found yet.")

  elif choice == "3":
    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
      print("Please enter a keyword.")
      continue
    try:
      with open(FILE_NAME, "r", encoding="utf-8") as file:
        found = False
        for idx, line in enumerate(file, start=1):
          clean_line = line.strip()
          if keyword in clean_line.lower():
            if not found:
              print("Matching Entries:")
            print(f"{idx}. {clean_line}")
            found = True
        if not found:
          print("No matching entries found.")
    except FileNotFoundError:
      print("No notes file found yet.")

  elif choice == "4":
    print("Goodbye!")
    break

  else:
    print("Invalid option. Please choose 1, 2, 3, or 4.")
