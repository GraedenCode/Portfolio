import streamlit as st

# Set up the pages configuration
st.set_page_config(layout="wide", page_icon="Images/Icon.webp", page_title="Graeden Boyer")

# Create two columns with the specified gap
col1, col2 = st.columns(2, gap="small")

# Add content to the first column
with col1:
    st.image("Images/photo.png",use_column_width="always")

# Add content to the second column
with col2:
    st.title("Graeden Boyer")
    content = '''Hey, I am Graeden! I have been studying technologies hoping to land my first job in tech. I have been working in Sales for the last 5 years out performing everyone in our market.
    I have always had an interest in developing software and becoming a mentor to others in this field. I could never afford the loan to get into college for my field of study therefore,
    I have taken it upon myself to get the education and experience by developing application and use industry best standards to prepare me for a career in technologies.'''
    st.write(content)


st.write("Below Are some of my projects I have been working on to improve my skills.")

st.session_state