# Simple Todo List Application
This is a command-line todo list application written in Python. The application allows users to manage their tasks efficiently by providing options to add, view, and delete tasks. Additionally, tasks are saved to a file so they persist across sessions.

## Features
Add Task: Easily add new tasks to your todo list.
View Tasks: Display all tasks currently in your todo list.
Delete Task: Remove a task from your list by selecting its number.
Save Tasks: Automatically saves your tasks to a file, ensuring they are available the next time you run the application.

# Installation
Prerequisites
Python 3.x: Ensure that Python 3 is installed on your system. You can download it from python.org.
Steps
Clone the Repository:

Clone the repository to your local machine using Git:

git clone https://github.com/yourusername/simple-todo-list.git
Navigate to the Project Directory:

Change the directory to the project folder:

cd simple-todo-list

# Usage
Run the Application:

To start the application, run the following command:

python todo.py

# Interact with the Application:

After running the application, you’ll see a menu with the following options:

Simple Todo List Application
1. Add a Task
2. View Tasks
3. Delete a Task
4. Exit
Add a Task: Enter 1 and follow the prompt to add a new task.
View Tasks: Enter 2 to view all your current tasks.
Delete a Task: Enter 3, and you'll be prompted to enter the number of the task you want to delete.
Exit: Enter 4 to save your tasks and exit the application.
File Storage:

The application stores tasks in a file named tasks.txt located in the same directory as the script. This file is created automatically when you first run the application and is updated whenever you add or delete tasks.

Example Session
Here’s what a typical session with the application might look like:

plaintext
Copy code
Simple Todo List Application
1. Add a Task
2. View Tasks
3. Delete a Task
4. Exit
Enter your choice (1/2/3/4): 1
Enter the task: Buy groceries
Task 'Buy groceries' added successfully.

Simple Todo List Application
1. Add a Task
2. View Tasks
3. Delete a Task
4. Exit
Enter your choice (1/2/3/4): 2
Tasks:
1. Buy groceries

Simple Todo List Application
1. Add a Task
2. View Tasks
3. Delete a Task
4. Exit
Enter your choice (1/2/3/4): 3
Enter the number of the task you want to delete: 1
Task 'Buy groceries' deleted successfully.

Simple Todo List Application
1. Add a Task
2. View Tasks
3. Delete a Task
4. Exit
Enter your choice (1/2/3/4): 4
Tasks saved. Exiting the program...
Project Structure
todo.py: The main Python script that contains the logic for the todo list application.
tasks.txt: A file where the tasks are saved. This file is automatically created and managed by the application.

# Contributing
Contributions are welcome! If you have ideas for improvements or new features, feel free to fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contact
For any inquiries or feedback, you can reach me at Matthewsnow35@gmail.com