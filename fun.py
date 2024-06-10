from datetime import datetime


def add_todo_item():
    todo_item = input("Enter a todo item: ") + "\n"
    file = open('todos.txt', 'r')
    todos = file.readlines()
    file.close()
    todos.append(todo_item)
    #todo_list.append(todo_item)
    file = open('todos.txt', 'w')
    file.writelines(todos)
    file.close()
    print("Todo item added successfully.")


def delete_todo_item():
    print_todo_list()
    file = open('todos.txt', 'r')
    todos = file.readlines()
    file.close()
    if len(todos) > 0:
        index = int(input("Enter the index of the todo item you want to delete: "))
        if 1 <= index <= len(todos):
            #del todo_list[index - 1]
            todos.pop(index - 1)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            print("Todo item deleted successfully.")
            print("The new list :\n")
            print_todo_list()
        else:
            print("Invalid index. Please enter a valid index.")
    else:
        print("Todo list is empty.")


def edit_todo_item():
    print_todo_list()
    file = open('todos.txt', 'r')
    todos = file.readlines()
    file.close()
    if len(todos) > 0:
        index = int(input("Enter the index of the todo item you want to edit: "))
        if 1 <= index <= len(todos):
            new_todo_item = input("Enter the new todo item: ") + "\n"
            todos[index - 1] = new_todo_item
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            print("Todo item edited successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    else:
        print("Todo list is empty.")


def print_todo_list():
    file = open('todos.txt', 'r')
    todos = file.readlines()
    file.close()
    print("\nYour todo list:")
    if len(todos) > 0:
        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            print(f"{index}. {item}")
    else:
        print("Todo list is empty.")


def getdt():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_datetime}")


def gettodo():
    file = open('todos.txt', 'r')
    todos = file.readlines()
    return todos
    file.close()


def writetodo(todos_arg):
    # todo_list.append(todo_item)
    file = open('todos.txt', 'w')
    file.writelines(todos_arg)
    file.close()
