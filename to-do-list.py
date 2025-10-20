import os

# Define the filename where the tasks will be saved
TODO_FILE = "todo.txt"
# Initialize the global tasks list
tasks = []

def load_tasks():
    """Loads tasks from the persistent file (todo.txt) into the global tasks list."""
    global tasks
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as f:
                # Read all lines and strip newline characters
                tasks = [line.strip() for line in f.readlines()]
            print(f"Successfully loaded {len(tasks)} tasks from {TODO_FILE}.")
        except Exception as e:
            print(f"Error loading tasks: {e}")
            tasks = []
    else:
        print("No existing to-do file found. Starting with an empty list.")

def save_tasks():
    """Saves the current tasks list back to the persistent file (todo.txt)."""
    global tasks
    try:
        with open(TODO_FILE, 'w') as f:
            # Write each task on a new line
            for task in tasks:
                f.write(f"{task}\n")
        print(f"Successfully saved {len(tasks)} tasks to {TODO_FILE}.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def view_tasks():
    """Displays the current to-do list with numbered indices."""
    global tasks
    if not tasks:
        print("\nYour to-do list is empty! Add a task to get started.")
        return

    print("\n--- Current To-Do List ---")
    # Use enumerate to get both the index (i) and the item (task)
    for i, task in enumerate(tasks):
        # Display index starting from 1 for user readability
        print(f"{i + 1}. {task}")
    print("--------------------------")

def add_task():
    """Prompts the user for a new task and adds it to the list."""
    global tasks
    new_task = input("Enter the new task description: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"Task added: '{new_task}'")
        save_tasks() # Save immediately after modification
    else:
        print("Task description cannot be empty.")

def mark_complete():
    """Marks a task as complete by adding a [DONE] prefix."""
    global tasks
    if not tasks:
        print("No tasks to mark complete.")
        return

    view_tasks()
    try:
        # Ask for the task number (1-based index)
        task_num = int(input("Enter the number of the task to mark as COMPLETE: "))
        # Convert to 0-based index
        task_index = task_num - 1

        if 0 <= task_index < len(tasks):
            task_to_complete = tasks[task_index]
            if not task_to_complete.startswith("[DONE]"):
                tasks[task_index] = "[DONE] " + task_to_complete
                print(f"Task {task_num} marked as complete.")
                save_tasks()
            else:
                print(f"Task {task_num} is already marked complete.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_task():
    """Removes a task from the list based on user input."""
    global tasks
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks()
    try:
        # Ask for the task number (1-based index)
        task_num = int(input("Enter the number of the task to REMOVE: "))
        # Convert to 0-based index
        task_index = task_num - 1

        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Removed task {task_num}: '{removed_task}'")
            save_tasks()
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def display_menu():
    """Displays the main menu options to the user."""
    print("\n\n===== To-Do List Menu =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Remove Task")
    print("5. Exit and Save")
    print("===========================")

def run_app():
    """The main function to run the To-Do List application."""
    print("Starting To-Do List Application...")
    load_tasks() # Load tasks at startup

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

# This ensures the run_app function only executes when the script is run directly
if __name__ == "__main__":
    run_app()
