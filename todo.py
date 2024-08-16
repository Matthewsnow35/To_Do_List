import os


tasks = [] # Initializes an empty list to store tasks
filename = "tasks.txt"

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.\n")


def view_tasks():
    if not tasks:
        print("No tasks found.\n")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print() # Prints a new line for better readability


def delete_task():
    view_tasks()
    if not tasks:
        return
    
    try: 
        task_number = int(input("Enter the number of the task you want to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully. \n")
        else:
            print("Invalid input. Please enter a number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


def save_tasks():
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")



def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                tasks.append(line.strip())


def main():
    load_tasks()


    while True:
        print("Simple Todo List Application")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Delete a Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice =='1':
            add_task()
            pass
        elif choice == '2': 
            view_tasks()
            pass
        elif choice == '3':
            delete_task()
            pass
        elif choice == '4':
            save_tasks()
            print("Tasks saved. Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()



