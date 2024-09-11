import streamlit as st

# Set up the page configuration
st.set_page_config(layout="wide", page_icon="Images/Icon.webp", page_title="Graeden Boyer")

# Data for the rows
data = [
    {"title": "Todo app", "image": "Images/TodoApp.png", "description": "This is my todo app. I used figma for planning out the design then used streamlit as the main functionality of the program"},
    {"title": "Camera Converter", "image": "Images/TodoApp.png", "description": "Description"}
]

# Create rows and display content in columns
for i, item in enumerate(data):
    # Create two columns with the specified gap
    col1, col2 = st.columns(2, gap="small")

    # Add content to the first column
    with col1:
        st.title(item["title"])
        st.image(item["image"])

    # Add content to the second column
    with col2:
        st.title(item["description"])

st.session_state