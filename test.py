import streamlit as st

st.title("Hello, nitish!")

st.write("This is my first streamlit app.")

st.text("This is plain text.")

st.markdown("this is markdown text.")

name = st.text_input("Enter your name:")

age = st.number_input ("Enter your age")

st.write(f"Hello {name}, you are {age} year old!")

uploaded_file = st.file_uploader("Choose file")
if uploaded_file:
    st.write("file uploaded:", uploaded_file.name)


st.sidebar.header("sidebar")

option = st.sidebar.selectbox("Choose an option:", ['alok', 'rachit'])



