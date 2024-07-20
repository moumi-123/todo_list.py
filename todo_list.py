
def add_task(task_list):
    task = input("Enter a new task: ")
    task_list.append(task)
    print(f"Task '{task}' added.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def delete_task(task_list):
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(task_list):
            removed_task = task_list.pop(index)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    task_list = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            delete_task(task_list)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
