import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse

# Database configuration
DB_HOST = "127.0.0.1"  # Replace with your MySQL server host (e.g., IP address or domain)
DB_PORT = "3306"  # MySQL default port
DB_NAME = "student_database"  # Replace with your database name
DB_USER = "root"  # Replace with your MySQL username
DB_PASSWORD = urllib.parse.quote("lucky")

db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)


def update_data(student_id, field, new_value):
    query = text(f"UPDATE student_data SET {field}= :new_value WHERE id = :student_id")
    with engine.connect() as conn:
        conn.execute(query, {"new_value": new_value, "student_id": student_id})
        conn.commit()


st.title("Update Student Data")
student_id = st.number_input("Enter Student ID to update", min_value=1, step=0)
field = st.selectbox("Field to  Update", ["firstname", "lastname", "title", "age", "nationality", "registration_status", "num_courses", "num_semesters"])
new_value = st.text_input("New Value")
if st.button("Update"):
    try:
        update_data(student_id, field, new_value)
        st.success("Data successfully updated!")
    except Exception as e:
        st.error(f"Error updating data: {e}") 































