def read_todos(filepath):
    """
    Read and return a list of todos from a file.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todo_list, filepath):
    """
    Write a list of todos to a file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list)

def show_todos(todo_list):
    """
    Display todos from a given list with line numbers.
    """
    for index, item in enumerate(todo_list):
        item = item.strip('\n')
        print(f"{index + 1}-{item}")