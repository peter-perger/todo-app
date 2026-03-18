from functions import get_todos, write_todos, add_todo
import streamlit as st 
from pathlib import Path

todos = get_todos("files/todos.txt")

st.set_page_config(page_title = "Todo App", page_icon = "✅")
st.title("ToDo app ✅")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        
        completed = get_todos("files/completed.txt")
        completed.append(todo)
        write_todos(completed, "files/completed.txt")

        todos.pop(index)
        write_todos(todos, "files/todos.txt")
        
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter new todo!", on_change=add_todo, args=(todos, "files/todos.txt"), key="new_todo")