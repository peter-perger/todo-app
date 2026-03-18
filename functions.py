import streamlit as st

def get_todos(path):
    with open(path, "r") as file:
        todos = [todo.strip() for todo in file.readlines()]

    return todos

def add_todo(todos, path):
    todos = get_todos(path)
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    write_todos(todos, path)

def write_todos(todos, path):
    with open(path, "w") as file:
        for todo in todos:
            file.write(f"{todo} \n")

def remove_todo(todos, index):
    todos.pop(index)
    

if __name__ == "__main__":
    for i, t in enumerate(get_todos("files/completed.txt")):
        print(i, t)