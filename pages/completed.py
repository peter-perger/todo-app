from functions import get_todos
import streamlit as st

completed_todos = get_todos("files/completed.txt")
st.title("Completed todos✅")
st.subheader(f"({len(completed_todos)})")

for index, todo in enumerate(completed_todos):
    st.text(todo)