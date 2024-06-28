""" this is the main file for the web app """

import streamlit as st
import functions as fn


def add_todo():
    """this function adds a new todo to the list of todos"""
    local_todo = st.session_state["new_todo"] + "\n"
    todos.append(local_todo)
    if local_todo != "":
        fn.add_todos(todos)


st.title("My todo app")
st.subheader("This is a simple todo app")
st.write("This app is for increasing productivity")

todos = fn.get_todos()
for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        fn.add_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(
    label="Add new todo",
    placeholder="Type new todo...",
    key="new_todo",
    on_change=add_todo,
)
