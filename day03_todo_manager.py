#day03_todo_manager

# 1 — View all tasks
# 2 — Add a new task
# 3 — Remove a task by its number
# 4 — Exit the program

print("--- To-Do Manager ---")
print("1. View Tasks | 2. Add Task | 3. Remove Task | 4. Exit")

tasks = []

while True:
  choice = input("\nChoose an option (1-4): ").strip()

  if choice == "1":
    if not tasks:
      print("No tasks yet.")
    else:
      print("Your Tasks:")
      for idx, item in enumerate(tasks, start=1):
        print(f"{idx}. {item}")

  elif choice == "2":
    task = input("Enter task: ").strip()
    if task:
      tasks.append(task)
      print(f"Added: '{task}'")
    else:
      print("Task cannot be empty.")

  elif choice == "3":
    if not tasks:
      print("No tasks to remove.")
      continue

    for idx, item in enumerate(tasks, start=1):
      print(f"{idx}. {item}")

    num_input = input("Enter task number to remove: ").strip()
    if num_input.isdigit():
      task_num = int(num_input)
      if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Removed: '{removed}'")
      else:
        print(f"Please enter a number between 1 and {len(tasks)}.")
    else:
      print("Invalid input. Please enter a valid task number.")

  elif choice == "4":
    print("Goodbye!")
    break

  else:
    print("Invalid option. Please choose 1, 2, 3, or 4.")