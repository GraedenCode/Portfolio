import streamlit as st

divs = ()

 = ({"col1" : "Project"}, {"col2" : "prodesc"})

# change range to change number of rows
for i in range(2):
    # this effects columns/width
    row = st.columns(2)

    for i,col in enumerate(row):
        tile = col.container(height= 120)
        tile.title("bla")
        print(dict[i-1])

st.session_state


# on creation it should find its data within a csvlist.

