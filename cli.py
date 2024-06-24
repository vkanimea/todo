# from functions import get_todos, write_todos, to use function.get_todos, or functions.write_todos
import functions
import time

now = time.strftime ( "%b %d, %Y %H:%M:%S" )
print ( "It is", now )

while True :
    user_action = input ( "Type add <todo>, show, edit <no>, complete <no>, sort or exit: " )
    user_action = user_action.strip ()  # remove spaces

    if user_action.startswith ( 'add' ) :
        todo = user_action[4 :] + '\n'  # list slicing starting with char after index 4 .. i.e todo
        todos = functions.get_todos ()
        todos.append ( todo )  # append instead of overwriting

        functions.write_todos ( todos )

    elif 'show' in user_action :
        todos = functions.get_todos ()
        for index, item in enumerate ( todos ) :  # index & enumerate allows for no along with values
            item = item.strip ( '\n' )
            row = f"{index + 1}-{item.title ()}"  # f strings use {} for variables
            print ( row )
    elif 'edit' in user_action :
        try :
            no = int ( user_action[5 :] )
            no = no - 1
            todos = functions.get_todos ()
            new_todo = input ( "Enter new todo: " )
            todos[no] = new_todo + '\n'

            functions.write_todos ( todos )

        except ValueError :
            print ( "Your Command is not valud" )
            continue  # Continue the while loop i.e ask for user_action
    elif 'complete' in user_action :
        try :
            number = int ( user_action[9 :] )
            todos = functions.get_todos ()
            index = number - 1
            todo_to_remove = todos[index].strip ( '\n' )
            todos.pop ( index )

            functions.write_todos ( todos )

            message = f"Todo {todo_to_remove} was removed from the list"
            print ( message )
        except ValueError :
            print ( "Your Command is not valud" )
            continue  # Continue the while loop i.e ask for user_action
    elif 'sort' in user_action :
        todos = functions.get_todos ()
        todos.sort ()

        functions.write_todos ( todos )

        print ( f"Todos Sorted. {todos} Type 'show' to view" )
    elif 'exit' in user_action :
        break
    else :
        print ( 'Command is not valid' )

print ( "Bye" )
