import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Personal Budget Tracker")

if "expanse" not in st.session_state:
    st.session_state.expanses = pd.DataFrame(columns=["Description", "Category", "Amount"])

st.header("Add a New Expanse")

description = st.text_input("Expanse Description")
amount = st.number_input("Amount", min_value=0.0, step=0.01)
category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Other"])


if st.button("Add Expense"):
    new_expense = pd.DataFrame([{"Description": description, "Category": category, "Amount": amount}])
    st.session_state.expanses = pd.concat([st.session_state.expanses, new_expense], ignore_index=True)
    st.success("Expense added successfully!")




st.header("Summary")

if not st.session_state.expanses.empty:
    st.write("### Total Expenses")
    total = st.session_state.expanses["Amount"].sum()
    st.write(f"{total:.2f} Rs")

    st.write("### Expenses by Category")
    category_summary = st.session_state.expanses.groupby("Category")["Amount"].sum()
    st.bar_chart(category_summary)
else:
    st.write("No expenses added yet.")


st.header("Upload Past Expanses")
uploaded_file = st.file_uploader("upload a CSV file", type=["csv"])

if uploaded_file:
    uploaded_data = pd.read_csv(uploaded_file)
    if set(["Description", "Category", "Amount"]).issubset(uploaded_data.columns):
        st.session_state.expanses = pd.concat([st.session_state.expanses, uploaded_data], ignore_index=True)
        st.success("csv data added success fully!")
    else:
        st.error("Invalid file formate. Please upload a file with columns Description, Category, Amount.")