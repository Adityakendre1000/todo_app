from functions import read_todos,write_todos,show_todos
import time

now = time.strftime("%d %b, %Y. %H:%M:%S")
print(now)

todo_file_name = input("Select TODO list to open: ")

while True:
    user_action = input("add, show, edit, complete, exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # Extract the new todo from user input
        todo = user_action[4:] + '\n'

        # Read existing todos from the selected file
        todos = read_todos(todo_file_name + '.txt')

        # Add the new todo to the list of existing todos
        todos.append(todo)

        # Write the updated list of todos back to the file
        write_todos(todos, todo_file_name + '.txt')

    elif user_action.startswith('show'):
        # Read and display the todos from the selected file
        todos = read_todos(todo_file_name + '.txt')
        show_todos(todos)

    elif user_action.startswith('edit'):
        try:
            # Read existing todos from the selected file
            todos = read_todos(todo_file_name + '.txt')

            # Extract the index of the todo to be edited
            number = int(user_action[5:]) - 1

            # Display the existing todo to be edited
            existing_todo = todos[number]
            print(existing_todo)

            # Prompt the user for the new todo and update the list
            new_todo = input("Replace existing todo with: ") + '\n'
            todos[number] = new_todo

            # Write the updated list of todos back to the file
            write_todos(todos, todo_file_name + '.txt')
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            # Read existing todos from the selected file
            todos = read_todos(todo_file_name + '.txt')

            # Extract the index of the todo to be marked as complete and remove it
            number = int(user_action[9:])
            todos.pop(number - 1)

            # Display the updated list of todos
            print("The new todo list is as follows: ")
            show_todos(todos)

            # Write the updated list of todos back to the file
            write_todos(todos, todo_file_name + '.txt')
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        # Exit the program if the user chooses to
        break

    else:
        # Display an error message for invalid commands
        print("Command is not valid.")

print("Bye!")
