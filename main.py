import streamlit as st

st.set_page_config(layout="wide",page_icon="Images/Icon.webp", page_title="Graeden Boyer")

data = (({"title":"Todo app", "image": "Images/TodoApp.png"}, {"description": "Description"}),({"title":"Camera Converter", "image": "Images/TodoApp.png"},{"description":"Description"}))

# change range to change number of rows
for i, number in enumerate(range(len(data))):
    # this effects columns/width
    row = st.columns(2, vertical_alignment="bottom",gap="small")

    for index, col in enumerate(row):
        tile = col.container(height= 750, border=False)
        if index == 0:
            tile.title(data[i][index]["title"])
            tile.image(data[i][index]["image"])
        if index == 1:
            tile.title(data[i][index]["description"])

st.session_state


# on creation it should find its data within a csvlist.

