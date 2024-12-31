import streamlit as st
import time as t

# title - it is used to add the title of an app
st.title("welcome  to streamlit")


#header 
st.header("machhine  learning")

# subheader
st.subheader("linear Regression")

# info

st.info("information details of user")

# warning
st.warning("come on time or else you'll marks as absent")


# write

st.write("Employee name")


# error message
st.error("wrong password")

# succsees msg

st.success("congrats you've got A grade")

# markdown
st.markdown(" #lucky")

st.markdown(":moon:")



# text
st.text("lucky lerner")


# to write a caption
st.caption("captionn here")

# to deisplay mathmetical equation
st.latex(r''' a+b z^2+c''')


# image




# widget
# chekbox
st.checkbox("Login")

#  button
st.button("click")

# radio
st.radio("pick your gender", ["male", "female"])

# select box
st.selectbox("pick your course", ["ml", "cloud", "cyber security"])

# multi select
st.multiselect("chose a department", ["content", "sales", "marketing"])

# select sliderr
st.select_slider("Rating", ["bad", "good", "execellent", "outstading"])

# slider
st.slider("Enter your number", 0,30)


# number input
st.number_input("pick a number", 0,200)


# text input
st.text_input("Enter your Email address")



# date input

st.date_input("Opening ceremony")

# time input
st.time_input("hey what's a timing")


# text area

st.text_area("welcomme to tha lucky website")



# upload file

st.file_uploader("Upload your file")

# chosing color

st.color_picker("color")

# progress

st.progress(90)


# spinner function

with st.spinner("just wait"):
    t.sleep(2)


# baloonns
st.balloons()


# sidebar
st.sidebar.title("luckypad")
st.sidebar.text_input("enter mail  address")
st.sidebar.text_input("enter password")
st.sidebar.button("submit")
st.sidebar.radio("Profassional Expert", ["Student", "Teacher", "Principal"])

# Data visualization

