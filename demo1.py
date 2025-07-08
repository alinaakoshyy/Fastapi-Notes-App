#TASK MANAGER

tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")


def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def remove_task(task_number):
    list_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task description: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
