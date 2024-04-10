import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print('It is', now)

while True:
    user_action = input("Type, add or show, edit, exit, complete: ")
    user_action = user_action.strip() 

    if user_action.startswith('add'):
        todo = user_action[4:].title() + '\n'
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = functions.get_todos()
        new_todos = []

        for item in todos:
            new_item = item.strip("\n")
            new_todos.append(new_item)

        for index, item in enumerate(new_todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            if user_action[5:].isnumeric():
                number = int(user_action[5:]) - 1
                todos = functions.get_todos()

                print(todos[number])
                todos[number] = (input("Type new edit: ").title()) + "\n"
                print(todos[number].strip("\n"), " was edited.")
            else:
                to_be_edited = user_action[5:].title() + '\n'
                todos = functions.get_todos()
                index_to_be_edited = todos.index(to_be_edited)
                todos[index_to_be_edited] = (input('Type new edit: ') + '\n').title()
                functions.write_todos(todos)
                print('edited successfully')

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            completed_task = int(user_action[9:]) - 1
            todos = functions.get_todos('todos.txt')

            removed_task = todos[completed_task].strip('\n')
            todos.pop(completed_task)
            functions.write_todos(todos)
            print(removed_task, " was completed successfully.")
        except IndexError:
            print("That index number doesn't exist, try again.")
            continue

    elif "exit" in user_action:
        break
    else:
        print("Command is not valid")

print("Bye!")
