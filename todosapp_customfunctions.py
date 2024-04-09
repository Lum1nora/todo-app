def get_todos(filepath='todos.txt'):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local
        #2 breaklines between functions
print(help(get_todos))
def write_todos(todos_arg, filepath='todos.txt'):
    """ Writes in the database."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type, add or show, edit, exit, complete: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:].title() + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = get_todos()
        new_todos = []

        for item in todos:
            new_item = item.strip("\n")
            new_todos.append(new_item)

            #new_todos = [item.strip() for item in todos]

        for index, item in enumerate(new_todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            if user_action[5:].isnumeric():
                number = int(user_action[5:]) - 1
                todos = get_todos()

                print(todos[number])
                todos[number] = (input("Type new edit: ").title()) + "\n"
                print(todos[number].strip("\n"), " was edited.")
            else:
                to_be_edited = user_action[5:].title() + '\n'
                todos = get_todos()
                index_to_be_edited = todos.index(to_be_edited)
                todos[index_to_be_edited] = (input('Type new edit: ') + '\n').title()
                write_todos(todos)
                print('edited successfully')

            write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        #completed_task = int(input("Number of task completed: ")) - 1
        try:
            completed_task = int(user_action[9:]) - 1
            todos = get_todos('todos.txt')

            removed_task = todos[completed_task].strip('\n')
            todos.pop(completed_task)
            write_todos(todos)
            print(removed_task, " was completed successfully.")
        except IndexError:
            print("That index number doesn't exist, try again.")
            continue

    elif "exit" in user_action:
        break
    else:
        print("Command is not valid")
print("Bye!")