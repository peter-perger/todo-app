from functions import get_todos
import streamlit as st

completed_todos = get_todos("files/completed.txt")
st.title(f"Completed todos✅ ({len(completed_todos)})")

for index, todo in enumerate(completed_todos):
    st.text(todo)
