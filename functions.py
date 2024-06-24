# Separate functions in own file and main logic is in the cli.py
FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the List of
    to-do items
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the to-do items list in the text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)