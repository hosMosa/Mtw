import streamlit as st
import fun

todos = fun.gettodo()


def add_todo():
    n_todo = st.session_state['add_todo'].strip()
    if n_todo:
        n_todo += '\n'
        todos.append(n_todo)
        fun.writetodo(todos)
        st.session_state['add_todo'] = ''


st.title("This is my TODO App")
st.subheader("MY TODO app")
st.write("This is will hopefully improves your productivity")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{i}")
    if checkbox:
        todos.pop(i)
        fun.writetodo(todos)
        del st.session_state[f"todo_{i}"]
        st.experimental_rerun()


# for todo in todos:
#    st.checkbox("todo")

st.text_input(label="", placeholder="Please enter a todo item...",
              key='add_todo', on_change=add_todo)


st.session_state